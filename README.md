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


 ## 17 03 25

 ### RBAC - Role Basic Access Control


 Há alguns tipos de Polices, entre elas:
 1. Polices Gerenciaveis
 2. Não gerenciaveis

 - São polices de identidade
        -- Eu vou no zezinho e falo qual permissão ele  tem

#### Há polices de recursos

- Eu quero hospedar um site estatico, o que eu faço?

1. Vou no S3 e dou um nome

2. Apesar de habilitar a hospedagem, da 403, pois ele não é publico

3. Todo balde é bloqueado por padrão em virar publico.

4. Mesmo depois de permitir ele publico, irá dar 403
- ode: AccessDenied
-Message: Access Denied

5. Tenho que criar uma Police que permite que qualquer usuario, possa pegar ou listar objetos do meu bucket. Ai eu aplico a alteração
- ARM

6. Irá funcionar

#### Police de recurso você vai no recurso e escreve um doc dizendo a permissão.

- Você não é o Deus da conta da AWS, mas você tem a permissão de criar um bucket, voce pode querer compartilhar o bucket com o colega do lado, mas você não tem permissão de ir no IAM e compartilhar. Ai você vai no bucket e compartilha, é mais granular. É possivel ser feito pelo IAM também.

### Prova de certificação
#### É necessário saber

- Na policie de recurso você tem que dizer qual usuário está dando permissão (Principal)
- Na police de identidade/usuario você não tem isso

#### Se há o "Principal", é uma police de recurso.
#### Se **NÃO** há, é police de identidade


- Colocar foto dps

### Porque a police de recurso tem que ter recurso?

- Associei a police a um bucket no S3, o balde pode ter arquivos na raiz do balde e nas "pastas", ai de forma granular eu consigo dar permissão a raiz e tudo la dentro, ou a uma pasta especifica, etc.

### IAM Policy Estrutura de documento

Uma politica IAM é um documento JSON que define permissões. Estrutura basica:

- Version: Data do formato da politica
- Statement: Lista de permissões
    - Effect: Permitir ou negar acesso
    - Action: Ações permitidas ou negadas
    - Resoruce: Recurso aos quais politica se aplica
    - Condition: Define condições especificas para a aplicação da politica
        - Exemplo: Permitir acesso apenas de um endereço IP especifico.

### Diagrama 


1. Alguém de algum jeito chamou a AWS:
    -  Console
    -  CLI
    -  SDK
    -  API REST

2. O walter pediu pra pegar um objeto do S3

3. Ele verifica: existe uma police negando do Walter de pegar o objeto?

4. Se tiver algum Deny, ele nega, mesmo que tenha uma permissão depois.

#### Outro cenario

- Somente se tiver uma permissão explicita, ele pode fazer.

- Se não tiver permissão explicita, ele vai negar tudo do mesmo jeito.

#### Evaluete - Junta todas as polices do usuario para decidir o que vai fazer

#### Efeito, ação e resurso - Os 3 obrigatorios em polices

- Ainda há o "Condition" nas polices

#### Police: doc que da permissão (quais as perms que eu te dou?)

#### Role: é alguem que pode receber uma permissão, uma identidade, tipo um usuário

Deny - NotIpAddress (foto)

## Existe 3 formas de armazenamento nas nuvens

### 1. Armazenamento por blocos:
- O HD guarda em blocos/setores
- Chamado de armazenamento blocado, ele usa uma quantidade de blocos.

-EBS (Elastic Block Storage)

- Por isso você pode editar o meio do arquivo, porque ele vai mudar só aquele bloco

### 2. File Share:
- Computador/Servidor e todo mundo se conecta nele.
- Ele resolve conflitos se varios usuarios ao mesmo tempo tentarem modificar o mesmo arquivo.
-EFS (Elastic Fire System)
-FXs

### 3. De objeto:
- Baseaso em atributos e metadados
- S3

## S3:

1. Armazenamento Massio (Ilimitado)
2. Limite de 5TB por Obj/Arq
   - Num banco por exemplo, se passar de 5tb, você fraciona e envia os arquivos.

3. Todos os objetos no S3 tem um URL **Global** e **Única**

4. Todo objeto do S3 tem uma chave do objeto ()

- s3-<regiao>.amazonaws.com/<nome-bucket>/<chave-do-objeto>

- Não existe dois baldes com o mesmo nome no mundo, pois o bucket tem um endereço unico


## Aula 20 03

- Por padrão todos os objetos do S3 não vem publicos

- Você pode criar pastas, mas as pastas não exitem

- O S3 nao trabalha com pastas, e sm com objetos, ele irá criar prefixos

- Toda vez que vc faz o upload de um arquivo, a AWS faz a copia dele em 3 AZs, dando 11 noves (99.999999999) de chance de você não perder o arquivo

- Disponibilidade é de 99,99%

- Pode ser usado alta disponibilidade para diminuir chance

- Usos do S3
-     - Sites estaticos
-     - Guardar dados financeiros/Sistemas de backup

