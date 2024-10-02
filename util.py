import pandas as pd

def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    tables.columns = tables.columns.str.strip()  # Remove leading/trailing spaces from column names
    filtered_tables = tables.query("to_be_loaded == 'yes'")  # Filter the tables
    return filtered_tables

