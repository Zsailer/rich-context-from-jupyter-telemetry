import logging

# Define log files
contents_log = 'logs/contents.log'
kernels_log = 'logs/kernels.log'

# Define schemas list.
contents_schemas = [
    'eventlogging.jupyter.org/notebook/contentsmanager-actions'
]

kernels_schemas = [
    'eventlogging.jupyter.org/notebook/websocketmessaging-actions'
]

# Define Handlers
contents_handlers = logging.FileHandler(contents_log)
kernels_handlers = logging.FileHandler(kernels_log)

# Configure the server eventlog to watch for the above events.
c.EventLog.handlers = [
    contents_handlers,
    kernels_handlers
]

c.EventLog.allowed_schemas = contents_schemas + kernels_schemas