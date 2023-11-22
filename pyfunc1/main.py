import json
import base64

def handler(event, context): 
    return create_function(event, event_handler = event_handler)

def event_handler(msg_payload, msg_headers, inputs):
    payload =  str(msg_payload, 'utf-8')
    as_json = json.loads(payload) 
    as_json['went in lambda'] = "yessir"
    as_json['went in lambda2'] = "yessir2"

    return bytes(json.dumps(as_json), encoding='utf-8'), msg_headers

def create_function(
    event,
    event_handler: callable
) -> None:
    class EncodeBase64(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, bytes):
                return str(base64.b64encode(o), encoding='utf-8')
            return json.JSONEncoder.default(self, o)

    def handler(event):
        processed_events = {}
        processed_events["messages"] = []
        processed_events["failed_messages"] = []
        for message in event["messages"]:
            try:
                payload = base64.b64decode(bytes(message['payload'], encoding='utf-8'))
                processed_message, processed_headers = event_handler(payload, message['headers'], event["inputs"])

                if isinstance(processed_message, bytes) and isinstance(processed_headers, dict):
                    processed_events["messages"].append({
                        "headers": processed_headers,
                        "payload": processed_message
                    })
                elif processed_message is None and processed_headers is None: # filter out empty messages
                    continue
                elif processed_message is None or processed_headers is None:
                    err_msg = f"processed_messages is of type {type(processed_message)} and processed_headers is {type(processed_headers)}. Either both of these should be None or neither"
                    raise Exception(err_msg)
                else:
                    err_msg = "The returned processed_message or processed_headers were not in the right format. processed_message must be bytes and processed_headers, dict"
                    raise Exception(err_msg)
            except Exception as e:
                processed_events["failed_messages"].append({
                    "headers": message["headers"],
                    "payload": message["payload"],
                    "error": str(e)  
                })

        try:
            return json.dumps(processed_events, cls=EncodeBase64).encode('utf-8')
        except Exception as e:
            return f"Returned message types from user function are not able to be converted into JSON: {e}"

    return handler(event)