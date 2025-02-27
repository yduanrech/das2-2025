# Design e Arquitetura de Software 2

Yduan Rech Effting

## Aula 27/02/2025

Toda vez que vamos projetar um sistema, temos que escolher uma linguagem de programação, tendo muitas variedades, +200

Geralmente escolhemos a linguagem que mais conhecemos, mas nem sempre é a melhor opção. (Trade-Offs)

Podemos abrir mão de uma segurança melhor (Ex: C vs Rust), desempenho melhor pela comodidade.

Todo sistema precisa ser consistente o tempo todo? Depende
    1. Se for um sistema financeiro, sim
    2. Numa rede social não há necessidade

### Durabilidade
- Gravar uma informação e o BD garante que aquela informação vai ser mantidade ali
- Se usarmos cache, não podemos manter a informação para sempre, por conta de inconsistencia.
- Pode ocorrer sobrecarga do servidor de cache por conta que a RAM é limitada

        Terceira forma normal: Serve para reduzir redundancia, eliminar coisas repetidas

### Escalabilidade
Se chega num limite que a linguagem de promamação não consegue acompanhar (ex: php não consegue mais utilizar memoria no site da univille), vamos precisar de mais maquinas, de forma automatica, alarmes. Se for topar, ele coloca mais maquina automaticamente.

Qual o trade-off aqui? 
- Ganha consistencia
- Ganha Disponibilidade
- Perde Dinheiro

Isso não precisa ser pra sempre, não precisamos comprar uma maqina nova pra isso. Por isso podemos usar a nuvem, numa estrutura elastica. Pedir o servidor pelo tempo que precisa, geralmente automaticamente e depois quando não precisa, não paga mais por ela.

O que podemos fazer para melhor a percepção do usuario?

        Ex: Uma maquina crashou
        

### Outra dica
laC
Infraestrutura como código

Um script que jogam no Azure e roda tudo.

Terraform - A principal, agnostico de nuvem




