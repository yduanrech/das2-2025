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

### Região
No brasil temos somente uma da AWS.


### Zona de disponibilidade
Um local com um conjunto de um ou mais datacenters.
Todas as regioes da AWS tem no minimo um AZ 

Corrigir depois

##### Local Zones
- Rodar serviço computacional onde ainda não tem serviços da AWS
- Como se fosse uma pequena AZ numa localidade
- Existe parar lugares numa grande concentraççao populacional, que não justifica uma AZ, mas é necessario ter servidores lá.


###### Wavelength Zone

- Do que adianta ter um serviço, Uber, que usa o 5G, tem uma transferencia alta, mas chega na antena da operadora, o trafego tem que trafegar pela internet, fica mais "lento". Ai colocaram a AWS para rodar dentro da operadora de telefonia.


### AZ 

Local zone parecida com AZ, mas ela é menor, ela não justifica ter uma regiçao, não justifica ter um AZ, tem só um datacenter.


## Corrigido

#### Região

É um conjunto de AZs

#### AZ

Uma AZ é um conjunto de um ou mais datacenters fisicos interconectados dentro de uma região.

#### Local Zones

Uma infra da AWS que não é uma região???

#### Edge localtions

É um PoP usados para serviços de cache e entrega de conteúdo.

##### Como entregar um site estatico? Ex: Angular

Há mais de uma resposta, mas o mais barato e que faz + sentido é um PoP.

Mas se eu hospedar dentro do Brasil também está certo.


## Aula 10/03/2025

### Securing Access

- Quando você roda seus sistemas on-premise, a responsabilidade é sua.
- Quando roda numa nuvem a responbilidade é compartilhada. Não é totalmente responsabilidade da AWS.

- Iaas (Infraestrutura como serviço)/EC2/Servidor
- Quando eu entro ele me pergunta tudo sobre o servidor, ram, cpu, etc e em minutos o servidor estará pronto.
- A responsibilidade da AWS é região, az, local zone, rack, servidor, ar condicionado, bateria. A infra global, links das regioes eles são responsaveis.
- O computador fisico, HD, SSD, BD, toda parte fisica é responsabilidade da AWS.

- Você por acaso subiu um servidor de minecraft e deixou a porta 22 aberta para a internet e coloquei a senha admin, admin e a maquina foi invadida e mineraram bitcoin nela, quem é responsável? Você. Nesse caso você cometeu o erro, você deixou a porta aberta.

- Agora se tem uma falha num software da AWS que permite uma invasão? a AWS é responsável.

- Colocou uma senha fraca, não habilitou criptografia? Se der BO a culpa é sua.

- Tem uma falha no linux e você não aplicou um patch de segurança? Você é o culpado.

- Estamos usando a infraestrutura como serviço. Ela é reponsável. O que roda ali em cima ela não sabe, não é responsável.

##### Outro extremo

- S3: é quase um SaaS/PaaS, fica num meio termo entre os dois. É um cara, que eu crio um bucket e cria um endereço na internet, ai você pode colocar e tirar arquivos de lá.

- Nesse caso tem algumas partes de responsabilidade que continuam com a AWS.

- Rede, Firewall e OS: Tudo responsabilidade da AWS no caso do **S3**

- Teve um caso de ranson no S3 que roubava arquivos
Como funcionava: Um dos serviços que o S3 oferece é criptografia quando sobe os arquivos. Esse serviço se chama:

##### Server Side Encryption (SSE):
Temos 4 modelos:
1. SS3-S3: Quando eu subo um objeto pro S3, criptografa em uam chave unica que ela cria na minha conta. Quando peço ela pega a chave, descriptografa e me entrega o arquivo.
(Modelo Default)

2. SSE-KMS (Key managment Server): A empresa precisa ter o controle da chave. Vai la no cofre e pega a minha chave e faz o mesmo processo.

3. SSE-C (Customer): Eu nãoconfio na AWS, quando vou subir um objeto no S3, eu subo o objeto e a chave. Ela criptografa e joga fora a chave, só guarda os dados criptografados. Ela não sabe o que tem aqui dentro. Pra baixar eu tenho que dar a chave novamente, para a AWS descriptografar. Ela não tem posso da chave.

Eles colocaram o ransonware nesse terceiro modelo. Tinham todos os arquivos do S3. O cliente configurou errado o bucket, o hacker conseguia trocar o modelo para o terceiro e ele usa uma chave que só o hacker tem acesso.

Um software roda e troca o tipo de criptografia do bucket, pois os clientes deixam a configuração do bucket muito aberto, não é culpa da AWS.

4. SSE-DKMS (Depois vamos ver)

#### Principios para ter uma aplicação segura

