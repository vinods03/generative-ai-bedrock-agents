import json
import boto3

dynamodb = boto3.resource('dynamodb')
customer_account_status_tbl = dynamodb.Table('customerAccountStatus')

def lambda_handler(event, context):
    
    print('The event is: ', event)
    
    # account = event['Account']
    account = int(event['parameters'][0]['value'])
    print('The account is: ', str(account))
    
    action_group = event['actionGroup']
    api_path = event['apiPath']
    http_method = event['httpMethod']
    session_attributes = event['sessionAttributes']
    prompt_session_attributes = event['promptSessionAttributes']
    
    print('action_group is: ', action_group)
    print('api_path is: ', api_path)
    print('http_method is: ', http_method)
    print('session_attributes is: ', session_attributes)
    print('prompt_session_attributes is: ', prompt_session_attributes)
    
    response = customer_account_status_tbl.get_item(Key = {'AccountID': account})['Item']
    print('The response is: ', response)
        
    response_body = {
        'application/json': {
            'body': response
        }
    }
    
    action_response = {
        'actionGroup': action_group,
        'apiPath': api_path,
        'httpMethod': http_method,
        'httpStatusCode': 200,
        'responseBody': response_body
    }
        
   
    api_response = {
        'messageVersion': '1.0', 
        'response': action_response,
        'sessionAttributes': session_attributes,
        'promptSessionAttributes': prompt_session_attributes
    } 
    
    return api_response

