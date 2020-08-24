O Ateliê do Software da SME tem o objetivo de garantir a manutenção e evolução dos sistemas  em  operação e construir  sistemas  novos sob demanda, possibilitado a partir do Edital nº 33/SME/2017. Baseados  em um modelo de contratação  baseado  pelos  movimentos  ágil e de Software Craftsmanship, trabalhamos com equipes  multidisciplinares para o desenvolvimento de produtos que beneficiam  toda a comunidade escolar (técnicos da SME e DREs, gestores, professores, alunos e famílias).

Plataforma Escola Aberta

Visão do Produto

Para a **qualquer cidadã(o)** interessada(o) que queira consultar de forma intuitiva e obter em linguagem simples os dados da Rede Municipal de Educação (RME) de São Paulo o **Escola Aberta** é uma **aplicação web responsiva** que **permite a busca pelas escolas municipais a partir de seu nome ou de um dado endereço e apresenta de forma didática e atraente suas principais estatísticas** (como séries, períodos, quantidade de turmas e de estudantes, vagas oferecidas e atendidas, quantos e quais profissionais trabalham lá, que ambientes a escola possui e como está a avaliação dela no Índice de Desenvolvimento da Educação), **além de apresentar os dados gerais agregados da RME, com algumas opções de recorte** (como por Diretoria Regional de Educação). Ao contrário do **Portal de Dados Abertos ou do EOL Gerenciamento**,  o Escola Aberta **não exige um conhecimento prévio aprofundado em bases de dados ou na estruturação da RME**.

