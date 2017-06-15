import uuid


def _request_id_from_uuid():
    return str(uuid.uuid4())


class RequestID(object):
    def __init__(self, app, header_name="X-Request-ID", generator_func=_request_id_from_uuid):
        """
        Adds the Request ID middleware to your current app
        :param app: Flask APP
        :param header_name: The header name returned, X-Request-ID by default
        :type header_name: string
        :param generator_func: Generator function, returning a string. By default, will generate an uuid v4
        :type generator_func: func
        """
        # Use wsgi_app
        self.app = app.wsgi_app
        self._header_name = header_name
        self._flask_header_name = header_name.upper().replace("-", "_")
        self._generator_func = generator_func
        # Change your app wsgi_app
        app.wsgi_app = self

    def __call__(self, environ, start_response):
        header_key = "HTTP_{0}".format(self._flask_header_name)
        environ.setdefault(header_key, self._generator_func())
        req_id = environ[header_key]
        environ["FLASK_REQUEST_ID"] = req_id

        def new_start_response(status, response_headers, exc_info=None):
            response_headers.append((self._header_name, req_id))
            return start_response(status, response_headers, exc_info)

        return self.app(environ, new_start_response)
