import base64
import hashlib

""" Test message for 'Qadium' substring in values, ignore private elements """
def transform1(msg):
    for k, v in msg.items():
        if not k.startswith('_'):
            if isinstance(v, str) and 'Qadium' in v:
                msg[k] = v[::-1]
    return msg


""" Test message for integer value, ignore private elements """
def transform2(msg):
    for k, v in msg.items():
        if not k.startswith('_'):
            if isinstance(v, int):
                msg[k] = ~v
    return msg


""" Compute hash of field specified in _hash key """
def transform3(msg):
    if '_hash' in msg:
        hash_field = msg['_hash']

        hash_object = hashlib.sha256(hash_field.encode('utf-8'))
        hex_dig = hash_object.hexdigest()

        msg['hash'] = base64.b64encode(hex_dig.encode('utf-8')).decode('utf-8')
    return msg