- O balde é regional (Se foi criado no Brasil, fica só no Brasil)
-     - Podemos ter uma CDN para acelerar isso, na AWS temos a Cloudfrount

- A AWS da mecanismos para checar se os dados foram copiados, se não houve corrupção

- aws snowball

- Storage Gateway (Grava nele e manda pro S3)

- Desde janeiro de 2024 todos os arquivos dentro do S3 são criptografados
-     - Quando ele recebe ele criptografa, quando você baixa ele descriptografa e entrega pra você.

- #### Como subir arquivos

- 1. Navegador: 160GB
  2. CLI: Melhor jeito (aws s3 cp arquivoorigem s3://bucketdestino)
  3. Escrever um código em Python, dotNet para integrar e enviar
  4. API Rest
  5. Tem uma ferramenta nova, tipo explorer do Windows, bem nova
 
- Tenho um arquivo de 1TB
1. Ter um link rápido
2. Pode paralelizar ele ,fatiar em arquivos de tamanhos iguais, subo eles e digo pra AWS remontar (Multi Part Upload), tudp feito de forma automatica, aws s3 cp

#### Curiosidade:
1. Arq maiores que 100MB, indicado fazer MPU
2. Arq maiores que 5GB, é obrigado a fazer
3. 5TB tamanho máximo de objeto do S3

Drive Deep S3 resilience AWS

### S3 Transfer Acceleration

- Há um monte de saltos para chegar no datacenter da AWS, para fazer upload de um arquivo

- Posso conectar numa edge location da AWS, pode ser que em Floripa tenha uma, eu conecto nela, de floripa até SP, eu vou por um link proprietario da AWS
- Ele encurta o caminho até o destinho
- É o contrario da CDN

- - Trabalha num banco: 99% dos bancos usam FTP.
  - Por isso a AWS, criou a Transfer Family
  - Cria uma ponta na frente da AWS, conecta nele e ele manda pra AWS.

  ### S3 - A coisa MAIS importante do S3
  #### Deve ser decorado

  #### Storage Class
  - A foram como o S3 guarda a informação, vai definir:
  - 1. Preço
    2. Disponibilidade do Arquivo

    **TEM** que decorar

    Classes dividido em dois mundos
    1. Classes Quentes: Acesso imediato no objeto, subiu, baixa instantaneo
    2. Calsses Frias: Não tem acesso imediato, o objeto tem que ser recuperado ou reidratado.
 
   #### S3 Standart
    - Walter eu criei um arquivo, não confirei subi o arquivo, onde ele vai? S3 Standart
    - É o mais barato para download
    - É o **mais caro** para guardar
    - Altamente disponivel

  - Vamos dizer que o cara vai baixar muito pouco o arquivo, sera usado o:
  - ### Infrquent Access
    #### S3 Standart-IA
    - O armazenamento é mais barato
    - Mas o download é mais caro
    - Um arquivo que vou acessar menos, no maximo duas vezes no mês
   
      - Walter eu não rpeciso de 11 noves de durabilidade
      - Vou guardar um arquivo que consigo reconstruir com facilidade
      - Pode ser usado o:
    #### S3 One Zone-IA
    - Mais barato para armazenar
    - Mais caro pra baixar
    - Sem replicação, só há uma copia, não possui 11 noves de durabilidade
   
    - Modelos que não me dão acesso imediato ao objeto
    - Aqui é um modelo + barato da AWS
    ### S3 Glace Deep Archive
    - Pode levar de 12 a 48h para baixar o arquivo
    - Para guardar é muito barato
    - Mas pra baixar é muito caro

    - Não posso esperar tanto tempo pra baixar o arquivo
    ### S3 Glacier Flexible Retrieval
    - Mais caro que p deep archive
    - Mais caro pra baixar
   
    - Não posso esperar, quero clicar e baixar instantaneamente
    ### S3 Glacier Instant Retrieval
    - Não é possivel servir um cloudfrount, CDN, etc
    - O arquivo tem que ser reidratado, recupera o arquivo em ms
   
    #### Na camada fria, não é possível baixar, ele tem que ser recuperado em qualquer um dos glaciers e ir pra camada quente, um S3 standart por exemplo.

    - Se eu não sei o comportamento do arquivo, vou baixar ou não, tme:
   
    ### S3 Intelligent-Tiering
    - Se ficou X dias parados, move pro Infrequent
    - Ficou muitos dias parados, vai pro Glacier
    - Ele analisa quanto tempo
   
    #### Os arquivos do S3 são imutaveis

    ### S3 Outpots (Frio)
    - Quero levar a AWS fisicamente para minha empresa
    - Quero levar um rack de servidor para dentro da minha empresa
    - Posso pedir até 96 racks, se ultrapassar será criado uma região "só sua"
    - Eu posso rodar meu S3 dentro da empresa, mas ele perde a elastificade limitada dele
    - Quando eu peço um desse eu tenho que pedir o disco do tamanho, se precisar eu tenho que pedir mais HD/SSD
    - O Outpost tem um limite que o rack comporta
    - Esse é o rack, a AWS vem até sua empresa
    - Tem o server, que você pode pedir servidores separados.

      




