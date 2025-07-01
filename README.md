# Cardápio sugerido

## Motivação
Este projeto tem como objetivo desenvolver um modelo preditivo para definir um cardápio para uma refeição com base no histórico de cardápios, segundo dia da semana e horário, a fim de trazer uma recomendação diária para os usuários de uma empresa de restaurantes coorporativos. Nesse projeto usa-se o dataset [Online retail](https://www.kaggle.com/datasets/lakshmi25npathi/online-retail-dataset/data), que tem dados de compra de varejo online.

## Bibliotecas utilizadas  
- pandas
- numpy
- scikit-learn
- tensorflow
- fastapi
- pydantic
- uvicorn

Para instalá-las, basta rodar `pip install -r requirements.txt`.

## Limpeza e Tratamento dos Dados
Foi usado nessa etapa os arquivos `limpeza.py` e `tratamento.py`.
Para limpeza e tratamentos dos dados, fez-se as seguintes técnicas:
- Criação de colunas referentes a horário e a dia da semana
- Agrupamento de registros com pouca aparição
- Remoção de espaços desnecessários e mudança das letras para minúsculo

## Explicação do Modelo
Foi usado nessa etapa o arquivo `treinamento.py`.
O modelo utilizado foi uma Rede Neural LSTM, que é eficiente para capturar dependências temporais em séries históricas. Ele foi treinado para prever o cardápio, dado um dia da semana e um horário de refeição (café-da-manhã, almoço ou jantar). 

## Testes e Avaliação
Foi usado nessa etapa o arquivo `teste.py`.
O conjunto de teste foi separado com 20% dos dados. A métrica utilizada foi acurácia. O modelo atingiu uma acurácia de 5% no conjunto de teste.
A imagem abaixo mostra os resultados obtidos.

## API
Foi usado nessa etapa o arquivo `app.py`.
A API foi construída usando FastAPI e expõe o endpoint `/predict` que recebe dados no formato JSON e retorna a predição do modelo. A API, para fins de economia financeira, foi criada e executada localmente.
A imagem abaixo mostra o uso dela com seu resultado.


## Conclusão
Embora os resultados do modelo não tenham sido expressivos, principalmente pela limitação no tratamento dos dados e pela alta variabilidade das informações, todas as etapas foram realizadas de forma clara e concisa, permitindo visualizar previsões diretamente na planilha final com base no histórico de refeições original.

Para os próximos passos, é fundamental aprimorar a acurácia utilizando técnicas, como a aplicação do teste de Dickey-Fuller para verificar a estacionariedade da série temporal (ou seja, se a média e a variância permanecem constantes ao longo do tempo), o que garante que a série possa ser prevista. Caso necessário, é recomendável aplicar técnicas de normalização para garantir a estacionariedade. Além disso, integrar a planilha ou a API a uma plataforma de visualização ou a um website interno pode facilitar o acesso e o acompanhamento dos resultados por diferentes usuários da empresa. Também visando a melhoria do projeto, seria interessante utilizar uma plataforma de automação para o melhor acesso a informação. Nesse projeto não foi usado automação devido ao link da url ser privada, porém seria utilizado o sistema [Albato](https://albato.com), uma plataforma que conecta aplicações e sistemas de forma simples, permitindo criar fluxos de trabalho automatizados sem necessidade de programação. Nesse projeto, a ideia seria que o Albato consumisse os dados gerados pela API e os enviasse diretamente para o Google Sheets, facilitando o acesso e o uso das informações por equipes sem conhecimento técnico avançado.

