# Desafio Técnico ETL

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/emersonmcostaa/desafio_tecnico_etl/blob/main/LICENSE) 

## Sobre o projeto

Este é um desafio tecnico de ETL.

## Tecnologias utilizadas

- __Python__
- __Spark__
- __Postgres__
- __Docker__

##### Decidi usá-las pois é uma boa solução para resolução desse desafio de forma local.    
##### Docker facilita muito a solução pro banco de dados local, através de uma linha de comando é possível subir o container do nosso banco de dados, e usa pouquíssima memória.  
##### Spark é um ferramenta muito robusta e poderosa para manipulação de dados.    

## Steps do desafio:

- Leitura e transformação dos arquivos .csv da camada RAW para .parquet e carrega-los na camada TRUSTED.
- Transforamação dos arquivos .parquet da camada TRUSTED e carrega-los na camada REFINED.
- Carregamento dos dados da camada REFINED para o banco de dados postgres.
- Realizar consultas no banco

## Consultas Realizadas no Banco de dados

#### Consulta 1

#### Escreva uma query que retorna a quantidade de linhas na tabela Sales.SalesOrderDetail pelo campo SalesOrderID, desde que tenham pelo menos três linhas de detalhes.   

#### Query

```bash

SELECT
  "SalesOrderID",
  COUNT(*) AS number_of_details
FROM
  rox.sales_salesorderdetail
GROUP BY
  "SalesOrderID"
HAVING
  COUNT(*) >= 3;

```

#### Resultado da consulta 1
![postgres_consulta_1](https://github.com/emersonmcostaa/desafio_tecnico_etl/assets/99415850/0270cdca-228b-4b6e-8775-74713d8a5b38)


#### Consulta 2

#### Escreva uma query que ligue as tabelas Sales.SalesOrderDetail, Sales.SpecialOfferProduct e Production.Product e retorne os 3 produtos (Name) mais vendidos (pela soma de OrderQty), agrupados pelo número de dias para manufatura (DaysToManufacture).   

#### Query

```bash

SELECT
  production_product."Name",
  production_product."DaysToManufacture",
  SUM(rox.sales_salesorderdetail."OrderQty") AS TotalSales
FROM
  rox.sales_SalesOrderDetail
  INNER JOIN rox.sales_specialofferproduct
    ON sales_salesorderdetail."ProductID" = sales_specialofferproduct."ProductID"
  INNER JOIN rox.production_product AS production_product
    ON sales_specialofferproduct."ProductID" = production_product."ProductID"
GROUP BY
  production_product."DaysToManufacture",
  production_product."Name"
ORDER BY
  TotalSales DESC
LIMIT 3;

```

#### Resultado da consulta 2
![postgres_consulta_2](https://github.com/emersonmcostaa/desafio_tecnico_etl/assets/99415850/db2e2fc4-44b4-4933-a9cc-e91101646110)


## Como executar o projeto

Pré-requisitos:   
- Python 3.6 ou superior   
- Docker    

```bash

# clonar repositório
git clone https://github.com/emersonmcostaa/desafio_tecnico_etl

# start no banco de dados (postgres) usando o docker compose que esta na pasta `docker` desse projeto
docker-compose up -d

# Stop no banco de dados (caso necessário)
docker-compose down

# executar o arquivo `etl.py`
python etl.py

# realizar as consultas no banco de dados

- pode usar o DBeaver para realizar as consultas acima e que também estão na pasta `sql`

https://dbeaver.io/download/

```

## Autor

Emerson Monteiro da Costa
https://github.com/emersonmcostaa
https://www.linkedin.com/in/emersonmcostaa
