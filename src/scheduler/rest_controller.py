"""REST Controller

Here you'll find handlers for RESTful API, which is meant to be stateless
"""

import tornado
from tornado.escape import json_decode

from scheduler.utils import routes

from scheduler.view import BaseRESTController

from scheduler.api import *


@routes("/api/", name="api")
class ApiHandler(BaseRESTController):
    """API Handler"""
    pass

@routes('/api/user/', name="user_api")
class UserApiHandler(BaseRESTController):
    """Register"""
    @tornado.web.asynchronous
    #@tornado.gen.coroutine
    def post(self):
        kwargs = json_decode(self.request.body)
        print(kwargs)
        create_user(self._return, **kwargs)
        #self._return({'result': 'success'})

@routes('/api/auth/', name="auth_api")
class AuthApiHandler(BaseRESTController):
    def post(self):
        """Login"""
        #authenticate_user(**kwargs)
        self._return({'result': 'success'})  # or error
    def delete(self):
        """Logout"""
        #logout_user(**kwargs)
        self._return({'result': 'success'})  # or error

@routes('/api/university/', name="univ_api")
class UniversityApiHandler(BaseRESTController):
    def post(self):
        """Create"""
        #create_university(**kwargs)
        self._return({'id': 1})  # or some other int, otherwise - error
    def get(self):
        """Autocomplete"""
        #get_universities(**kwargs)
        self._return([{'id': 1, 'name': 'National University of Ukraine \'Kyiv Polytechnic Institute\''}, {'id': 3, 'name': 'National University of Georgia'}])  # or error

@routes('/api/group/', name="group_api")
class GroupApiHandler(BaseRESTController):
    def post(self):
        """Create"""
        #create_group(**kwargs)
        self._return({'id': 1})  # or some other int, otherwise - error
    def get(self):
        """Autocomplete"""
        #get_groups(**kwargs)
        self._return([{'id': 1, 'name': 'IO-31m'}, {'id': 3, 'name': 'IK-32s'}])  # or error

@routes('/api/class/', name="class_api")
class ClassApiHandler(BaseRESTController):
    def post(self):
        """Create"""
        #create_class(**kwargs)
        self._return({'id': 1})  # or some other int, otherwise - error

@routes('/api/timetable/', name="sched_api")
class TimetableApiHandler(BaseRESTController):
    def get(self):
        """Create"""
        #create_timetable(**kwargs)
        self._return([
                        [
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                        ],
                        [
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                        ],
                        [
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                        ],
                        [
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                        ],
                        [
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                        ],
                        [
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                        ],
                        [
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                        ],
                        [
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                            {
                                'lesson_name': 'Computer science',
                                'audience': '418-18',
                                'teacher_name': 'Oleh Lisovychenko',
                                'type': 'lection',  # (lection\practice\laboratory)
                                'start_time': '08:30',
                                'color': '#ff0000',  # (hex)
                            },
                        ],
                    ])  # or some other int, otherwise - error

@routes('/api/comment/', name="comment_api")
class CommentApiHandler(BaseRESTController):
    def post(self):
        """Post"""
        #create_comment(**kwargs)
        self._return({
                        'user_name': 'webknjaz',
                        #'user_picture_url': '',
                        'text': 'ololo',
                        'time': '08:00',
                    })  # or some other int, otherwise - error

    def get(self):
        """Get lesson messages"""
        #get_comment_list(**kwargs)
        self._return([{
                        'user_name': 'webknjaz',
                        #'user_picture_url': '',
                        'text': 'ololo',
                        'time': '08:00',
                    },{
                        'user_name': 'webknjaz',
                        #'user_picture_url': '',
                        'text': 'ololo',
                        'time': '08:00',
                    },{
                        'user_name': 'webknjaz',
                        #'user_picture_url': '',
                        'text': 'ololo',
                        'time': '08:00',
                    },{
                        'user_name': 'webknjaz',
                        #'user_picture_url': '',
                        'text': 'ololo',
                        'time': '08:00',
                    },])  # or error
