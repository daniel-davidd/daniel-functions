import logging
import mmh3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    msgmmh = mmh3.hash(event['data'])
    return { 
        'message' : msgmmh
    }