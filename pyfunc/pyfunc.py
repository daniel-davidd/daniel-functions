import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    message = 'Hello {} #### !'.format(event['data'])  
    return { 
        'message' : message
    }