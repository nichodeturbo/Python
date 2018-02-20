
import os
import google.cloud.language
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "PATH"


    # Create a Language client.
language_client = google.cloud.language.LanguageServiceClient()

text = u'Hello, world!'
document = google.cloud.language.types.Document(
content=text,
type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)

    # Use Language to detect the sentiment of the text.
response = language_client.analyze_sentiment(document=document)
sentiment = response.document_sentiment

print(u'Text: {}'.format(text))
print(u'Sentiment: Score: {}, Magnitude: {}'.format(sentiment.score, sentiment.magnitude))
