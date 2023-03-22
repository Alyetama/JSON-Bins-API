# JSON Bin API

This is a simple Flask API that provides endpoints to create, read, update, and delete JSON bins in a SQLite database. Each bin is identified by a unique ID, and contains a JSON object.


## Installation

To install and run the JSON Bin API, follow these steps:

1. Clone this repository:
```bash
git clone https://github.com/example/json-bin-api.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Start the API server:

```bash
python app.py
```

The API server should now be running at http://localhost:5000.

## Usage
### Creating a Bin

To create a new JSON bin, send a POST request to the /bins endpoint with a JSON payload that contains a name field and a json field:

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"name": "mybin", "json": {"foo": "bar"}}' http://localhost:5000/bins
{"id": "ZUO_MupYIZgn"}
```

This will create a new bin with a unique ID and the given name and JSON object.

### Retrieving a Bin

To retrieve the JSON object from a bin by its ID, send a GET request to the `/bins/<bin_id>` endpoint:

```bash
$ curl http://localhost:5000/bins/ZUO_MupYIZgn
{"foo": "bar"}
```

This will return the JSON object as a string.


### Updating a Bin

To update the JSON object in a bin by its ID, send a PUT request to the `/bins/<bin_id>` endpoint with a JSON payload that contains a json field:

```bash
$ curl -X PUT -H "Content-Type: application/json" -d '{"json": {"foo": "baz"}}' http://localhost:5000/bins/ZUO_MupYIZgn
```

This will update the JSON object in the bin with the new object.


### Deleting a Bin

To delete a bin by its ID, send a DELETE request to the `/bins/<bin_id>` endpoint:

```bash
$ curl -X DELETE http://localhost:5000/bins/ZUO_MupYIZgn
```

This will delete the bin with the given ID.
