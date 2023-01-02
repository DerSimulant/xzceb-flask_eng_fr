import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

lt.set_service_url('url')



def englishToFrench(englishText):
    '''Translates the English text in the string variable "text" to French
    and returns the translation. To get to the translation you need to access the 
    1st data in the JSON returned. Rest is additional data'''

    frenchText = lt.translate(
    text=englishText,
    model_id='en-fr').get_result()
    print(json.dumps(frenchText, indent=2, ensure_ascii=False))
    return frenchText

def frenchToEnglish(frenchText):
    '''Translates the French text in the string variable "text" to English
    and returns the translation. To get to the translation you need to access the 
    1st data in the JSON returned. Rest is additional data'''
    
    englishText = lt.translate(
    text=frenchText,
    model_id='en-fr').get_result()
    print(json.dumps(englishText, indent=2, ensure_ascii=False))
    return englishText 
