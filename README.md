# flask-decop

Flask extension to write decorator-based apps.

## Description

This extension has two purposes:

* Allow users to focus on writing of the application logic.
* Improve the portability of the application code.

It contains two decorators, `@decop.intent` and `@decop.responses`.

* `@decop.intent(callable)`
    * `callable`: Receive `flask.request`. Return `status_code` and `outcome`.
* `@decop.responses({status_code: callable, ...})`
    * `callable`: Receive `flask.request` and `outcome`. Return `headers` and `body`.

flask-decop will choose an appropriate response by `status_code`.

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

## Installation

`$ pip install flask-decop`

## Contribution

Create new Pull Request.

## License

[MIT](https://opensource.org/licenses/MIT)
