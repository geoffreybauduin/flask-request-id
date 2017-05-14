# Flask Request ID
[![Build Status](https://travis-ci.org/geoffreybauduin/flask-request-id.svg?branch=master)](https://travis-ci.org/geoffreybauduin/flask-request-id)

A simple request id middleware for Flask.

`pip install flask-request-id-middleware`

## How to use it ?

```python
from flask import Flask
from flask_request_id import RequestID

def init_app():
    app = Flask(app)
    RequestID(app)
    return app
```

All your HTTP requests will include a header named (by default) "X-Request-ID" inside their responses.

## How can I retrieve this Request ID ?

```python
def _get_request_id():
    return request.environ.get("FLASK_REQUEST_ID")
```

# Contributing

Feel free to open a PR or an issue if you feel like discussing about something.

To launch unit tests:

`tox`

# License

MIT License

Copyright (c) 2017 Geoffrey Bauduin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
