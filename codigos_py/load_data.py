import os

from get_spark_session import spark


def load_data(directory_in:str):
    """Loads data from Parquet files in a directory into PostgreSQL tables.

    Args:
        directory_in: The directory containing the Parquet files.
    """

    print("\nloading data...")

    for filename in os.listdir(directory_in):

        name_file = filename.rsplit('.', 1)[0]
        table_name = name_file.replace('.', '_')

        # read parquet file:
        df = spark.read.parquet(f"{directory_in}{filename}", inferSchema=True)

        # save as table in PostgreSQL:
        (
            df.write
            .mode('Overwrite')
            .format("jdbc")
            .options(
                url="jdbc:postgresql://localhost:5432/postgres", 
                user="postgres",
                password="1234", driver="org.postgresql.Driver", 
                dbtable=f"rox.{table_name}"
            )
            .save()
        )

        print(f'{table_name} Loaded successfully!')
