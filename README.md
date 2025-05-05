# Design e Arquitetura de Software II

[AWS Canvas](https://awsacademy.instructure.com/courses/113113)

## Repositório dos alunos
- [Repos](https://gist.github.com/901f02fd5f852b62abab10b5fb2d6328.git)

## Aula 24/02
- Well-Architect Framework
  - Excelencia operacional
  - Segurança
  - Confiabilidade (Reliabillity)
  - Eficiência em performance
  - Otimização de custos
  - Sustentabilidade

## Aula 27/02
- Trade-Offs
  - Escalabilidade/Elasticidade
  - Automatização auto escalabilidade
  - Infraestrutura como Código
  - Tratar os recursos como descartaveis
  - Baixo acoplamento
  - Design de serviços e não servidores
  - Escolha o banco de dados correto

## Aula 06/03
- Trade-Offs
  - Evitar ponto único de falha
  - Otimização de custo
  - Use de cache
  - Proteger sua infraestrutura
- Infraestrutura global da AWS
  - Regiões
  - Zonas de Disponibilidade
  - Local Zones
  - Data Centers

## Aula 10/03
- Infraestrutura global da AWS
  - POPs - Edge Location
- Segurança
  - Modelo de responsabilidade compartilhado
  - Autenticação
  - Autorização
  - Princípio do privilégio mínimo
  - Criptografia

## Aula 13/03
- Modelo de responsabilidade compartilhada
- Princípio do privilégio mínimo
- Autenticação
- Autorização
- Identity and Access Management
- Usuários
- Acesso pela console / acesso programático

## Aula 17/03
- Policy de Identidade
- Policy de Recurso
- S3

## Aula 24/03
- S3 - Gerenciamento de ciclo de vida
- S3 - Versionamento
- S3 - CORS

```bash
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "http://127.0.0.1:5500"
        ],
        "ExposeHeaders": [
            "x-amz-server-side-encryption",
            "x-amz-request-id",
            "x-amz-id-2"
        ],
        "MaxAgeSeconds": 3000
    }
]
```

## Aula 27/03
- Códigos S3

## Aula 31/03
- Códigos S3

## Aula 03/04
- Computing (EC2)
- EBS
- AMI

## Aula 07/04
- Placement (Cluster/Spread/Partition)
- EC2 Purchase model (on-demand/reserved/savings plans/spot)

## Aula 10/04
- RDS
- Bancos de dados relacionais
- Bancos de dados não relacionais


## Aula 05/05

- Amazon VPC (Virtual Private Cloud)

Como definir uma rede, sem tocar na rede?

Usamos Software Defined Network -> SDN


### Introdução ao Amazon VPC

O Amazon Virtual Private Cloud (VPC) permite que você provisione uma seção isolada da nuvem AWS onde pode lançar recursos da AWS em uma rede virtual que você define. Ele oferece controle total sobre o ambiente de rede, incluindo seleção de intervalos de IP, criação de sub-redes e configuração de tabelas de roteamento e gateways de rede.

#### Componentes Principais do VPC

1. **Sub-redes:**
  - Dividem o VPC em segmentos menores.
  - Podem ser públicas (acessíveis pela internet) ou privadas (restritas a uma rede interna).

2. **Internet Gateway (IGW):**
  - Permite que instâncias em sub-redes públicas se comuniquem com a internet.

3. **NAT Gateway:**
  - Permite que instâncias em sub-redes privadas acessem a internet sem serem diretamente acessíveis.

4. **Tabelas de Roteamento:**
  - Definem como o tráfego é roteado dentro do VPC e para fora dele.

5. **Security Groups e Network ACLs:**
  - Controlam o tráfego de entrada e saída para instâncias e sub-redes.

#### Benefícios do Amazon VPC

- **Isolamento:** Recursos são isolados em uma rede virtual privada.
- **Segurança:** Controle granular sobre o tráfego de rede.
- **Flexibilidade:** Personalização de configurações de rede para atender às necessidades específicas.
- **Conectividade Híbrida:** Integração com redes locais usando VPN ou AWS Direct Connect.

#### Casos de Uso

- Hospedagem de aplicativos web em sub-redes públicas com bancos de dados em sub-redes privadas.
- Configuração de ambientes híbridos conectando redes locais ao VPC.
- Implementação de arquiteturas de microserviços com controle de tráfego entre serviços.

#### Boas Práticas

- Use múltiplas zonas de disponibilidade (AZs) para alta disponibilidade.
- Configure sub-redes privadas para recursos sensíveis.
- Habilite logs do VPC Flow para monitorar o tráfego de rede.
- Utilize Security Groups e Network ACLs para reforçar a segurança.


1. Primeiro nivel de isolamento: Conta
2. Segundo nivel: VPC
- Dentro da AWS temos as regiões.
- No Brasil temos SA-east-1
- No EUA us-east-1
Ou seja, o que está dentro de uma região, não conversa com outra região, a não ser que você queira.
Uma região é composta por varias AZs.
Tudo que está dentro de uma região é interconectado.
Uma AZ pode estar até 100 milhas de distância.

Há limite de datacenters por AZ?
Não temos como saber.

Uma AZ pode ter pelo menos 1 datacenter.
Uma região tem varias AZs, e em cada AZ pelo menos 1 datacenter.

Dica prova de certificação AWS:
Toda vez que você cria uma rede, ela fica dentro de uma região.
Cria uma rede pro servidor de minecraft no Brasil.
Agora quero pegar esse servidor e rodar no EUA, tenho que criar outra rede.
Elas não se comunicam a não ser que voc~e queira.

Uma VPC se espalha para dentro de uma região.
Se uma região tiver varios data centers e espalhados, a VPC se comunica entre todos eles, pos estão na mesma VPC.

### Amazon VPC:
1. Rede definida por software
2. Logicamente Isolada
3. Voocê customiza o trafego, quem fala com quem.
4. Tem que definir o tamanho da sua rede por CIDR

IPV4 formado por 4 octais
Cada octeto vai de 0-255
Representado por 2^8? confirmar

cidr.xyz

10.0.0.0/16

255.255.0.0

Endereço da Rede / Endereço do Host

![](image.png)

Gerenciar tantos IPs é dificil, por isso segregamos a rede, comummente chamados de VLAN.

Na AWS isso é chamado de Subnet.
Ela é semelhante a VPC, mas um pouco diferente.
Ela é um pedacinho da VPC.
A subnet tem que estar contida na VPC.

o CIDR da subnet não pode bater no CIDR de outra subnet.
Ex: Não pode ter duas subnet com 10.1.128.0/24.


No Unifi por exemplo, tenho isolamento de cliente, mesmo se o cliente está conectado na mesma SSID, ele não se consegue comunicar com outro.

Na AWS é usado a **Tabela de rotas**.


A tabela de rotas da AWS (Route Table) é um componente fundamental dentro de uma VPC (Virtual Private Cloud). Ela define como o tráfego de rede é direcionado dentro da VPC e para fora dela.

### Conceitos principais

- **Associação com Subnets:** Cada subnet em uma VPC está associada a uma tabela de rotas. Isso determina como o tráfego de saída da subnet será roteado.
- **Rotas:** Cada entrada na tabela especifica um destino (CIDR) e um alvo (target), como um gateway de internet, NAT, ou outra interface de rede.

### Funcionamento

- Quando um pacote sai de uma instância, a AWS verifica a tabela de rotas associada à subnet para decidir para onde enviar o pacote.
- Exemplo de rotas comuns:
  - `10.0.0.0/16` → local (tráfego interno da VPC)
  - `0.0.0.0/0` → igw-xxxxxxx (Internet Gateway, para acesso à internet)
  - `0.0.0.0/0` → nat-xxxxxxx (NAT Gateway, para acesso à internet privado)

### Resumindo

A tabela de rotas controla para onde vai o tráfego de rede de cada subnet. Ela é essencial para isolar, conectar ou expor recursos na AWS.

Se quiser um exemplo prático de configuração, posso mostrar!

A AWS dá um IP para uma aplicação e reserva ela com através do MAC Address.

Subnet vivem dentro de um datacenter.
Quando criamos uma subnet, dizemos que essa maquina fica nesse lugar do mundo.

### Public subnet
Na imagem há duas cores, um azul claro e verde claro.
Na AWS há dois tipos de subnets.
1. Publica:
- Subnet onde os recursos onde estão dentro dela estão visiveis na internet publica, de dentro pra fora e de fora pra dentro.
Acesso ela de fora da rede.
E ela acessa a internet de fora pra dentro.

Para eu transformar uma subnet em pública, eu preciso de um **Internet Gateway** associado a sua VPC.

Depois, você precisa, na **Tabela de Rotas** vigente para sua subnet, adicionar uma regra de saída apontando para o **Internet Gateway**. Isso garante que o tráfego destinado à internet seja roteado corretamente para fora da VPC.

Exemplo de rota para tornar a subnet pública:

| Destino      | Target         |
|--------------|---------------|
| 0.0.0.0/0    | igw-xxxxxxxx   |

- **0.0.0.0/0**: representa todo o tráfego externo (internet).
- **igw-xxxxxxxx**: é o identificador do seu Internet Gateway.

Sem essa configuração, mesmo com o Internet Gateway associado à VPC, as instâncias na subnet não terão acesso à internet.

E a máquina precisa te rum IP Público associado.

**Internet Gateway** faz um NAT

Eu posso associar um IP publico a máquina, mas a máquina só enxerga o IP Privado, pois quem gerencia o publico é a **Internet Gateway**.



2. Privada:

