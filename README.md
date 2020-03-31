# flask-decop

A Flask extension that forces extremely skinny controllers.

```python
@app.route("/dogs/<int:dog_id>", methods=["POST"])
@decop.responses({200: responses.greet_dog, 400: responses.bad_request})
@decop.intent(intents.greet_dog)
def greet_dog(dog_id):
    pass
```

## Description

This extension contains two decorators, `@decop.intent` and `@decop.responses`.

* `@decop.intent(callable)`
    * `callable`: Receives `flask.request`, returns `status_code` and `outcome`.
* `@decop.responses({status_code: callable, ...})`
    * `callable`: Receives `flask.request` and `outcome`, returns `headers` and `body`.

`@decop.responses` will choose an appropriate response by `status_code`.

## Simple Usage

```python
from flask import Flask
from flask_decop import decop
from random import randint
import json


def intent(request):
    if randint(0, 1) == 0:
        status_code = 200
        outcome = "OK"
    else:
        status_code = 403
        outcome = "Forbidden"
    return status_code, outcome


def response(request, outcome):
    headers = {"content-type": "application/json"}
    body = json.dumps({"message": outcome}) + "\n"
    return headers, body


app = Flask(__name__)


@app.route("/", methods=["GET"])
@decop.responses({200: response, 403: response})
@decop.intent(intent)
def index():
    pass
```

## Detailed Usage

See [app.py](https://github.com/iwamot/flask-decop/blob/master/app.py).

## Installation

`$ pip install flask-decop`

## Contribution

Create new Pull Request.

## License

[MIT](https://opensource.org/licenses/MIT)
