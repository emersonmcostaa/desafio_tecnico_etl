from load_data import load_data
from save_csv_as_parquet import save_csv_as_parquet
from transform_data import transform_data


def etl_process():
    """Executes the ETL process."""
    
    path_raw = "/home/emerson/rox/raw/"
    path_trusted = "/home/emerson/rox/trusted/"
    path_refined = "/home/emerson/rox/refined"

    save_csv_as_parquet(path_raw, path_trusted)
    transform_data(path_trusted, path_refined)
    load_data(path_trusted)


if __name__ == "__main__":
    etl_process()
