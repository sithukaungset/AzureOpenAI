# Using the text analytics service to platform sentiment analysis on a
# a piece of text using Python. This can be useful in applications such as monitoring
# customer feedback or social media sentiment

# Make sure -

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def authenticate_client():
    key = "MY_TEXT_ANALYTICS_KEY"
    endpoint = "MY_TEXT_ANALYTICS_ENDPOINT"
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=ta_credential)
    return text_analytics_client


def sentiment_analysis_example(client):

    documents = [
        "I had the best day of my life. I wish you were there with me."]
    response = client.analyze_sentiment(documents=documents)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive = {0:.2f}; neutral={1:.2f}; negative{2:.2f} \n".format(
        response.confidence_scores.postive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))


client = authenticate_client()
sentiment_analysis_example(client)


# The authenticate_client function authenticates my client using my key and endpoint. Replace analytics key and
# The sentiment_analysis_example function sends a single document to the text analytics service for sentiment
# analysis. The service returns the overall sentiment of the document, as well as confidence scores for postive, netural , and negative sentiments
# Finally, the code authenticates the client and calls the sentiment analysis function
