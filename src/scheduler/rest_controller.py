"""REST Controller

Here you'll find handlers for RESTful API, which is meant to be stateless
"""

from scheduler.utils import routes

from scheduler.view import JSONHandler


@routes("/api/", name="api")
class ApiHandler(JSONHandler):
    """API Handler"""
    def get(self):
        resp = {}
        self._return(resp)
