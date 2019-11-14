import logging

# Define log files
all_events_log = '../../logs/all-events.log'
contents_log = '../../logs/contents.log'
kernels_log = '../../logs/kernels.log'

# Define schemas list.
contents_schemas = [
    'eventlogging.jupyter.org/notebook/contentsmanager-actions'
]

kernels_schemas = [
    'eventlogging.jupyter.org/notebook/websocketmessaging-actions'
]

# Define Handlers
# contents_handler = logging.FileHandler(contents_log)
# kernels_handler = logging.FileHandler(kernels_log)
all_events_handler = logging.FileHandler(all_events_log)

# Configure the server eventlog to watch for the above events.
c.EventLog.handlers = [
    all_events_handler,
    # contents_handler,
    # kernels_handler
]

c.EventLog.allowed_schemas = contents_schemas + kernels_schemas