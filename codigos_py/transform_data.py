import os

from get_spark_session import spark

import pyspark.sql.functions as f


def transform_data(directory_in:str, directory_out:str):
    """Transforms data in Parquet files in a directory by dropping all rows with any NaN values.

    Args:
        directory_in: The directory containing the Parquet files.
        directory_out: The directory where the transformed Parquet files will be saved.
    """

    print(f"\nTransforming data...")

    for filename in os.listdir(directory_in):
        name_file = filename.rsplit('.', 1)[0]

        # read parquet file:
        df = spark.read.parquet(f"{directory_in}{filename}", inferSchema=True)

        # drop rows with any NaN values:
        df = df.dropna(how="all")

        # Clean extra spaces in string columns:
        for column in df.columns:
            if df.select(column).dtypes[0][1] == 'string':
                df = df.withColumn(column, f.trim(f.col(column)))
        
        # Replace empty strings by null values:
        df = df.replace('', None)

        # save transformed data as parquet files:
        df.write.format("parquet").mode("overwrite").save(f"{directory_out}/{name_file}.parquet")

        print(f"{name_file} transformed successfully!")
