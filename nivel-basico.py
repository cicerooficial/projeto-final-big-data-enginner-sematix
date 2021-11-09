# Enviar os dados para o HDFS

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

# Envie os arquivos para o DFS
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

#Acesse o jupyter-notebook

```shell
http://localhost:8889/
```

#Abra um arquivo PySpark chamado projeto-final-spark

# Acesse os arquivos .CSV pelo HDFS
!hdfs dfs -ls "hdfs:///user/cicero/projeto-final-spark/"






------

# Criar as 3 visualizações pelo Spark com os dados enviados para o HDFS 


------

# Salvar a primeira visualização como tabela Hive


------

# Salvar a segunda visualização com formato parquet e compressão snappy


------

# Salvar a terceira visualização em um tópico no Kafka


------

# Criar a visualização pelo Spark com os dados enviados para o HDFS

