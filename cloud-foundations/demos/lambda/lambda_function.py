import json

def lambda_handler(event, context):
    # Extract 'name' from the event input
    name = event.get('name', 'World') # Default to 'World' if no name is provided
    
    # Construct the greeting message
    greeting = f'Hello, {name}!'

    # Return the message
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
