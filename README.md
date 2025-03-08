
# ETL para Análise de Dados - DOF Transportes de Produtos Florestais

Este repositório contém um projeto para a construção de um processo de ETL (Extração, Transformação e Carga) para preparar dados provenientes do **DOF (Documento de Origem Florestal)**, com o objetivo de realizar uma análise detalhada sobre o transporte de produtos florestais no Brasil.

## Objetivo do Projeto

O objetivo deste projeto é processar e preparar o **Dataset Público de DOF - Transportes de Produtos Florestais**, fornecido pelo [IBAMA](https://dadosabertos.ibama.gov.br/dataset/dof-transportes-de-produtos-florestais), para análise de dados. Este processo de ETL será dividido em três etapas:

1. **Extração**: Obtenção dos dados do dataset público.
2. **Transformação**: Limpeza, normalização e enriquecimento dos dados para garantir sua qualidade e relevância para análise.
3. **Carga**: Carregamento dos dados transformados em um formato adequado para análise, como um banco de dados ou arquivo CSV.

## Estrutura do Repositório

```bash
├── data/
│   ├── raw/               # Dados brutos extraídos
│   └── processed/         # Dados processados e prontos para análise
├── src/
│   ├── extract.py         # Script de extração dos dados
│   ├── transform.py       # Script de transformação dos dados
│   └── load.py            # Script de carga dos dados
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

## Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/etl-dof-transporte.git
   cd etl-dof-transporte
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute os scripts na ordem das etapas de ETL:

   - **Extração de Dados**:
     ```bash
     python src/extract.py
     ```

   - **Transformação de Dados**:
     ```bash
     python src/transform.py
     ```

   - **Carga de Dados**:
     ```bash
     python src/load.py
     ```

## Dependências

Este projeto utiliza as seguintes bibliotecas:

- `pandas`: Para manipulação e análise de dados.
- `requests`: Para download dos dados, se necessário.
- `sqlalchemy`: Para interação com banco de dados (caso o destino seja um banco de dados relacional).
- `numpy`: Para operações numéricas.

Você pode instalar essas dependências usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Contribuindo

Sinta-se à vontade para contribuir para este projeto! Se você quiser sugerir melhorias, correções de bugs ou outras melhorias, basta abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.
