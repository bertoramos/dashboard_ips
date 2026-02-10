
import sqlite3
import pandas as pd


def read_database(input_db, logger=None):
    try:
        conn = sqlite3.connect(input_db)
        query = """
            SELECT
                b.Id AS Beacon_Id,
                b.Id_capture,
                b.N_reading,
                b.Date_hour,
                b.Mac,
                b.Pack_size,
                b.Channel,
                b.RSSI,
                b.PDU_type,
                b.CRC,
                b.Protocol,
                b.Identificator,

                c.Date,
                c.Light,
                c.Temperature,
                c.Relative_humidity,
                c.Absolute_humidity,
                c.Position_x,
                c.Position_y,
                c.Position_z,
                c.Platform_angle,
                c.Dongle_rotation
            FROM Beacon_BLE_Signal b
            JOIN Capture c
                ON b.Id_capture = c.Id;

            """

        df = pd.read_sql(query, conn)
        conn.close()
    except Exception as e:
        if logger is not None:
            logger.error("Error reading database: %s", e)
        raise e

    if logger is not None:
        logger.info("Data read from database: %d rows", len(df))

    return df


def transform_data(df, logger=None):
    # Convertir timestamp a formato datetime
    df["Date_hour"] = pd.to_datetime(df["Date_hour"], errors="coerce")

    # Rellenar valores faltantes con NaN
    df.replace({None: pd.NA}, inplace=True)

    if logger is not None:
        logger.info(
            "Data transformed: timestamp converted, missing values handled")

    return df


def etl(input_db, output_csv, logger=None):
    dataframe = read_database(input_db, logger=logger)
    transformed_df = transform_data(dataframe, logger=logger)
    transformed_df.to_csv(output_csv, index=False)
    if logger is not None:
        logger.info("Data written to %s", output_csv)

if __name__ == "__main__":
    db_file = r"C:\Users\usuario\Documents\ALBERTO\IPS\ips_dashboard\data\input\prueba_lab_4_12_t1.sqlite3"
    output_csv = r"C:\Users\usuario\Documents\ALBERTO\IPS\ips_dashboard\data\output\prueba_lab_4_12_t1.csv"
    etl(input_db=db_file, output_csv=output_csv)
