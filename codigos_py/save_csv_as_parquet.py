import os

from get_spark_session import spark

def save_csv_as_parquet(directory_in:str, directory_out:str):
    """Extracts data from CSV files in a directory and saves them as Parquet files in another directory.

    Args:
        directory_in: The directory containing the CSV files.
        directory_out: The directory where the Parquet files will be saved.
    """

    print("\Processing data...")

    for filename in os.listdir(directory_in):

        f = os.path.join(directory_in, filename)

        # check if it is a file csv:
        if f.endswith('.csv'):
            name_file = filename.rsplit('.', 1)[0]

            # read csv file:
            df = spark.read.csv(f, inferSchema=True, header=True, sep=';', encoding="UTF-8")

            # save as parquet file:
            df.write.format("parquet").mode("overwrite").save(f"{directory_out}/{name_file}.parquet")
            
            print(f"{name_file} Processed successfully!")