Conteúdo
1. [Sobre o Time](#sobre-o-time)  
2. [Sobre o Produto](#sobre-o-produto)  
3. [Como surgiu](#como-surgiu)  
4. [Links Úteis](#links-úteis)  
5. [Comunicação](#comunicação)  
6. [Como contribuir](#como-contribuir)  
7. [Repositórios](#repositórios)  
8. [Instalação e Configuração](#instalação-e-configuração)

 
## [](#sobre-o-time)Sobre o Time



| Papel | Titular | Suplente  
|--|--|--|  
| Product Owner | Thais Brianezi| gabinete de SME |  
| Agente de Governança | Filipe Carvalho | Fernando Gonsalez |  
| Gerente de Projeto | Aline Freitas |  |  
| Scrum Master | Marcos Nastri |  |  
| Design de Serviços | Cintia Ramos | Caio Dib |  
| Analista UX/UI | Jennifer Moreno | Luciana Baptista |  
| Analista Programador | Ollyver Otoboni | |


## [](#sobre-o-produto)Sobre o Produto

### [](#objetivos-de-negócio)Objetivos de negócio

Oferecer mecanismo de busca amigável para consulta aos dados da Rede Municipal de Educação já disponíveis no Portal Dados Abertos, com retorno das informações em linguagem simples (incluindo gráficos e mapas interativos).

### [](#personas)Personas

Cidadã(o) em geral: qualquer pessoa interessada em consultar de forma rápida e simples as escolas municipais mais próximas de sua casa ou de um dado endereço e ter acesso em linguagem simples às estatísticas não apenas dessas unidades, mas de toda a Rede Municipal de Ensino de São Paulo.

Estudantes e famílias: público já engajado na Rede Municipal de Ensino, que busca o Escola Aberta para ter dados gerais de sua escola e, também, uma visão mais ampla da Rede Municipal de Ensino – e, assim, conseguir participar mais ativamente de sua gestão democrática.

Servidores: buscam informações e dados gerenciais apresentados de forma simples e atraente a respeito  da  Rede  Municipal  de  Ensino  de  São  Paulo,  para  subsidiar  seus  trabalhos  de  análise  e  planejamento  da  política  educacional  nas  diferentes  áreas  e  escalas  (como  Educação  de  Jovens  e  Adultos  –  EJA  ou  determinada  Diretoria  Regional  de  Educação  -  DRE).

Jornalistas e demais comunicadores: consomem informações e dados sobre a Rede Municipal de Educação, para levantar pautas e subsidiar suas matérias.

Pesquisadores consomem informações e dados sobre a Rede Municipal de Educação, como subsídio para os estudos e análise da política educacional da Prefeitura de São Paulo, que contribuem com o seu constante aprimoramento.

### [](#funcionalidades)Funcionalidades

-   Busca pelas escolas municipais mais próximas de um dado endereço (logradouro).
    
-   Apresentação dos resultados da busca por endereço em mapa interativo, com georreferenciamento e dados de contato (endereço e telefone).
    
-   Apresentação (em tabelas e gráficos) dos principais números de cada escola municipal, como as séries ofertadas, períodos, quantidade de turmas e de estudantes, vagas oferecidas e atendidas, quantos e quais profissionais trabalham lá, que ambientes a escola possui e como está a avaliação dela no Índice de Desenvolvimento da Educação (IDEP).
    

-   Busca pelos dados agregados da Rede Municipal de Ensino, a partir dos seguintes filtros, que podem ser combinados: Distrito, Subprefeitura, Diretoria Regional de Ensino e tipo de unidade escolar.
    
-   Apresentação (em tabelas) das principais estatísticas da Rede Municipal de Ensino, divididas em quatro grandes categorias temáticas (escolas, Profissionais, Vagas e Matrículas e Ambientes).
    

### [](#jornadas)Jornadas

O(a) usuário(a) acessa a homepage do Escola Aberta e digita o endereço para o qual quer buscar as escolas municipais mais próximas ou o nome da unidade específica que procura. Ele(a) então terá o retorno da busca em mapa interativo, que informa também o endereço exato e dados de contato de cada unidade. A partir daí, ao clicar em estatísticas, ao lado do nome de uma determinada escola, ele(a) terá acesso à página na qual é possível consultar (em tabelas e gráficos) os principais números da escola, divididos em quatro áreas: séries e estudantes, vagas e matrículas, ambientes e Idep (quando couber).

O(a) usuário(a) acessa a homepage do Escola Aberta e seleciona no menu superior o item “Busca por Filtro”. Ele(a) então seleciona o Distrito e/ou Subprefeitura e/ou Diretoria Regional de Ensino e/ou tipo de unidade escolar que deseja consultar. Ele(a) então terá o retorno da busca em mapa interativo, que informa também o endereço exato e dados de contato de cada unidade. A partir daí, ao clicar em estatísticas, ao lado do nome de uma determinada escola, ele(a) terá acesso à página na qual é possível consultar (em tabelas e gráficos) os principais números da escola, divididos em quatro áreas: séries e estudantes, vagas e matrículas, ambientes e Idep (quando couber).

O(a) usuário(a) acessa a homepage do Escola Aberta e seleciona no menu superior o item “Conheça a Rede”. Ele(a) então terá acesso à página na qual é possível consultar as principais estatísticas da Rede Municipal de Ensino, divididas em quatro grandes categorias temáticas (escolas, Profissionais, Vagas e Matrículas e Ambientes).

### [](#roadmap)RoadMap

Release 1 -

Homepage com mecanismo de busca por endereço ou nome de unidade

Release 2 -

Busca por filtro e retorno da busca (principal e por filtro) em mapa interativo

Release 3 -

Números de cada escola apresentados em tabelas e gráficos, divididas em quatro categorias: séries e estudantes, vagas e matrículas, ambientes e Idep (quando couber).

Release 4 -

Estatísticas agregadas da Rede Municipal de Ensino apresentadas em gráficos e divididas em quatro categorias: escolas, Profissionais, Vagas e Matrículas e Ambientes.

## [](#como-surgiu)Como surgiu

Diagnóstico de que os dados da Rede Municipal de Ensino estavam disponíveis com busca pouco amigável e apresentação de difícil compreensão no EOL gerenciamento:

[http://eolgerenciamento.prefeitura.sp.gov.br/frmgerencial/NumerosCoordenadoria.aspx?Cod=000000](http://eolgerenciamento.prefeitura.sp.gov.br/frmgerencial/NumerosCoordenadoria.aspx?Cod=000000)

Benchmark:

[https://www.qedu.org.br/escola/192016-emef-luiz-david-sobrinho-prof/sobre](https://www.qedu.org.br/escola/192016-emef-luiz-david-sobrinho-prof/sobre)

Protótipos:

Home page: [https://www.figma.com/file/Pxhwd1fPmKEgZM692v7xHjV1/Escola-Aberta_MPV1?node-id=357%3A0](https://www.figma.com/file/Pxhwd1fPmKEgZM692v7xHjV1/Escola-Aberta_MPV1?node-id=357%3A0)

Resultado da busca: [https://www.figma.com/file/Pxhwd1fPmKEgZM692v7xHjV1/Escola-Aberta_MPV1?node-id=458%3A2](https://www.figma.com/file/Pxhwd1fPmKEgZM692v7xHjV1/Escola-Aberta_MPV1?node-id=458%3A2)

Estatísticas: [https://www.figma.com/file/Pxhwd1fPmKEgZM692v7xHjV1/Escola-Aberta_MPV1?node-id=652%3A1071](https://www.figma.com/file/Pxhwd1fPmKEgZM692v7xHjV1/Escola-Aberta_MPV1?node-id=652%3A1071)

## [](#links-úteis)Links Úteis

Homologação:

[https://hom-escolaaberta.sme.prefeitura.sp.gov.br/escolaaberta/](https://hom-escolaaberta.sme.prefeitura.sp.gov.br/escolaaberta/)

Produção:

[http://educacao.sme.prefeitura.sp.gov.br/escolaaberta](http://educacao.sme.prefeitura.sp.gov.br/escolaaberta)

## [](#comunicação)Comunicação

Canal de comunicação

[Telegram](https://t.me/joinchat/I_roaBNmFdyseLXVuSbBHw)

-   Alinhamento sobre produto
    
-   Comunicar novidades sobre os produtos
    
-   Movimentar a comunidade
    

-   Falar tópicos que não demandem discussões profundas
    

## [](#como-contribuir)Como contribuir

Contribuições  são super bem  vindas! Se você  tem  vontade de construir o portal da secretaria municipal e educação  conosco, veja o nosso  guia de contribuição  onde  explicamos  detalhadamente  como  trabalhamos e de que formas  você  pode  nos  ajudar  a  alcançar  nossos  objetivos. Lembrando que todos  devem  seguir  nosso  código de conduta.

## [](#repositorios)Repositórios

[SME-EscolaAberta]
[https://github.com/prefeiturasp/SME-EscolaAberta](https://github.com/prefeiturasp/SME-EscolaAberta)

[SME-EscolaAberta-API}
[https://github.com/prefeiturasp/SME-EscolaAberta-API](https://github.com/prefeiturasp/SME-EscolaAberta-API)

[SME-EscolaAberta-Front]
[https://github.com/prefeiturasp/SME-EscolaAberta-Front](https://github.com/prefeiturasp/SME-EscolaAberta-Front)

## [](#instalação-e-configuração)Instalação e Configuração

#Escola Aberta API
This is a [Docker][] setup for deploying your web application based on Django. It also contains tox file for testing your app.

## Requirements
You need to install [Docker][] and [Docker-Compose][].

## Production checklist
make sure your django app is configures for production use using this <a href='https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/'>link</a>.

## Build
`docker-compose build` or `make build`.

## Django models in database
`docker-compose run --rm djangoapp /bin/bash -c 'cd hello; ./manage.py makemigrations'`.

## Migrate database
`docker-compose run --rm djangoapp /bin/bash -c 'cd hello; ./manage.py migrate'`.

## Run
`docker-compose up` or `make run`.

## Tests
- `make checksafety`
- `make checkstyle`
- `make test`
- `make coverage`
