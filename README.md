# Testes Unitários

## O que é teste unitário
Teste unitário é um tipo de teste automatizado que valida a menor parte testável do sistema (funções, métodos ou classes) de forma isolada, verificando se ela produz o resultado esperado.

## Para que serve
### Os testes unitários servem para:
- Garantir que cada unidade do código funcione corretamente;
- Identificar erros de forma precoce;
- Evitar regressões após alterações no código;
- Aumentar a confiabilidade e a manutenibilidade do sistema.

## Como o Django testa
### O Django fornece suporte nativo a testes por meio da classe `TestCase`, localizada no módulo `django.test`.

- `TestCase`: permite criar testes automatizados que rodam de forma isolada, utilizando um banco de dados de teste criado e destruído automaticamente a cada execução.
- `manage.py test`: comando responsável por localizar os testes do projeto, preparar o ambiente de testes, executar os métodos definidos nas classes `TestCase` e exibir o resultado no terminal.
