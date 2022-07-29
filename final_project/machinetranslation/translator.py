#pylint translator.py -> get possible errors

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    authenticator=authenticator,
    version='2018-05-01',)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')   # LONDON API URL



def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    
    x = (json.dumps(frenchText, indent=2, ensure_ascii=True))
    y = json.loads(x)

    print(y["translations"][0]["translation"])

    return y["translations"][0]["translation"]
    #return frenchText



def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    
    print(json.dumps(englishText))

    x = (json.dumps(englishText, indent=2, ensure_ascii=True))
    y = json.loads(x)

    return y["translations"][0]["translation"]
    #return englishText


englishToFrench("Hello")