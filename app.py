import flask
from flask_decop import decop
from sample_app import intents, responses

app = flask.Flask(__name__, static_folder="htmlcov")


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
def not_found(error):
    return flask.jsonify({"error": "Not Found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return flask.jsonify({"error": "Method Not Allowed"}), 405


@app.errorhandler(500)
def internal_server_error(error):
    return flask.jsonify({"error": "Internal Server Error"}), 500
