import logging


c.EventLog.handlers = [logging.FileHandler('logs/events.log')]
c.EventLog.allowed_schemas = [
#    'eventlogging.jupyter.org/notebook/contentsmanager-actions',
    'eventlogging.jupyter.org/notebook/websocketmessaging-actions'
]