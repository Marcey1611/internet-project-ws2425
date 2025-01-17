from enum import Enum

class HttpStatus(Enum):
    OK = "200 OK"
    CREATED = "201 Created"
    BAD_REQUEST = "400 Bad Request"
    NOT_FOUND = "404 Not Found"
    METHOD_NOT_ALLOWED = "405 Method Not Allowed"
    NOT_ACCEPTABLE = "406 Not Acceptable"
    UNSUPPORTED_MEDIA_TYPE = "415 Unsupported Media Type"
    UNPROCESSABLE_ENTITY = "422 Unprocessable Entity"
    INTERNAL_SERVER_ERROR = "500 Internal Server Error"
    NOT_IMPLEMENTED = "501 Not Implemented"

class ContentType(Enum):
    PLAIN = "text/plain"
    JSON = "application/json"
    HTML = "text/html"
    XML = "application/xml"
    ALL = "*/*"

class Method(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
