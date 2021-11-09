#### Enviar os dados para o HDFS

# No WSL2, baixe o arquivo de dados .rar dentro da pasta spark:

```shell
curl -O https://mobileapps.saude.gov.br/esus-vepi/files/unAFkcaNDeXajurGB7LChj8SgQYS2ptm/04bd3419b22b9cc5c6efac2c6528100d_HIST_PAINEL_COVIDBR_06jul2021.rar
```

# Instale o unrar para descompactar o arquivo .rar 

```shell
sudo apt install unrar
```
```shell
unrar x 04bd3419b22b9cc5c6efac2c6528100d_HIST_PAINEL_COVIDBR_06jul2021.rar
```
#Enviar os arquivos .csv para a pasta input
```shell
sudo mv *.csv /home/cicero/projeto-final-spark/spark/input
```

# Inicie todos os serviços:

```shell
docker-compose -f docker-compose-parcial.yml up -d
```

# Envie os arquivos .CSV para o HDFS
```shell
#Entre no namenode
docker exec -it namenode bash
```
```shell
#Crie a pasta projeto-final-spark no HDFS para salvar o arquivo de dados .rar
hdfs dfs -mkdir -p /user/cicero/projeto-final-spark
```
```shell
#Envie o arquivo de dados .rar para a pasta projeto-final-spark no HDFS
hdfs dfs -put /input/*.csv /user/cicero/projeto-final-spark
```
```shell
#Confirme se o arquivo foi enviado
hdfs dfs -ls /user/cicero/projeto-final-spark
```

------

#### Otimizar todos os dados do hdfs para uma tabela Hive particionada por município

#Acesse o jupyter-notebook pelo navegador e abra um arquivo PySpark e renomeie para projeto-final-spark
http://localhost:8889/

# Acesse os arquivos .CSV pelo HDFS
!hdfs dfs -ls "hdfs:///user/cicero/projeto-final-spark/"


#Importe as bibliotecas necessárias
from pyspark.sql import *
from pyspark.sql.types import *

#Acesse os arquivos pelo HDFS
!hdfs dfs -ls "hdfs:///user/cicero/projeto-final-spark/"

#Acessar os arquivos e mostrar a primeira linha 
rdd = sc.textFile("hdfs:///user/cicero/projeto-final-spark/")
rdd.first()

#Mostrar as primieras linhas para entender os dados
rdd.take(200)

'''
#Criar um Data Frame com Schema organizado.
colunas_painel_covidbr = [ StructField("regiao", StringType()),
                          StructField("estado", StringType()),
                          StructField("municipio", StringType()),
                          StructField("coduf", StringType()),
                          StructField("codmun", StringType()),
                          StructField("codRegiaoSaude", StringType()),
                          StructField("nomeRegiaoSaude", StringType()),
                          StructField("data", DateType()),
                          StructField("semanaEpi", StringType()),
                          StructField("populacaoTCU2019", IntegerType()),
                          StructField("casosAcumulado", IntegerType()),
                          StructField("casosNovos", IntegerType()),
                          StructField("obitosAcumulado", IntegerType()),
                          StructField("obitosNovos", IntegerType()),
                          StructField("Recuperadosnovos", IntegerType()),
                          StructField("emAcompanhamentoNovos", IntegerType()),
                          StructField("interior/metropolitana", IntegerType())]

schema = StructType(colunas_painel_covidbr)
df_painel_covidbr = spark.read.option("header","true").option("delimiter",";").csv("hdfs:///user/cicero/projeto-final-spark/")
'''

#Utilizando o option("inferSchema","true") para que automaticamente o spark identifique os tipos de dados das colunas
df_painel_covidbr = spark.read.option("sep",";").option("header","true").option("inferSchema","true").csv("hdfs:///user/cicero/projeto-final-spark/")

#Visualize o schema
df_painel_covidbr.printSchema()
df_painel_covidbr.head()

df_painel_covidbr.show(5, vertical=True)

#Inserindo os dados no Apache Hive

#Separando os dados por municípios


------

#### Criar as 3 visualizações pelo Spark com os dados enviados para o HDFS 


------

#### Salvar a primeira visualização como tabela Hive


------

#### Salvar a segunda visualização com formato parquet e compressão snappy


------

#### Salvar a terceira visualização em um tópico no Kafka


------

#### Criar a visualização pelo Spark com os dados enviados para o HDFS

'''
Fontes de ajuda:

Spark Read CSV file into DataFrame: https://sparkbyexamples.com/spark/spark-read-csv-file-into-dataframe/


'''