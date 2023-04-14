import boto3
import os

# Find the AWS credentials file
session = boto3.Session(profile_name='default')
credentials = session.get_credentials()

# Invoke the translation service
translate = boto3.client(service_name='translate')

# Translate the sample text
result = translate.translate_text(Text="Hello, World",
            SourceLanguageCode="en", TargetLanguageCode="de")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
