from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
import pandas as pd

def transform(df):
    for col_name in ["Gender", "Vehicle_Age", "Vehicle_Damage"]:
        indexer = StringIndexer(inputCol=col_name, outputCol=col_name + "_indexed")
        df = indexer.fit(df).transform(df)
        df = df.drop(col_name).withColumnRenamed(col_name + "_indexed", col_name)
    return df

def spark_etl():
    spark = SparkSession.builder.appName("InsuranceETL").getOrCreate()

    df_train = spark.read.csv("data/train.csv", header=True, inferSchema=True)
    df_test = spark.read.csv("data/test.csv", header=True, inferSchema=True)

    df_train = transform(df_train)
    df_test = transform(df_test)

    df_train.toPandas().to_csv("data/processed_train.csv", index=False)
    df_test.toPandas().to_csv("data/processed_test.csv", index=False)

    spark.stop()

if __name__ == "__main__":
    spark_etl()