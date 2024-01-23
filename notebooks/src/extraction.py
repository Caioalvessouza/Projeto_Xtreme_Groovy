import pandas as pd
import os
def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'bikes_completed.csv')
    return pd.read_csv(csv_path)