1. Provedor de identidade forte.
(Há empresas que guardam login e senha em banco de dados)
Aprendemos a colocar no banco na faculdade pois é facil, mas para empresas grandes é risco

Ex: keycloak (provedor de identidade)
Foram pensados em guardar dados da melhor forma conhecida.


2. Proteger dados em transito ou em descanço

Qual o principal protocolo padrão de proteção de dados em transito? SSL/TLS, muito conhecido o HTTPS.

AWS, Microsoft, Google investem na Let's Encrpypt, para não deixar dados vazarem em transito.

- Criptografia em descanço: Quando está gravado no disco.
Criptografar um S3 em disco? É criptografia em descanço
Criptografar o disco do servidor? Sim

Existe um terceiro:
- Criptografia em Uso: Computing Confidencial Consorce, criptografar a memoria RAM do servidor em uso, só o teu software enxerga o que está naquela parte da memoria.

Intel: Enclave

AMD: tecnologia no processador criptografa a memoria RAM inteira, perda de performance minima.

3. Aplicar segurança em todas as camadas

- As vezes a unica ferramenta de segurança é o firewall e antivirus. Precisamos ter segurança em varias camadas.
Se uma camada for prejudicada o atacante cair em outra camada.

4. Manter os dados longe das pessoas

Não dar acesso direto as fontes de dados.

Passar por uma autenticação etc. Só assim para ter acesso.

A AWS pode ser Deus, se a AWS não deixar ele não deixa fazer um select. ver o nome.

5. Ter rastreabilidade

Preciso saber quando um usuario logou no meu sistema, o que ele fez, o que foi que aconteceu na nuvem.

6. Se preparar para eventos de segurança

Tem que ter uma equipe de segurança 24/7 caçando problema o tempo todo.

7. Automatizar as melhores praticas de segurança (pois você vai esquecer)

Se criar um usuário na mão, vai criar errado.


#### Conceitos

1. Autenticação (Dizer que você é você mesmo)


O que eu sei (login e senha)
o que eu sou (biometria)
o que eu tenho (dispositivo)

2. Autorização (permissões)

o Jogn pode mexer nesses dois baldes, mas NÃO pode mexer nesse banco de dados.

Isso é autorização. Na AWS é feito atraves de um documento chamado **IAM policy**

3. Principio do privilegio minimo

O John é adm, ele tem total acesso a tudo, e está tudo bem.

Agora a Mary é do Marketing, porque vou dar acesso de ADM para a Mary, se ela só precisa ter acesso ao bucket? Não precisa

Dar ao usuario apenas as permissões necessárias para executar uma tarefa.

4. Use encriptação

Se trafegar dados na internet, tem que usar criptografia. Mesmo que seja local.



## Aula 13/03/25


### Aula anterior
- Modelo de responsabilidade compartilhado
- Principio do privilegio minimo
- autenticação
- autorização
- Identity and access management
- usuarios
- acesso pela console / acesso programatico

### Meios de acesso a AWS
- Acesso Console (Web)
- Acesso Programatica (AWS CLI)

### Criação de user e grous
- IAM User
- IAM Group



### Informações para configurar o acesso programatica (AWS CLI)
- Acess Key
- Secrety Key


### Melhores praticas
- Hablitar MFA
- Definir expiração da conta

### Usuário root
- Usuário master, pode fazer tudo na conta
- Habilitar MFA
- **NUNCA** usar no dia a dia

### Criação e usuario novo
- Por padrão ele não tem nenhuma permissão
- Temos que dar uma permissão nas `policies`


### IAM Roles
- IMPORTANTE
> Zezinho trabalha no banjedão
>
> Mas ele trabalha na cozinha
>
>Todo mundo quer comer quando chega na facul
>
> E a fila do caixa fica gigantesca
>
> Zezinho lava a mao e fica no caixa
>
> Ele perde a permissão de acessar a cozinha e ganha permissão para acessar o caixa
>
- Para faezr isso vou no console, e crio uma **Role**

- Vou copiar o ARN (Um código unico)
> AWS Pergunta: Pra quem você confia 
>
>Dou a permissão para que ele possa assumir outros papeis
>
>Quem 
>
>Rever



#### Qual a vantagem?

- Com role definimos o tempo maximo de sessão (1 ou 12h)

1. A sessão do zezinho deixa de valer e ele perde esse papel e ele volta ao papel original dele.

2. Toda vez que voce assume uma **role**, eu bato no **sts**

3. Gera uma nova access key e secrety key e usa uma nova chave.

4. É uma chave de curta direção, se vazar não há tanto problema.

5. Se o tempo acabar ele pode assumir e novo, e o processo começa novamente

6. É um acesso temporario

#### Instance Profile

- É uma role, um papel

- Consigo amarrar uma credencial a uma maquina virtual





