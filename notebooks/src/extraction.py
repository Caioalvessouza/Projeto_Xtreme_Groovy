import pandas as pd

def load_data():
    csv_path = "C:\\Users\\Caio\\Documents\\cientista de dados\\phyton\\Git para cientista de dados\\projeto\\notebooks\\data\\bikes_completed.csv"
    return pd.read_csv(csv_path)
