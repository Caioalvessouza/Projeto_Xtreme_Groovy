## Xtreme Groovy Bikes Sales - Análise de Dados

A Xtreme Groovy Bikes Sales é uma empresa de revenda de motocicletas. Seu modelo de nogócio é revender motocicletas usadas. Com a crescente do valor dos veículos usados, a XGB Sales, como é conhecida, deseja expandir os seus negócios. Você foi contratado como cientista de dados pela empresa XGB Sales para ajudá-los a encontrar as melhores motocicletas para revenda. 

Para isso, o CEO da empresa fez um estudo de mercado lhe entregou uma base de dados, obtida através desse estudo, para que você consiga auxiliá-lo a encontrar as melhores motocicletas para revenda, aumentando assim o lucro da empresa.

Abaixo, encontram-se as principais perguntas que norteiam essa análise:

### Quantidade de Motos:

Quantas motos temos dentro do Dataset?

###  Ano das Motos:

Qual é o ano da moto mais antiga da base de dados?
Qual é o ano da moto mais nova da base de dados?

### Valores e Quilometragem:

Qual é o valor da moto mais cara da base de dados?
Qual é o valor do hodômetro da moto com a maior quilometragem?
Qual é o valor do hodômetro da moto com a menor quilometragem?

### Show Room:

Das motocicletas expostas em um Show Room, qual é o maior e o menor valor registrado na base de dados?

### Vendas por Donos e Revendedores:

Quantas motocicletas estão sendo vendidas pelos seus donos e quantas estão sendo vendidas por outros revendedores?

### Médias Gerais:

Qual é a média de valores das motos na base de dados?
Qual é a média de ano das motos cadastradas na base de dados?
Qual é a média de quilometragem das motos cadastradas na base de dados?

### Propriedade Única e Quilometragem:

Existem quantas motos na base de dados que são de um único dono?
As motos com menor quilometragem são as mais baratas no conjunto de dados?
As motos de um único dono são mais caras em média do que as motos com mais donos?

### Relações entre Propriedade e Características:

Motos com mais donos possuem quilometragem média maior que as motos com menos donos?
Motos com mais donos são mais velhas em média?

### Vendas por Revendedores:

Motos vendidas por revendedores são mais caras em média do que as vendidas pelos seus donos?

### Novo Dataset e Fabricantes:

Adicione uma coluna no DataFrame com o nome de "company" (fabricante).
Crie um novo dataset chamado "bikes_completed.csv" com a coluna "company" preenchida.

### Fabricantes mais Prolíficos:

Quais são os fabricantes que mais possuem motos cadastradas na base de dados completa?

Essas perguntas visam fornecer insights cruciais para a Xtreme Groovy Bikes Sales, ajudando a orientar suas estratégias de aquisição e venda de motocicletas usadas. A análise abrange desde aspectos financeiros até características específicas relacionadas aos veículos, proporcionando uma visão abrangente para otimizar os negócios da empresa.

## Dados
Os dados fornecidos incluem informações cruciais sobre as motocicletas disponíveis, como fabricante, modelo, preço de venda, ano de fabricação, tipo de vendedor, histórico de proprietários, quilometragem percorrida, entre outros.

## Análise do Código

O código disponibilizado utiliza a biblioteca Streamlit para criar uma interface interativa de análise de dados. Ele carrega o conjunto de dados e fornece respostas para questões importantes relacionadas às motocicletas disponíveis para revenda.

## Funções Principais

### load_data(csv_path):

 Carrega o conjunto de dados a partir do caminho fornecido.

### create_dataframe_section(df):
 Apresenta informações sobre o banco de dados, incluindo uma visualização das primeiras linhas e uma descrição das colunas.

### create_answers_section(df): 

Fornece respostas para perguntas essenciais sobre as motocicletas no conjunto de dados.

## Execução do Código

Para explorar as respostas e visualizações interativas, basta executar o script principal. Ele carregará os dados do arquivo "bikes_completed.csv" e facilitará a análise das melhores oportunidades de motocicletas para revenda.

[Link para o Dashboard](https://projetoxtremegroovy.streamlit.app/)


