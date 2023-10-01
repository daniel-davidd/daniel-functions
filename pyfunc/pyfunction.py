import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('Event: {}'.format(event))
    logger.info('Context: {}'.format(context))
    result = event['data'] + "heiiiiiiii"
    response = {'data': result}
    return response