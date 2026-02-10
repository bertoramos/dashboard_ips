
import re
import pandas as pd

def read_txt(path):
    content = pd.read_csv(path, sep=";", header=None, names=["timestamp", "beacon", "channel", "rssi"])
    return path.stem, content

def transform_database(filename, content):
    x = re.search(r"x_([+-]?\d+)", filename).group(1)
    y = re.search(r"y_([+-]?\d+)", filename).group(1)

    content["x"] = int(x)
    content["y"] = int(y)

    content["protocol"] = "UNKNOWN"

    content = content[["timestamp", "x", "y", "beacon", "protocol", "channel", "rssi"]]

    return content

def etl(input_path, output_path, logger=None):
    
    df_parts = []
    
    for txt_file in input_path.glob("*.txt"):
        
        filename, content = read_txt(txt_file)
        transformed_data = transform_database(filename, content)
        df_parts.append(transformed_data)
    
    df = pd.concat(df_parts, ignore_index=True)
    output_file = output_path / (input_path.name + ".csv")

    df.to_csv(output_file, index=False)
    if logger is not None:
        logger.info("Data written to %s", output_file)
