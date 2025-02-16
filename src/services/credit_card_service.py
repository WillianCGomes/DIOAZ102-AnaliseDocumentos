from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import Config

def analize_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)
        document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

        card_info = document_Client.begin_analyze_document("prebuilt-document", AnalyzeDocumentRequest(url_source=card_url))
        result = card_info.result()

        for document in result.documents:
            fields = document.get("fields", {})

            return {
                "card_name": fields.get('CardholderName', {}).get('content'),
                "card_number": fields.get('CardNumber', {}).get('content'),
                "expiration_date": fields.get('ExpirationDate', {}).get('content'),
                "bank_name": fields.get('IssuingBank', {}).get('content')
            }

    except Exception as e:
        print(e)