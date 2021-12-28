"""
English to French & French to English Using IBM Watson
"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-12-29',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    """
    This function translates english to french
    """

    frenchtranslation = language_translator.translate(
                            text=englishText,model_id='en-fr'
                            ).get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def frenchToEnglish(frenchText):
    #write the code here
    """
    This function translates french to english
    """

    englishtranslation = language_translator.translate(
                            text=frenchText,model_id='fr-en'
                            ).get_result()
    return englishtranslation.get("translations")[0].get("translation")
