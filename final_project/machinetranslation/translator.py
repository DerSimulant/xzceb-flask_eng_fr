'''
This module is a translator utilizing the IBM wastom web service via API
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

lt.set_service_url(url)


def english_to_french(english_text):
    '''Translates the English text in the string variable "text" to French
    and returns the translation. To get to the translation you need to access the
    1st data in the JSON returned. Rest is additional data'''

    french_text = lt.translate(
    text=english_text,
    model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    '''Translates the French text in the string variable "text" to English
    and returns the translation. To get to the translation you need to access the
    1st data in the JSON returned. Rest is additional data'''

    english_text = lt.translate(
    text=french_text,
    model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text['translations'][0]['translation']

#print(englishToFrench("Hello my name is Sebastian "))
#print(englishToFrench("Hello my name is Sebastian ")['translations'][0]['translation'])
