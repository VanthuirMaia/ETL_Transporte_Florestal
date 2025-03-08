import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Carregar o CSV processado
df = pd.read_csv('output/2007_filtered.csv')

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout do Dashboard
app.layout = html.Div([
    html.H1("Dashboard de Análise de Transportes de Produtos Florestais"),

    html.Div([
        html.Label("Selecione a Análise:"),
        dcc.Dropdown(
            id='analise-dropdown',
            options=[
                {'label': 'Análise de Rota', 'value': 'rota'},
                {'label': 'Análise de Produtos', 'value': 'produtos'},
                {'label': 'Mapeamento de Destinatários', 'value': 'destinatarios'},
            ],
            value='rota'  # Valor inicial
        ),
    ]),

    html.Div([
        dcc.Graph(id='grafico'),
    ])
])

# Função para gerar gráfico conforme a análise selecionada
@app.callback(
    Output('grafico', 'figure'),
    [Input('analise-dropdown', 'value')]
)
def update_graph(analise):
    if analise == 'rota':
        # Análise de Rota usando gráfico de barras
        df_rota = df.groupby(['ufOrigem', 'municipioOrigem', 'ufDestino', 'municipioDestino']).agg({'volume': 'sum'}).reset_index()
        fig = px.bar(df_rota, 
                     x='municipioOrigem', 
                     y='volume', 
                     color='municipioDestino', 
                     title="Análise de Rota - Volume de Transporte por Origem e Destino",
                     labels={"municipioOrigem": "Município de Origem", "municipioDestino": "Município de Destino", "volume": "Volume de Transporte"})
        
    elif analise == 'produtos':
        # Análise de Produtos
        df_produtos = df.groupby('produto').agg({'volume': 'sum', 'valor': 'sum'}).reset_index()
        fig = px.bar(df_produtos, x='produto', y='volume', title="Análise de Produtos - Volume por Produto")
        
    elif analise == 'destinatarios':
        # Mapeamento de Destinatários (sem CPF/CNPJ)
        fig = px.scatter(df, x='ufDestino', y='municipioDestino',
                         title="Mapeamento de Destinatários")
                         
    return fig

# Rodar o servidor do Dash
if __name__ == '__main__':
    app.run_server(debug=True)
