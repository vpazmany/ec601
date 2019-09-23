from google.cloud import language_v1
from google.cloud.language_v1 import enums
import json


def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """
    count_latte=0
    avg_sum_latte=0

    count_cap=0
    avg_sum_cap=0

    count_coldbrew=0
    avg_sum_coldbrew=0

    count_psl=0
    avg_sum_psl=0

    count_frappe=0
    avg_sum_frappe=0

    avg_latte=0
    avg_cap=0
    avg_frappe=0
    avg_psl=0
    avg_coldbrew=0


    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:

        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))
        if 'latte' in sentence.text.content.lower():
            count_latte+=1
            avg_sum_latte+= sentence.sentiment.magnitude
            avg_latte= avg_sum_latte/count_latte
        if 'cappucino' in sentence.text.content.lower():
            count_cap+=1
            avg_sum_cap+= sentence.sentiment.magnitude
            avg_cap= avg_sum_cap/count_cap
        if 'frappe' in sentence.text.content.lower():
            count_frappe+=1
            avg_sum_frappe+= sentence.sentiment.magnitude
            avg_frappe= avg_sum_frappe/count_frappe
        if 'cold brew' in sentence.text.content.lower():
            count_coldbrew+=1
            avg_sum_coldbrew+= sentence.sentiment.magnitude
            avg_coldbrew= avg_sum_coldbrew/count_coldbrew
        if 'pumpkin spice latte' or 'pumpkin' in sentence.text.content.lower():
            count_psl+=1
            avg_sum_psl+= sentence.sentiment.magnitude
            avg_psl= avg_sum_psl/count_psl




    print('Latte Magnitude:',avg_latte,count_latte)
    print('Cappucino Magnitude:',avg_cap,count_cap)
    print('Frappe Magnitude:',avg_frappe,count_frappe)
    print('PSL Magnitude:',avg_psl, count_psl)
    print('Coldbrew Magnitude:',avg_coldbrew, count_coldbrew)
    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))

json_fname='tweet.json'#'test_coffee.json'
json_keyword='text'
with open(json_fname,'r') as f:
  data = json.load(f)
  for x in data:
      example_text = x[json_keyword]
      sample_analyze_sentiment(example_text)
      #print(x['text'])
#print(data[json_keyword])
#example_text = data[json_keyword]#"it's pumpkin spice szn!!!!! Love pumpkin spice coffee!!!"
