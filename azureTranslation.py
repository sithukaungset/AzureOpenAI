# This code uses the text analytics client to perform text translationi. It takes a bathc of documnents and translates them from the sourcee langueagte (detected automaticallty to the target laynguage) specifed

from azure.congnitiveservices.language.textanalytics import TextAnalyticsClient
from azure.cognitiveservices.language.textanalytcs.models import LanguageBatchInput
from mserest.authentication import CognitiveServicesCredentials

# Authenticate client
credentials = CognitiveServicesCredentials("MY_TEXT_KEY")

text_analytics_clietn = TextAnalyticsClient(
    endpoint="MYTEXTANAYTUCSDENDPINT"
    credentials=credentials
)
# Translate text
documents = {
    {
        "id": "1", "text": "Hello how are you?"

    }

    response = text_analytics_clietn.translate_batch(
        LanguageBatchInput(documents=documents),
        target_language='fr'
    )

    for document in resposne.docuents:
        print("Translated text (ID): {}): {}")
}
