def has_key_special(msg):
    if '_special' in msg:
        return 'Notice: "_special" key exists'


def has_key_hash(msg):
    if 'hash' in msg:
        return 'Notice: "hash" key exists'


def has_value(msg, string=None):
    for key, value in msg.items():
        if not key.startswith('_'):
            if isinstance(value, str) and string in value:
                return 'Notice: msg contains string value "{}"'.format(string)


def has_value_int(msg):
    for key, value in msg.items():
        if not key.startswith('_'):
            if isinstance(value, int):
                return 'Notice: msg contains an integer'