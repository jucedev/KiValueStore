from flask import Flask, request

# 1. setup http server
api = Flask(__name__)

# 2. setup a global store for key value pairs
key_value_pairs = {}


# requirement 1: store key value pairs
# HTTP POST: /api/data/{key:alphanumeric}
#   - key: string, any length
#   - value: string, any length
#   - if key already exists => decline: 409 Conflict

@api.route("/api/data/<key>", methods=["POST"])
def post_key_value_pair(key):
    if key in key_value_pairs:
        return 'key exists', 409
    key_value_pairs[key] = request.data
    return 'value set', 201


# requirement 2: retrieve value by key
# HTTP GET: /api/data/{key:alphanumeric}
#   - if key exists => return value: as string
#   - if key does not exist => error: 404 NotFound

@api.route("/api/data/<key>", methods=["GET"])
def get_value_by_key(key):
    if key not in key_value_pairs:
        return 'key does not exist', 404
    return key_value_pairs[key], 200


# requirement 3: delete key value pairs by key
# HTTP DELETE: /api/data/{key:alphanumeric}
#   - if key exists => delete key value pair
#   - if key does not exist => error: 404 NotFound

@api.route("/api/data/<key>", methods=["DELETE"])
def delete_key_value_pair(key):
    if key not in key_value_pairs:
        return 'key does not exist', 404
    del key_value_pairs[key]
    return 'key value pair deleted', 200


# requirement 4: check if a key is present
# HTTP GET: /api/keys/{key:alphanumeric}
#   - if key exists => 200
#   - if key does not exist => error: 404 NotFound

@api.route("/api/keys/<key>", methods=["GET"])
def is_key_present(key):
    if key not in key_value_pairs:
        return 'key does not exist', 404
    return 'key exists', 200


if __name__ == '__main__':
    api.run()

