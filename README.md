<img align="center" src="./logo-semantix.png" alt="Logo Semantix Inc." style="zoom:100%;" />

# Projeto Final Spark: Big Data Enginner

<p align="center">
    <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
    <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
    <img src="https://img.shields.io/badge/Hadoop-FFFFFF?style=for-the-badge&logo=hadoop&logoColor=#E35A16"/>
    <img src="https://img.shields.io/badge/Apache_Spark-FFFFFF?style=for-the-badge&logo=apachespark&logoColor=#E35A16"/>
	<img src="https://img.shields.io/badge/Elastic_Search-005571?style=for-the-badge&logo=elasticsearch&logoColor=white"/>
</p>

- Nome: Cícero Henrique dos Santos
- Instituição: Semantix Academy
- Turma: Big Data Engineer 08-21
- Professor: Rodrigo Rebouças

## Tópicos 

- [Pré-requisitos](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#pr%C3%A9-requisitos)
- [Descrição do projeto](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#descri%C3%A7%C3%A3o-do-projeto)
- [Configurando o Docker em sua máquina]()
- [Preparando o ambiente](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#preparando-o-ambiente)
- [Nível básico](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#n%C3%ADvel-b%C3%A1sico)
  - [Objetivos](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#objetivos)
  - [Projeto Final Spark - Nivel básico](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#-projeto-final--spark---nivel-b%C3%A1sico)
- [Nível avançado](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#n%C3%ADvel-avan%C3%A7ado)
  - [Objetivo](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#objetivo)
  - [Passo a passo](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix#-passo-a-passo-1)

------

## Pré-requisitos

Para melhor compreensão e execução do projeto é necessário conhecimentos básicos (fundamentos) em: Big Data, Docker, Python, Kafka, Elastic e Spark. 

------

## Descrição do projeto

Esse projeto tem como objetivo desenvolver os conhecimentos adquiridos durante o treinamento de [Big Data Enginner](https://github.com/cicerooficial/big-data-engineer-sematix) promovido pela Semantix Inc no segundo semestre de 2021. 

O projeto é dividido em duas partes (básico e avançado) sobre o tema Campanha Nacional de Vacinação contra Covid-19.

⚠ **Observação: Todas as imagens de exemplo abaixo (Visualizações) são apenas para referencias, o projeto irá ter valores diferentes e as formas de se criar tabelas com dataframe/dataset das visualizações, pode ser realizado da maneira que preferir.**

------
## Configurando o Docker em sua máquina:

A fim de facilitar o desenvolvimento das etapas do projeto, abaixo segue um passo a passo de preparação de ambiente.

### Download Docker e Docker Compose:

### Download Docker - Windows

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Instalação Docker - Windows

1. Verificar se o Windows está atualizado. Caso seja inferiro a 18362, clique no link ao lado para atualizar o Windows 10. [Atualizar o Windows](https://www.microsoft.com/pt-br/software-download/windows10);
2. Pesquise por Ativar ou desativar recursos do Windows e siga os passos abaixo:
    - Desativar Hyper-V;
    - Desativar Plataforma do Hipervisor do Windows;
    - Habilitar a Plataforma de Máquina Virtual;
    - Habilitar o Subsistema do Windows para Linux (WSL).
3. Faça o Download do WSL 2 clicando no link ao lado: [Download WSL 2](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi);
4. Acesse a Microsoft Store, e faça download e instale a distribuição Linux Ubuntu 20.04 LTS (recomendado);
5. Instale o Docker Desktop no Windows: [Docker Desktop](https://hub.docker.com/editions/community/docker-ce-desktop-windows);
    - Obs: Abra o Docker Desktop e verifique se estão habilitados o "Enable integration with my default WSL distro" e "Ubuntu-20.04" em Settings->Resource->WSL Integration.

### Instalação Docker - Linux

- [Link para instalação do Docker Engine](https://docs.docker.com/engine/install/)
- [Link para instalação do Docker Compose](https://docs.docker.com/compose/install/)

### Instalação Docker - Mac
- [Link para instalação do Docker Desktop no Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)

----------

## Preparando o ambiente:

1. Abra o terminal do WSL2 e crie um diretório para o projeto no `~$/home/<seu-nome>` com o comando: `mkdir projeto-final-spark`
2. Acesse o diretório `cd projeto-final-spark`
3. No diretório projeto-final-spark, clone o cluster disponibilizado no treinamento: `git clone https://github.com/rodrigo-reboucas/docker-bigdata.git spark`
4. Confirme se o arquivo foi baixado com o comando de listar: `ls`
5. Entra na pasta spark `cd spark`
6. Configure o vm.max_map_count para 262144:
    1. Digite o comando `sudo nano /etc/sysctl.conf`
    2. Vá até o final do arquivo e incluia o parâmetro `vm.max_map_count=262144` 
    3. CTRL+O para salvar e CTRL+X para sair
    4. Verifique se funcionou utilizando o comando `grep vm.max_map_count /etc/sysctl.conf` no terminal.
Obs.: Sempre que iniciar o cluster, deve-se utilizar o comando `sudo sysctl -w vm.max_map_count=262144` para que os containers sejam ativos.
7. baixe as imagens com o comando `docker-compose -f docker-compose-parcial.yml pull`
8. Verifique se as imagens foram baixadas através do comando de listar `docker image ls`
9. Inicie todos os serviços com o comando: `docker-compose -f docker-compose-parcial.yml up -d`
Obs.: Cuidado para não iniciar o cluster completo (docker-compose-completo.yml), pois dependendo das congifurações da sua máquina, ficará pesado para executar.
10. Por fim, será necessário configurar que as tabelas Hive aceitem o formato parquet. 
    1. Faça downlod do arquivo .jar com o comando `curl -O https://repo1.maven.org/maven2/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.jar`
    2. Copie o arquivo para o diretório `/opt/spark/jars` com o comando `docker cp parquet-hadoop-bundle-1.6.0.jar jupyter-spark:/opt/spark/jars`

Agora sua máquina está configurada e seus arquivos estão prontos para serem utilizados no HDFS.
Continue os próximos passos pelo Jupyter-Notebook acessando pelo navegador a porta `http://localhost:8889/`. 
Depois crie um arquivo de tipo PySpark chamado projeto_final_spark_nivel_basico. Neste arquivo continuaremos com os próximos passos utilizando PySpark.

----------

## Nível básico

- Dados: https://mobileapps.saude.gov.br/esus-vepi/files/unAFkcaNDeXajurGB7LChj8SgQYS2ptm/04bd3419b22b9cc5c6efac2c6528100d_HIST_PAINEL_COVIDBR_06jul2021.rar
- Referência das Visualizações:
  - Site: https://covid.saude.gov.br/
  - Guia do Site: **Painel Geral**

### Objetivos

- ✅Enviar os dados para o HDFS
- ✅Otimizar todos os dados do HDFS para uma tabela Hive particionada por município
- ✅Criar as 3 visualizações pelo Spark com os dados enviados para o HDFS 
- ✅Salvar a primeira visualização como tabela Hive
- ✅Salvar a segunda visualização com formato parquet e compressão snappy
- ✅Salvar a terceira visualização em um tópico no Kafka
- ✅Criar a visualização pelo Spark com os dados enviados para o HDFS
- ⬜Salvar a visualização do exercício 6 em um tópico no Elastic
- ⬜Criar um dashboard no Elastic para visualização dos novos dados enviados

### ▶ [Projeto Final  Spark - Nivel básico](https://github.com/cicerooficial/projeto-final-big-data-enginner-sematix/blob/main/projeto_final_spark_nivel_basico.ipynb)

----------

## Nível avançado

- Link oficial para todas as informações: https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao
- Informações para se conectar ao cluster: 
  - URL https://imunizacao-es.saude.gov.br/desc-imunizacao
  - Nome do índice: desc-imunizacao
  - Credenciais de acesso o Usuário: imunizacao_public 
  - Senha: qlto5t&7r_@+#Tlstigi
  - Links utéis para a resolução do problema:
    - Consumo do API:
      https://opendatasus.saude.gov.br/dataset/b772ee55-07cd-44d8-958f-b12edd004e0b/resource/5916b3a4-81e7-4ad5-adb6-b884ff198dc1/download/manual_api_vacina_covid-19.pdf
    - Conexão do Spark com Elastic:
      https://www.elastic.co/guide/en/elasticsearch/hadoop/current/spark.html
      https://docs.databricks.com/data/data-sources/elasticsearch.html#elasticsearch-notebook
      https://github.com/elastic/elasticsearch-hadoop
      https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration.html
    - Instalar Dependências:
      https://www.elastic.co/guide/en/elasticsearch/hadoop/current/install.html

### Objetivo

- ⬜Replicar as visualizações do site https://covid.saude.gov.br/, porém acessando diretamente a API de Elastic.

### ▶ [Projeto Final Spark - Nivel Avançado]()





