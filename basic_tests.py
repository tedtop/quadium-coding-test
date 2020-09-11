#!/usr/bin/env python3
# If the line above fails on your machine, just run `python basic_test.py`.
import json

from q import solution


def get_new_service():
    return solution.get_message_service()


def test_integer_negation():
    svc = get_new_service()
    svc.enqueue('{"test": "message", "int_value": 512}')
    returned = json.loads(svc.next(3))
    if returned["int_value"] != -513:
        print("**FAILED** You did not negate the integer value.")
    else:
        print("**SUCCESS** You did negate the integer value.")

def test_special_field():
    svc = get_new_service()
    svc.enqueue('{"test": "message", "_special": "This must go to queue 0"}')
    try:
        svc.next(0)
    except Exception:
        print("**FAILED** You did not send the special message to queue 0.")
    else:
        print("**SUCCESS** You did send the special message to queue 0.")


def test_hash_field():
    svc = get_new_service()
    svc.enqueue('{"_hash": "message", "message": "This must go to queue 1"}')
    try:
        svc.next(1)
    except Exception:
        print("**FAILED** You did not send the special message to queue 1.")
    else:
        print("**SUCCESS** You did send the special message to queue 1.")


def test_value_muidaq():
    svc = get_new_service()
    svc.enqueue('{"company": "Qadium, Inc.", "message": "This must go to queue 2"}')
    try:
        svc.next(2)
    except Exception:
        print("**FAILED** You did not send the special message to queue 2.")
    else:
        print("**SUCCESS** You did send the special message to queue 2.")


def test_value_int():
    svc = get_new_service()
    svc.enqueue('{"int_value": 2345, "message": "This must go to queue 3"}')
    try:
        svc.next(3)
    except Exception:
        print("**FAILED** You did not send the special message to queue 3.")
    else:
        print("**SUCCESS** You did send the special message to queue 3.")


def test_sequence():
    svc = get_new_service()
    svc.enqueue('{"_sequence": "seq123", "_part": 0, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seq123", "_part": 1, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seq123", "_part": 2, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seq123", "_part": 3, "test": "message", "_special": "This must go to queue 0"}')

    part = -1
    try:
        while True:
            msg_str = svc.next(0)
            msg_json = json.loads(msg_str)


            print(msg_json)
            if not part < msg_json['_part']:
                print('**FAILED** Sequence parts out of order')
            else:
                part = msg_json['_part']
    except StopIteration:
        print("The queue is empty")

def test_sequence_unordered():
    svc = get_new_service()
    svc.enqueue('{"_sequence": "seq123", "_part": 0, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seq123", "_part": 6, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seq123", "_part": 4, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seq123", "_part": 2, "test": "message", "_special": "This must go to queue 0"}')

    part = -1
    try:
        while True:
            msg_str = svc.next(0)
            msg_json = json.loads(msg_str)


            print(msg_json)
            if not part < msg_json['_part']:
                print('**FAILED** Sequence parts out of order')
            else:
                part = msg_json['_part']
    except StopIteration:
        print("The queue is empty")


def test_multiple_sequences():
    svc = get_new_service()
    svc.enqueue('{"_sequence": "seqA", "_part": 1, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seqB", "_part": 1, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seqA", "_part": 2, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seqB", "_part": 2, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seqA", "_part": 3, "test": "message", "_special": "This must go to queue 0"}')
    svc.enqueue('{"_sequence": "seqB", "_part": 3, "test": "message", "_special": "This must go to queue 0"}')

    part = -1
    try:
        while True:
            msg_str = svc.next(0)
            msg_json = json.loads(msg_str)


            print(msg_json)
            if not part < msg_json['_part']:
                print('**FAILED** Sequence parts out of order')
            else:
                part = msg_json['_part']
    except StopIteration:
        print("The queue is empty")


if __name__ == "__main__":
    test_integer_negation()
    test_special_field()
    test_hash_field()
    test_value_muidaq()
    test_value_int()
    test_sequence()
    test_sequence_unordered()
    test_multiple_sequences()
