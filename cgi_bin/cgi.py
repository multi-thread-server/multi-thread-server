from http import HttpRequest, HttpResponse
import os

def build_cgi_environ(http_request):
    url_parts = http_request.get_url().split('?')
    return {
        'REQUEST_METHOD': http_request.get_method(),
        'PATH_INFO': url_parts[0],
        'QUERY_STRING': '' if len(url_parts) < 2 else url_parts[1],
        'SERVER_NAME': '127.0.0.1',
        'SERVER_PORT': '8888',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'HTTP_VERSION': http_request.get_version(),
        'CONTENT_TYPE': http_request.get_content_type(),
        'CONTENT_LENGTH': http_request.get_content_length(),
        'CONTENT': http_request.get_content(),
        **http_request.get_headers()
    }

app_registry = {}

def register_app(path, method):
    def app_decorator(app):
        if path not in app_registry:
            app_registry[path] = {}
        app_registry[path][method] = app
        return app
    return app_decorator

def method_get(path):
    return register_app(path, 'GET')

def method_post(path):
    return register_app(path, 'POST')

def default_app(cgi_environ):
    path = cgi_environ['PATH_INFO']
    try:
        with open(os.getcwd() + path, 'r') as f:
            return '200 OK', 'text/html', f.read()
    except:
        with open(os.getcwd() + '/404.html', 'r') as f:
            content = f.read()
        return '404 NOT-FOUND', 'text/html', content

def lookup_app(path, method):
    if path in app_registry and method in app_registry[path]:
        return app_registry[path][method]
    return default_app

def cgi(http_request):
    cgi_environ = build_cgi_environ(http_request)
    path = cgi_environ['PATH_INFO']
    method = cgi_environ['REQUEST_METHOD']
    app = lookup_app(path, method)
    status, content_type, content = app(cgi_environ)
    return HttpResponse(status, content_type, content)
