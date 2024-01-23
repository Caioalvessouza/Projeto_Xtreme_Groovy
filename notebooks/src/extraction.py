import pandas as pd
import os

def load_data():
    # Obtemos o caminho do diretório atual do script
    current_dir = os.path.dirname(__file__)
    
    # Construímos o caminho completo para o arquivo CSV
    csv_path = os.path.abspath(os.path.join(current_dir, '..', 'data', 'bikes_completed.csv'))
    
    # Lemos o arquivo CSV
    return pd.read_csv(csv_path)

