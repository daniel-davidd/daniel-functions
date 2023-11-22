import json
import base64
from memphis.functions import create_function

def handler(event, context): 
    return create_function(event, event_handler = event_handler)

def event_handler(msg_payload, msg_headers, inputs):
    payload =  str(msg_payload, 'utf-8')
    as_json = json.loads(payload) 
    as_json['went in lambda'] = "yessir"
    as_json['went in lambda2'] = "yessir2"

    return bytes(json.dumps(as_json), encoding='utf-8'), msg_headers



