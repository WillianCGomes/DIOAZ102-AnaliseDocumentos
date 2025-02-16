# Análise de Documentos Anti-fraude com Azure AI

Este projeto foi desenvolvido como parte do desafio de projeto **Análise de Documentos Anti-fraude com Azure AI** da **DIO** para a certificação **AZ-102**.

O objetivo deste projeto é demonstrar a capacidade do Azure AI em analisar imagens de cartões de crédito e extrair informações relevantes para validar sua autenticidade. O projeto utiliza o serviço de Form Recognizer para identificar e extrair informações como nome do titular, número do cartão, data de validade e banco emissor. Além disso, integra-se com o Azure Blob Storage para armazenar as imagens enviadas.

## Funcionamento

1. **Upload da Imagem:** O usuário carrega uma imagem de cartão de crédito através de um interface web construída com Streamlit. Os formatos suportados são PNG, JPG e JPEG.
2. **Envio para o Blob Storage:** A imagem carregada é enviada para um container no Azure Blob Storage.
3. **Análise com Form Recognizer:** A URL da imagem no Blob Storage é enviada para o serviço Form Recognizer. O modelo "prebuilt-document" é utilizado para analisar a imagem e extrair as informações do cartão de crédito.
4. **Exibição dos Resultados:** O aplicativo exibe a imagem enviada e os resultados da análise, incluindo o nome do titular, banco emissor e data de validade, caso o cartão seja considerado válido. Se a análise falhar ou o cartão for considerado inválido, uma mensagem correspondente é exibida.

## Arquitetura

O projeto utiliza os seguintes serviços do Azure:

* **Azure Blob Storage:** Armazenamento das imagens de cartão de crédito.
* **Azure Form Recognizer:** Análise das imagens e extração de informações.

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Streamlit:** Framework para criação da interface web.
* **Azure SDK para Python:** Biblioteca para interagir com os serviços do Azure.
* **python-dotenv:** Para gerenciar variáveis de ambiente.

## Instalação e Execução

1. **Clone o repositório:** `git clone <URL_DO_REPOSITORIO>`
2. **Instale as dependências:** `pip install -r requirements.txt`
3. **Configure as variáveis de ambiente:**
    * Crie um arquivo `.env` na raiz do projeto.
    * Adicione as seguintes variáveis com seus respectivos valores:
        * `ENDPOINT`: Endpoint do Form Recognizer.
        * `SUBSCRIPTION_KEY`: Chave de assinatura do Form Recognizer.
        * `AZURE_STORAGE_CONNECTION_STRING`: String de conexão do Azure Blob Storage.
        * `CONTAINER_NAME`: Nome do container no Blob Storage.
4. **Execute o aplicativo:** `streamlit run app.py`

## Arquivos

* `app.py`: Arquivo principal do aplicativo Streamlit.
* `blob_service.py`: Funções para interagir com o Azure Blob Storage.
* `credit_card_service.py`: Funções para interagir com o Azure Form Recognizer.
* `config.py`: Configurações do projeto.
* `requirements.txt`: Arquivo com as dependências do projeto.
* `.env`: Arquivo para armazenar as variáveis de ambiente (**não inclua este arquivo no repositório público**).

## Considerações

* Certifique-se de ter uma conta Azure ativa e os serviços Blob Storage e Form Recognizer configurados.
* As credenciais de acesso aos serviços do Azure devem ser armazenadas de forma segura, idealmente utilizando Azure Key Vault.
* Este projeto é uma demonstração e pode necessitar de ajustes para ser utilizado em produção.

## Autor
Willian Carlos Gomes