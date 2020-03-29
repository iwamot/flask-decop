from flask import Flask
from flask_decop import decop
from sample_app import intents, responses

app = Flask(__name__, static_folder="htmlcov")


@app.route("/dogs", methods=["GET"])
@decop.responses({200: responses.list_dogs})
@decop.intent(intents.list_dogs)
def list_dogs():
    pass


# Intent can receive path values
@app.route("/dogs/<int:dog_id>", methods=["POST"])
@decop.responses({200: responses.greet_dog, 400: responses.bad_request})
@decop.intent(intents.greet_dog)
def greet_dog(dog_id):
    pass


# Intent can be omitted for static responses
@app.route("/", methods=["GET"])
@decop.responses({301: responses.dogs_location})
def static_response():
    pass


# Response can return an iterable body
@app.route("/iterable", methods=["GET"])
@decop.responses({200: responses.iterable})
def iterable():
    pass


# 500 error will be raised when no response found
@app.route("/misconfiguration", methods=["GET"])
@decop.responses({})
def no_responses():
    pass


@app.errorhandler(404)
@decop.responses({404: responses.not_found})
def not_found(error):
    pass


@app.errorhandler(405)
@decop.responses({405: responses.method_not_allowed})
def method_not_allowed(error):
    pass


@app.errorhandler(500)
@decop.responses({500: responses.internal_server_error})
def internal_server_error(error):
    pass
