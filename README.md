
# ETL para Análise de Dados - DOF Transportes de Produtos Florestais

Este repositório contém um projeto para a construção de um processo de **ETL (Extração, Transformação e Carga)** para preparar dados provenientes do **DOF (Documento de Origem Florestal)**, com o objetivo de realizar uma análise detalhada sobre o transporte de produtos florestais no Brasil.

## Objetivo do Projeto

O objetivo deste projeto é processar e preparar o **Dataset Público de DOF - Transportes de Produtos Florestais**, fornecido pelo [IBAMA](https://dadosabertos.ibama.gov.br/dataset/dof-transportes-de-produtos-florestais), para análise de dados. O processo de ETL será dividido nas seguintes etapas:

1. **Extração**: Obtenção dos dados a partir de arquivos JSON.
2. **Transformação**: Limpeza, normalização e enriquecimento dos dados para garantir a qualidade e relevância para a análise.
3. **Carga**: Armazenamento dos dados transformados em arquivos CSV prontos para análise.

## Estrutura do Repositório

```bash
├── data/
│   ├── raw/               # Dados brutos extraídos (arquivos JSON)
│   └── processed/         # Dados processados e prontos para análise (arquivos CSV)
├── src/
│   ├── etl.py             # Script principal com funções para o processo de ETL
│   └── pipeline.py        # Pipeline para execução do processo de ETL
├── output/                # Pasta de saída para arquivos CSV
├── requirements.txt       # Dependências do projeto
├── poetry.lock            # Dependências travadas para garantir reprodutibilidade
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
   poetry install
   ```

3. Crie um ambiente virtual, caso ainda não tenha:

   ```bash
   poetry env use python3.11  # Certifique-se de usar a versão correta do Python
   ```

4. Ative o ambiente virtual:

   ```bash
   poetry shell
   ```

5. Execute o pipeline ETL (Extração, Transformação e Carga) com o seguinte comando:

   ```bash
   python src/pipeline.py
   ```

Este comando irá executar a sequência completa de processos para obter, transformar e salvar os dados.

## Dependências

Este projeto utiliza as seguintes bibliotecas:

- `pandas`: Para manipulação e análise de dados.
- `poetry`: Para gerenciamento das dependências.
- `json`: Para trabalhar com arquivos JSON.
- `glob`: Para encontrar arquivos em diretórios.

Para instalar as dependências do projeto, utilize:

```bash
poetry install
```

## Contribuindo

Sinta-se à vontade para contribuir para este projeto! Se você quiser sugerir melhorias, correções de bugs ou outras contribuições, basta abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.
