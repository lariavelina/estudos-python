# mini-projeto-de-checkpoint-em-python

Mini projeto de checkpoint para aula de Computational Thinking Using Python.
 
## Sobre o projeto
 
O sistema recebe informações sobre a infraestrutura da plataforma e realiza uma sequência de verificações utilizando estruturas condicionais (`if`, `elif` e `else`).
 
Entre as informações analisadas estão:
 
* Quantidade prevista de usuários;

* Quantidade de servidores disponíveis;

* Capacidade máxima de usuários por servidor;

* Latência atual da plataforma;

* Quantidade de erros críticos encontrados;

* Porcentagem de utilização do disco.
 
Com base nesses dados, o programa apresenta uma decisão sobre o lançamento.
 
## Regras do sistema
 
O programa segue as seguintes regras:
 
### Lançamento bloqueado
 
O lançamento é bloqueado quando:
 
1. Não existem servidores disponíveis;

2. A quantidade prevista de usuários por servidor ultrapassa a capacidade máxima;

3. Existe pelo menos um erro crítico encontrado.
 
### Lançamento adiado
 
O lançamento é adiado quando a latência atual da plataforma é superior a **300 ms**.
 
### Lançamento com alerta
 
O lançamento é autorizado com alerta quando a utilização do disco ultrapassa **90%**.
 
### Lançamento autorizado
 
Se nenhuma das condições anteriores for identificada, o lançamento é autorizado normalmente.
 
## Conceitos de Python utilizados
 
Este projeto foi desenvolvido para praticar conceitos fundamentais de programação, incluindo:
 
* `input()`

* Conversão de tipos com `int()` e `float()`

* Variáveis

* Operadores de comparação

* Operadores matemáticos

* Estruturas condicionais

* `if`, `elif` e `else`

* Divisão de valores

* Tomada de decisão baseada em regras de negócio
 
## 🎯 Objetivo de aprendizagem
 
O principal objetivo deste projeto é desenvolver a capacidade de transformar **regras de negócio em lógica de programação**, utilizando Python.
 
O exercício também ajuda a compreender como diferentes condições podem ser analisadas em sequência para que um sistema tome decisões automaticamente.
 
## Colaboradores:

Gabrielly Santos - github: @gabrielymoreira;

Isabelly Viana - github: @isabellyvianachavier;

Larissa Avelina - github: @lariavelina.
 
