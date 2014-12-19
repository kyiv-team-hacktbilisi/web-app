#! /usr/bin/env python
"""Student Scheduler

This app implements web service for students
"""

import yaml

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.options
import tornado.autoreload
from tornado.options import define, options

from jinja2 import Environment as Jinja2Environment, FileSystemLoader, TemplateNotFound

from webassets import Environment as AssetsEnvironment
from webassets.ext.jinja2 import AssetsExtension


import os
import sys

from scheduler import SRC_DIR, PRJ_ROOT, __config__

from scheduler.controller import MainHandler, UserPortfolioHandler, \
    LoginHandler, AuthLogoutHandler, \
    GoogleOAuth2LoginHandler as GoogleLoginHandler, \
    FacebookGraphLoginHandler as FacebookLoginHandler, \
    TwitterLoginHandler
from scheduler.rest_controller import ApiHandler

define('version', default='dev', help='Version settings (default: dev)')

class App(tornado.web.Application):
    """Main Tornado app"""
    def __init__(self, settings):
        handlers = [
            tornado.web.URLSpec(r'/', MainHandler, name='home'),
            tornado.web.URLSpec(r'/api', ApiHandler, name='api'),
            tornado.web.URLSpec(r'/login/', LoginHandler, name='login'),
            tornado.web.URLSpec(r'/login/google', GoogleLoginHandler, name='login_google'),
            tornado.web.URLSpec(r'/login/facebook', FacebookLoginHandler, name='login_facebook'),
            tornado.web.URLSpec(r'/login/twitter', TwitterLoginHandler, name='login_twitter'),
            tornado.web.URLSpec(r'/logout', AuthLogoutHandler, name='logout'),
            tornado.web.URLSpec(r'/.*/portfolio', UserPortfolioHandler, name='portfolio'),
            #(r'/static/(.*)', tornado.web.StaticFileHandler,
            #                {'path': os.path.join(PRJ_ROOT, 'static')}),
        ]

        template_dirs = []
        jinja2_env = None

        if settings.get('template_path'):
            template_dirs.append(
                settings['template_path']
            )



        assets_env = AssetsEnvironment(settings['static_path'], '/static')
        settings['jinja2_env'] = Jinja2Environment(loader=FileSystemLoader(template_dirs),
                                       extensions=[AssetsExtension])
        settings['jinja2_env'].assets_environment = assets_env

        tornado.web.Application.__init__(
            self,
            handlers,
            **settings
        )


def wsgi():
    """wsgi app creator"""
    return main(is_wsgi=True)


def main(is_wsgi=False):
    """This function runs web server"""
    tornado.options.parse_command_line()

    config = None

    try:
        with open(
            os.path.join(
                PRJ_ROOT,
                'config',
                options.version,
                __config__
                ),
            'r'
            ) as f:
            config = yaml.load(f)
        if 'settings' in config:
            pass
    except IOError:
        print('Invalid or missing config file: {}'.format(__config__))
    # if no settings, we go away
    except KeyError:
        print('No default configuration found')
        sys.exit(1)
    except Exception as ex:
        print('Smth unexpected happened')
        raise ex

    settings = config['settings']

    config['port'] = os.getenv('PORT', config['port'])

    settings['app_uri'] = os.getenv('APP_URI', settings['app_uri'])

    settings['static_path'] = os.path.join(PRJ_ROOT,
                                           settings['static_path'])
    settings['template_path'] = os.path.join(SRC_DIR,
                                             settings['template_path'])

    settings['twitter_consumer_key'] = os.getenv('TWITTER_APP_ID',
                                            settings['twitter_consumer_key'])
    settings['twitter_consumer_secret'] = os.getenv('TWITTER_SECRET',
                                            settings['twitter_consumer_secret'])

    settings['facebook_api_key'] = os.getenv('FACEBOOK_APP_ID',
                                            settings['facebook_api_key'])
    settings['facebook_secret'] = os.getenv('FACEBOOK_SECRET',
                                            settings['facebook_secret'])

    settings['google_oauth'] = settings.get('google_oauth', {})
    settings['google_oauth'] = {
                                'key': os.getenv('GOOGLE_APP_ID',
                                        settings['google_oauth'].get('key')),
                                'secret': os.getenv('GOOGLE_SECRET',
                                        settings['google_oauth'].get('secret'))
                                }


    for k, v in settings.items():
        if k.upper() in os.environ:
            settings[k] = os.getenv(k.upper(), v)
        elif k.endswith('_path'):
            settings[k] = v.replace(
                '__path__',
                PRJ_ROOT
            )

    application = App(settings)
    if is_wsgi:
        return tornado.wsgi.WSGIAdapter(application)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(config['port'])

    if 'debug' in settings and settings['debug'] is True:
        #tornado.autoreload.watch(SRC_DIR)
        tornado.autoreload.watch(os.path.join(
                PRJ_ROOT,
                'config',
                options.version,
                __config__
                ))
        tornado.autoreload.watch(settings['template_path'])
        tornado.autoreload.watch(settings['static_path'])
        #tornado.autoreload.start(tornado.ioloop.IOLoop.instance())
        tornado.autoreload.start()

    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        sys.exit(0)

    #from tornado.platform.asyncio import AsyncIOMainLoop
    #import asyncio
    #AsyncIOMainLoop().install()
    #asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()
