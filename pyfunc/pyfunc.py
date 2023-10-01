import logging
import jsonschema

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    schema = {
        'data' : {'type' : 'string'}
    }
    return { 
        'message' : jsonschema.validate(event, schema)
    }