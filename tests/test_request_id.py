from flask_request_id import RequestID
import pytest
from flask import Flask, Response, request


@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route("/")
    def route():
        return Response(request.environ.get("FLASK_REQUEST_ID"), 200)

    return app


@pytest.fixture
def client(app):
    return app.test_client()


def _custom_generator():
    return "test-request-id"


def test_req_id_default(app, client):
    RequestID(app)
    r = client.get("/")
    assert r.status_code == 200
    assert r.headers['X-Request-ID']
    assert r.data.decode("utf-8") == r.headers['X-Request-ID']


def test_req_id_custom_header_name(app, client):
    RequestID(app, header_name="App-Request-ID")
    r = client.get("/")
    assert r.status_code == 200
    assert r.headers['App-Request-ID']
    assert r.data.decode("utf-8") == r.headers['App-Request-ID']


def test_req_id_custom_generator(app, client):
    RequestID(app, header_name="App-Request-ID", generator_func=_custom_generator)
    r = client.get("/")
    assert r.status_code == 200
    assert r.headers['App-Request-ID'] == "test-request-id"
    assert r.data.decode("utf-8") == "test-request-id"


def test_req_id_passthrough(app, client):
    RequestID(app)
    request_id = "test-request-id2"
    r = client.get("/", headers={'X-Request-ID': request_id})
    assert r.status_code == 200
    assert r.headers['X-Request-ID'] == request_id
    assert r.data.decode("utf-8") == request_id
