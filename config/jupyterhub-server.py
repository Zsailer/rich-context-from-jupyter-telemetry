import logging

# Define log files
all_events_log = 'logs/all-events.log'
hub_log = 'logs/hub.log'

# Define schema lists
hub_schemas = [
    'hub.jupyter.org/server-action'
]

# Define Handlers
all_events_handler = logging.FileHandler(all_events_log)
hub_events_handler = logging.FileHandler(hub_log)

# Configure the JupyterHub Server Eventlog.
c.EventLog.handlers = [
    all_events_handler,
    hub_events_handler
]
c.EventLog.allowed_schemas = hub_schemas

# Configure a "dummy" JupyterHub
from jupyterhub.auth import DummyAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner

c.JupyterHub.authenticator_class = DummyAuthenticator
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner
c.Spawner.args = ['--config=../../config/singleuser-server.py']
c.Spawner.home_dir_template = 'users/{username}'
c.Spawner.default_url = '/lab'