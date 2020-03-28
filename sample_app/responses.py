import json


def list_dogs(request, outcome):
    return {"content-type": "application/json"}, json.dumps(outcome)


def greet_dog(request, outcome):
    return {"content-type": "application/json"}, json.dumps(outcome)


def bad_request(request, outcome):
    return {"content-type": "application/json"}, json.dumps(outcome)


def dogs_location(request, outcome):
    return {"location": "/dogs"}, ""


def iterable(request, outcome):
    def count5():
        for i in range(1, 6):
            yield str(i)

    return {"content-type": "text/plain"}, count5()
