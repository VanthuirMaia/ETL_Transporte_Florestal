# pipeline.py
import os
from glob import glob
from etl import process_file

def process_all_files():
    """Função para processar todos os arquivos JSON da pasta 'data'."""
    files = glob('data/*.json')
    
    if not os.path.exists('output'):
        os.makedirs('output')
    
    for file in files:
        process_file(file)

def main():
    print("Iniciando o processo de ETL...")
    process_all_files()

if __name__ == "__main__":
    main()
