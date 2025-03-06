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
iaC
Infraestrutura como código

Um script que jogam no Azure e roda tudo.

Terraform - A principal, agnostico de nuvem



## Aula 06/03/2025

Tratar seus recursos como descartaveis

Acoplamento

Algo altamente acoplato é algo que não pode ser altamente substituido

HDMI: baixo acoplamento

Anti-pattern: Não queremos que isso aconteça
- Geralmente nas empresas isso é o banco de dados, se o banco cai, cai a aplicação
- Como resoler: cria várias replicas do banco e colocamos um load balancer no meio. Quando qualquer maquina tentar conectar o load balancer escolhe quem vai responder. Essa é a melhor pratica.

#### Faça o design de serviços, não de servidores

- Container
- Serverless
- Comunicação baseada em mensagem
- Sites estaticos
- Autenticação

- Configure um EC2, instalo apache2 e copio o html, css e js pra lá: SERVIDOR

- Crio um S3, copio o html, css e js pra lá e usop web hosting da AWS: SERVIÇO

#### Escolher o banco de dados correto

- Temos o Relacional, o mais "tradicional"
- E temos também o NoSQL

- Relacional: O problema é a escalabilidade horinzontal
Aumentar memoria, hd, cpu, é escalabilidade vertical.
Essas replicas verticais é somente replica de leitura, esse é o gargalo do relacional.
NoSQL pode escalar até o infinito em alguns casos, replicas em leitura E escrita.
- NoSQL: Performance extrema e quando você não consegue modelar a tabela do banco de dados.


#### Evitar pontos unicos de falha

- Historia do banco, caiu banco, caiu aplicação.

#### Otimizar custos

- Existe duas IAs que analisam a sua conta, Exemplo: duas maquinas aqui estão mair parte do tempo paradas e essas outras estão no maximo.

- Não esbanjar, não usar algo grande para matar uma mosca.

- Uso de cache. Aos invés de vir toda vez no S3, ele vai num datacenter mais perto, o arquivo vai do S3 para o servidor cache atráves da rede da AWS, NÃO usa internet, é uma rede global otimizada.

##### Segurança

- Luta eterna. Paga muito bem, precisa de muita gente, profissional altamente qualificado.

az cojunto de data centers

##### Local Zones
- Rodar serviço computacional onde ainda não tem serviços da AWS
- Como se fosse uma pequena AZ numa localidade
- Existe parar lugares numa grande concentraççao populacional, que não justifica uma AZ, mas é necessario ter servidores lá.


###### Wavelength Zone

- Do que adianta ter um serviço, Uber, que usa o 5G, tem uma transferencia alta, mas chega na antena da operadora, o trafego tem que trafegar pela internet, fica mais "lento". Ai colocaram a AWS para rodar dentro da operadora de telefonia.


