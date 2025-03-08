import os
import json
import pandas as pd
from glob import glob

# Função para processar os arquivos JSON e extrair os dados relevantes
def process_file(file_path):
    print(f"Processando o arquivo: {file_path}")
    try:
        # Carregar o arquivo JSON
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Verificar se o JSON possui a chave 'data' ou uma estrutura similar
        if 'data' in data:
            df = pd.json_normalize(data['data'])
        else:
            # Se não houver 'data', tenta normalizar diretamente o JSON
            df = pd.json_normalize(data)
        
        # Verificando as colunas no DataFrame
        print(f"Colunas no arquivo {file_path}: {df.columns.tolist()}")
        
        # Filtrar apenas as colunas que interessam para cada análise
        cols_analise_rota = ['ufOrigem', 'municipioOrigem', 'ufDestino', 'municipioDestino']
        cols_analise_temporal = ['data', 'produto', 'volume', 'valor']
        cols_analise_produtos = ['produto', 'volume', 'valor', 'ufDestino', 'municipioDestino']
        cols_mapeamento_destinatarios = ['cpfCnpjRemetente', 'cpfCnpjDestinatario', 'municipioDestino', 'ufDestino']
        cols_conformidade_legal = ['numSerieDOF', 'ultimaTransacao', 'orgaoEmissorAutesp', 'tipoOrigem', 'paisDestino']
        
        # Filtrando as colunas para cada análise, garantindo que as colunas existam
        df_filtered = pd.DataFrame()

        for col in [cols_analise_rota, cols_analise_temporal, cols_analise_produtos, cols_mapeamento_destinatarios, cols_conformidade_legal]:
            valid_cols = [c for c in col if c in df.columns]
            if valid_cols:
                df_filtered = pd.concat([df_filtered, df[valid_cols]], axis=1)

        # Excluindo colunas que não têm dados válidos (NaN)
        df_filtered = df_filtered.dropna(axis=1, how='all')
        
        if not df_filtered.empty:
            # Salvando o DataFrame filtrado em um arquivo CSV na pasta 'output'
            output_path = os.path.join('output', f"{os.path.basename(file_path).replace('.json', '_filtered.csv')}")
            df_filtered.to_csv(output_path, index=False)
            print(f"Arquivo salvo: {output_path}")
        else:
            print(f"O DataFrame filtrado está vazio para o arquivo {file_path}")
    
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_path}: {e}")

# Função principal para processar todos os arquivos JSON na pasta 'data'
def process_all_files():
    files = glob('data/*.json')
    if not os.path.exists('output'):
        os.makedirs('output')
    
    for file in files:
        process_file(file)

# Chamada da função principal
if __name__ == "__main__":
    process_all_files()
