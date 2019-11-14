# Demo: "Building Rich Context from Jupyter's Telemetry System"

Here, we demostrate how to leverage Jupyter's new [Telemetry System]() to construct "rich context" around notebook+data usage in a JupyterHub deployment. This is particularly useful in research environments where usage data (from willing users) can inform relationships between notebooks, data sets, and literature. 

**Warning!** This is only a demo. It uses experimental branches of jupyter/telemetry, jupyterhub/jupyterhub, and jupyter/notebook and runs an insecure deployment of JupyterHub (useful only for demos/testing). DO NOT use any of this in production. You should only run this type of configuration locally on a single laptop. Authentication is essentially nonexistent--any user can log in and run arbitrary code on the underlying server.

## Setup and installion.

First, you'll need to clone this repo.

Because this demo uses experimental branches of various Jupyter repos, it is *highly recommended* that you run this demo in a virtual environment. The easiest way to get started is to create a new conda environment. This repo provides an `environment.yml` file with everything you need to get started, including the experimental branches you'll need. Use conda to create an environment from this file:

```
conda env create environment.yml
```

Once everything is installed, you'll be able to run the demo using the `run.sh` file.
```
sh run.sh
```

JupyterHub will start and you should land on a login page. `admin` is the only reserved account (any password will get you into this account). `admin` contains a set of Jupyter notebooks that track telemetry data across the JupyterHub.

Any other username (and password) will create a new account for that username. Actions by this user will be tracked in the `logs/all-events.log` file and watched by the admin account.

