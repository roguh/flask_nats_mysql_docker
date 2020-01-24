# Flask, NATS, MySQL, and Docker

## Installation

- Install Docker.
- Run `pipenv shell` to create Python virtual environment, install Python dependencies, and start a shell with virtual environment enabled.

### Updating Pipfile

Run `pipenv install -r requirements.txt` to re-generate the Pipfile.

## Running

```
docker-compose up
```

- connect to [https://localhost:8080](https://localhost:8080) to manage the MySQL database
- connect to [https://localhost:TBD](https://localhost:TBD) for the Flask server
- send a test event to 0mq by running `TODO`


## Configuration

Set FLASK_APPLICATION_SETTINGS to a Flask configuration file:

```
export FLASK_APPLICATION_SETTINGS='flask_dev_config.py'
```
