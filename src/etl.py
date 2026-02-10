
import logging
from pathlib import Path

from etl.etl_demo_database import etl

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

def get_logger(name, log_dir=None):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(LOG_FORMAT)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_dir is not None:
        log_path = log_dir / f"{name}.log"
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def main():
    project_dir = Path(__file__).resolve().parent.parent

    # Set up logging
    log_output = project_dir / Path("logs")
    log_output.mkdir(parents=True, exist_ok=True)
    
    # Define input and output paths
    database = project_dir / Path( r"data\input\SC_BLE_Fingerprinting\Calibration_21112023" )

    output = project_dir / Path( r"data\output\SC_BLE_Fingerprinting\Calibration_21112023" )
    output.mkdir(parents=True, exist_ok=True)
    
    # Run ETL process
    etl_logger = get_logger("etl", log_output)
    etl(database, output, logger=etl_logger)

if __name__ == "__main__":
    main()
