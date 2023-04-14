# aws_translate_text_api
This is a simple hello world that uses the translate text API. 

Here’s how to use the Translate Text API:

1. Log into the AWS Management Console. Go to IAM and create a new user and/or user group and grant it permissions to the AWS TranslateText API. Make a note or download a csv of the AWS Access Key ID and AWS Secret Access Key. Remember: never put this sensitive information directly in your code.
2. The AWS TranslateText API comes built in with the AWS CLI v2. Unlike AWS CLI v1 which you can install with pip, AWS CLI v2 uses a windows installer. Make sure you have AWS CLI v2 to proceed.
3. Next, create an AWS credentials file using the AWS CLI by typing in “aws configure”. It will prompt you for the AWS Access Key ID, AWS Secret Access Key, the default region name, and the default output format. Enter in the AWS Access Key ID and AWS Secret Access Key ID from step 1. For the default region name, use the region from the AWS Management Console. For the default output format, just leave it empty and click enter. It will create a config and credentials file located at C:\Users\username\.aws.
4. In your python script, import boto3 and os, then create a boto3 session: session = boto3.Session(profile_name=’default’)
5. Then access your credentials: credentials = session.get_credentials()
6. Then invoke the TranslateText service: translate = boto3.client(service_name=’translate’)
7. Lastly, translate the text with the translate_text function

Note: The API requires a source language code and a target language code. For a list of supported languages, check out the AWS website: https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html
