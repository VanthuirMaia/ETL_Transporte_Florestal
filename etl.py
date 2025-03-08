import os
import json
import pandas as pd
from glob import glob

def load_json(file_path):
    """Carrega um arquivo JSON e retorna o conteúdo."""
    print(f"Carregando o arquivo: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def normalize_json(data):
    """Normaliza o conteúdo do JSON para um DataFrame."""
    if 'data' in data:
        return pd.json_normalize(data['data'])
    else:
        return pd.json_normalize(data)

def filter_columns(df):
    """Filtra as colunas de interesse para diferentes análises."""
    cols_analise_rota = ['ufOrigem', 'municipioOrigem', 'ufDestino', 'municipioDestino']
    cols_analise_temporal = ['data', 'produto', 'volume', 'valor']
    cols_analise_produtos = ['produto', 'volume', 'valor', 'ufDestino', 'municipioDestino']
    cols_mapeamento_destinatarios = ['cpfCnpjRemetente', 'cpfCnpjDestinatario', 'municipioDestino', 'ufDestino']
    cols_conformidade_legal = ['numSerieDOF', 'ultimaTransacao', 'orgaoEmissorAutesp', 'tipoOrigem', 'paisDestino']

    df_filtered = pd.DataFrame()
    
    for col in [cols_analise_rota, cols_analise_temporal, cols_analise_produtos, 
                cols_mapeamento_destinatarios, cols_conformidade_legal]:
        valid_cols = [c for c in col if c in df.columns]
        if valid_cols:
            df_filtered = pd.concat([df_filtered, df[valid_cols]], axis=1)

    return df_filtered.dropna(axis=1, how='all')

def save_filtered_data(df, file_path):
    """Salva os dados filtrados em um arquivo CSV."""
    if not df.empty:
        output_path = os.path.join('output', f"{os.path.basename(file_path).replace('.json', '_filtered.csv')}")
        df.to_csv(output_path, index=False)
        print(f"Arquivo salvo: {output_path}")
    else:
        print(f"O DataFrame filtrado está vazio para o arquivo {file_path}")

def process_file(file_path):
    """Função para processar cada arquivo JSON individualmente."""
    try:
        data = load_json(file_path)
        df = normalize_json(data)
        print(f"Colunas no arquivo {file_path}: {df.columns.tolist()}")
        
        df_filtered = filter_columns(df)
        save_filtered_data(df_filtered, file_path)
    
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_path}: {e}")
