from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.UserUsuarioForm import UserUsuarioForm, UserForm

def list_usuario_view(request, id=None):
    usuarios = Usuario.objects.filter(perfil=2)
    context = {'usuarios': usuarios}
    return render(request, 'usuario/usuario.html', context, status=200)

def edit_usuario_view(request):
    usuario = get_object_or_404(Usuario, user=request.user)
    emailUnused = True
    message = None  # Variável para guardar mensagem de feedback

    if request.method == 'POST':
        usuarioForm = UserUsuarioForm(request.POST, instance=usuario)
        userForm = UserForm(request.POST, instance=request.user)

        # Verifica se o email já existe para outro usuário
        verifyEmail = Usuario.objects.filter(
            user__email=request.POST['email']
        ).exclude(user__id=request.user.id).first()

        emailUnused = verifyEmail is None

        if usuarioForm.is_valid() and userForm.is_valid() and emailUnused:
            usuarioForm.save()
            userForm.save()
            message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }
            # return redirect('usuarios')
        else:
            if not emailUnused:
                message = { 'type': 'warning', 'text': 'E-mail já usado' }
            else:
                message = { 'type': 'danger', 'text': 'Dados inválidos' }

    else:
        usuarioForm = UserUsuarioForm(instance=usuario)
        userForm = UserForm(instance=request.user)

    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm,
        'message': message
    }
    return render(request, 'usuario/usuario-edit.html', context, status=200)
