import urllib.parse
import time
from django.http import HttpResponse, HttpRequest

CACHE = {} # PATH => (Response, EXPIRE)

class CacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        path = urllib.parse.urlparse(request.path).path
        if path in CACHE and CACHE[path][1] > time.time():
            return CACHE[path][0]
        is_static = path.endswith(".css") or path.endswith(".js") or path.endswith(".html")
        response = self.get_response(request)
        if is_static:
            CACHE[path] = (response, time.time() + 100)
        print('Cache: ' + CACHE[path][0].content.decode('utf-8'))
        return response