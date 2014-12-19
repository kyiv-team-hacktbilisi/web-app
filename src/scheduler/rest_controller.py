"""REST Controller

Here you'll find handlers for RESTful API, which is meant to be stateless
"""

from scheduler.view import JSONHandler


class ApiHandler(JSONHandler):
    """API Handler"""
    def get(self):
        resp = {}
        self._return(resp)
