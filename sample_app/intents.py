DOGS = {1: "Matthew", 2: "Mona"}


def list_dogs(request):
    return 200, [{"dog_id": dog_id, "name": name} for dog_id, name in DOGS.items()]


def greet_dog(request, dog_id):
    dog = DOGS.get(dog_id, None)
    if dog is None:
        return 404, None

    request_json = request.json
    if request_json is None:
        return (
            400,
            {"error": 'Post JSON like {"greet": "Hello!"} with application/json.'},
        )

    greet = request_json.get("greet", None)
    if greet is None:
        return 400, {"error": "JSON must have 'greet' key."}

    return 200, {dog: "Yelp!"}
