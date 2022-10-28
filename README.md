# HNG INTERNSHIP - API

## Setting up

## Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=development
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### Documentation Example

`GET '/'`

- Fetches a dictionary
- Request Arguments: None
- Returns: An object with keys, `age, backend, bio, slackUsername`, that contains an object of `category: data` key: value pairs.

```json
{
  "age": 23, 
  "backend": true, 
  "bio": "My name is Richard Olaoluwa Akintola, a Full Stack Developer", 
  "slackUsername": "laolu"
}
```
