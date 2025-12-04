# middleware.py
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.utils.deprecation import MiddlewareMixin


class Custom404Middleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            response_html = render_to_string("404.html")
            return HttpResponse(response_html, status=404)
        return None
