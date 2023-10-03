import os

# Definindo a variável de ambiente do Java
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
# Definindo a variável de ambiente do Spark
os.environ["SPARK_HOME"] = "/home/emerson/spark-3.1.2-bin-hadoop2.7"
#importando a findspark
import findspark
# iniciando o findspark
findspark.init()
# importando o pacote necessário
from pyspark.sql import SparkSession

# iniciando o spark context
spark = SparkSession.builder.master('local[*]').getOrCreate()
