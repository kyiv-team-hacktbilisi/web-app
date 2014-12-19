"""View

This module contains mixins and helper functions/decorators
for content rendering
"""

import json
import tornado

import os
import tornado.web
from jinja2 import Environment as Jinja2Environment, FileSystemLoader, TemplateNotFound

from webassets import Environment as AssetsEnvironment
from webassets.ext.jinja2 import AssetsExtension


class TemplateRendering:
    """
    A simple class to hold methods for rendering templates.
    """

    def render_template(self, template_name, **kwargs):
        """templates rendering itself
        """
        try:
            template = self.settings['jinja2_env'].get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        content = template.render(kwargs)
        return content

    def _render(self, template_name, **kwargs):
        """
        This is for making some extra context variables available to
        the template
        """
        kwargs.update({
            'settings': self.settings,
            'STATIC_URL': self.settings.get('static_url_prefix', '/static/'),
            'request': self.request,
            'xsrf_token': self.xsrf_token,
            'xsrf_form_html': self.xsrf_form_html,
        })

        if self.current_user is not None:
            kwargs['current_user'] = tornado.escape.xhtml_escape(self.current_user)

        content = self.render_template(template_name, **kwargs)
        self.write(content)


class BaseHandler(tornado.web.RequestHandler, TemplateRendering):
    """Basic Handler

    RequestHandler already has a `render()` method. I'm writing another
    method `_return()` and keeping the API almost same.
    """

    def _return(self, template_name, **kwargs):
        """
        This is for making some extra context variables available to
        the template
        """
        self._render(template_name, **kwargs)
        self.finish()

    def get_current_user(self):
        return self.get_secure_cookie("user")


class JSONHandler(tornado.web.RequestHandler):
    """Handler with JSON output"""
    def _return(self, obj):
        self.set_header("Content-Type", "application/json")
        json.dump(obj, self)
        self.finish()
