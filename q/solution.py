import json
import queue
from q import transform_rule
from q import dispatch_rule


class QadiumQueue:

    def __init__(self):
        self.mq0 = queue.Queue()
        self.mq1 = queue.Queue()
        self.mq2 = queue.Queue()
        self.mq3 = queue.Queue()
        self.mq4 = queue.Queue()

    """ Returns next message in queue, takes queue_number as argument """
    def next(self, queue_number):
        switcher = {
            0: self.mq0,
            1: self.mq1,
            2: self.mq2,
            3: self.mq3,
            4: self.mq4,
        }
        try:
            msg = switcher[queue_number].get(block=False)
        except queue.Empty:
            raise StopIteration('Queue {0} is empty'.format(queue_number))
        else:
            return msg

    """ Takes msg as string of json """
    def enqueue(self, msg_str):
        alt_msg = self.transform(msg_str)
        self.dispatch(alt_msg)

    """ Takes msg as json object """
    def dispatch(self, msg_json):
        # print('Notice: dispatching transformed msg {0}'.format(msg_json))

        msg_str = json.dumps(msg_json)

        if dispatch_rule.has_key_special(msg_json):
            # print('Sending msg to queue 0')
            self.mq0.put(msg_str)
        elif dispatch_rule.has_key_hash(msg_json):
            # print('Sending msg to queue 1')
            self.mq1.put(msg_str)
        elif dispatch_rule.has_value(msg_json, string='muidaQ'):
            # print('Sending msg to queue 2')
            self.mq2.put(msg_str)
        elif dispatch_rule.has_value_int(msg_json):
            # print('Sending msg to queue 3')
            self.mq3.put(msg_str)
        else:
            # print('Sending msg to queue 4')
            self.mq4.put(msg_str)

    """ Apply transformation rules to message """
    def transform(self, msg):
        msg_json = json.loads(msg)
        transformations = [t(msg_json) for t in [transform_rule.transform1,
                                                 transform_rule.transform2,
                                                 transform_rule.transform3,
                                                 ]]
        for transform in transformations:
            if transform is not None:
                msg_json.update(transform)

        return msg_json


# Regardless of how you choose to implement your solution, please do something
# like this so that we can get a clean instance of your solution by calling
# q.solution.get_message_service().
def get_message_service():
    """Returns a new, "clean" Q service."""
    return QadiumQueue()