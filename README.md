# <img align="center" src="https://semantix.com.br/wp-content/uploads/2021/03/smtx-logo-white.png" alt="Logo Semantix Inc." style="zoom:100%;" />

# Projeto Final Spark: Big Data Enginner

- Nome: Cícero Henrique dos Santos
- Instituição: Semantix Academy
- Turma: Big Data Engineer 08-21
- Professor: Rodrigo Rebouças

<p align="center">
    <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
    <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
    <img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white" />
    <img src="https://img.shields.io/badge/Elastic_Search-005571?style=for-the-badge&logo=elasticsearch&logoColor=white">
    <img src="https://img.shields.io/badge/Apache_Spark-FFFFFF?style=for-the-badge&logo=apachespark&logoColor=#E35A16">
</p>

## Tópicos 

- [Pré-requisitos](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#pr%C3%A9-requisitos)
- [Descrição do projeto](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#descri%C3%A7%C3%A3o-do-projeto)
- [Preparando o ambiente](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#preparando-o-ambiente)
- [Nível básico](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#n%C3%ADvel-b%C3%A1sico)
  - [Objetivos](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#objetivos)
  - [Passo a passo](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#-passo-a-passo)
- [Nível avançado](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#n%C3%ADvel-avan%C3%A7ado)
  - [Objetivo](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#objetivo)
  - [Passo a passo](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#-passo-a-passo-1)

------

## Pré-requisitos

Para melhor compreensão e execução do projeto é necessário conhecimentos básicos (fundamentos) em: Big Data, Docker, Python, Kafka, Elastic e Spark. 

------

## Descrição do projeto

Esse projeto tem como objetivo promover os conhecimentos adquiridos durante o treinamento de [Big Data Enginner](https://github.com/cicerooficial/big-data-engineer-sematix) promovido pela Semantix Inc no segundo semestre de 2021. 

O projeto é dividido em duas partes (básico e avançado) sobre o tema Campanha Nacional de Vacinação contra Covid-19.

⚠**Observação: Todas as imagens de exemplo abaixo (Visualizações) são apenas para referencias, o projeto irá ter valores diferentes e as formas de se criar tabelas com dataframe/dataset das visualizações, pode ser realizado da maneira que preferir.**

------

## Nível básico

- Dados: https://mobileapps.saude.gov.br/esus-vepi/files/unAFkcaNDeXajurGB7LChj8SgQYS2ptm/04bd3419b22b9cc5c6efac2c6528100d_HIST_PAINEL_COVIDBR_06jul2021.rar
- Referência das Visualizações:
  - Site: https://covid.saude.gov.br/
  - Guia do Site: **Painel Geral**

### Objetivos

- ✅Preparando o ambiente
- ✅Enviar os dados para o HDFS
- ⬜Otimizar todos os dados do HDFS para uma tabela Hive particionada por município
- ⬜Criar as 3 visualizações pelo Spark com os dados enviados para o HDFS 
- ⬜Salvar a primeira visualização como tabela Hive
- ⬜Salvar a segunda visualização com formato parquet e compressão snappy
- ⬜Salvar a terceira visualização em um tópico no Kafka
- ⬜Criar a visualização pelo Spark com os dados enviados para o HDFS

### ▶ [Acesse aqui o Projeto Final  Spark - Nivel básico](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix/blob/main/projeto_final_spark_nivel_basico.ipynb)


------

## Nível avançado

- Link oficial para todas as informações: `https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao`
- Informações para se conectar ao cluster: 
  - URL https://imunizacao-es.saude.gov.br/desc-imunizacao
  - Nome do índice: desc-imunizacao
  - Credenciais de acesso o Usuário: imunizacao_public 
  - Senha: qlto5t&7r_@+#Tlstigi
  - Links utéis para a resolução do problema:
    - Consumo do API:
      https://opendatasus.saude.gov.br/dataset/b772ee55-07cd-44d8-958f-b12edd004e0b/resource/5916b3a4-81e7-4ad5-adb6-b884ff198dc1/download/manual_api_vacina_covid-19.pdf'
    - Conexão do Spark com Elastic:
      https://www.elastic.co/guide/en/elasticsearch/hadoop/current/spark.html
      https://docs.databricks.com/data/data-sources/elasticsearch.html#elasticsearch-notebook
      https://github.com/elastic/elasticsearch-hadoop
      https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration.html
    - Instalar Dependências:
      https://www.elastic.co/guide/en/elasticsearch/hadoop/current/install.html

### Objetivo

- ⬜Replicar as visualizações do site https://covid.saude.gov.br/, porém acessando diretamente a API de Elastic.

### ▶ [Passo a passo]()





