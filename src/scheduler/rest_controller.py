"""REST Controller

Here you'll find handlers for RESTful API, which is meant to be stateless
"""

from scheduler.utils import routes

from scheduler.view import BaseRESTController


@routes("/api/", name="api")
class ApiHandler(BaseRESTController):
    """API Handler"""
    pass

@routes('/api/user/', name="user_api")
class UserApiHandler(BaseRESTController):
    """Register"""
    def post(self):
        self._return({'result': 'success'})

@routes('/api/auth/', name="auth_api")
class AuthApiHandler(BaseRESTController):
    def post(self):
        """Login"""
        self._return({'result': 'success'})  # or error
    def delete(self):
        """Logout"""
        self._return({'result': 'success'})  # or error

@routes('/api/university/', name="univ_api")
class UniversityApiHandler(BaseRESTController):
    def post(self):
        """Create"""
        self._return({'id': 1})  # or some other int, otherwise - error
    def get(self):
        """Autocomplete"""
        self._return([{'id': 1, 'name': 'National University of Ukraine \'Kyiv Polytechnic Institute\''}, {'id': 3, 'name': 'National University of Georgia'}])  # or error

@routes('/api/group/', name="group_api")
class GroupApiHandler(BaseRESTController):
    def post(self):
        """Create"""
        self._return({'id': 1})  # or some other int, otherwise - error
    def get(self):
        """Autocomplete"""
        self._return([{'id': 1, 'name': 'IO-31m'}, {'id': 3, 'name': 'IK-32s'}])  # or error

@routes('/api/class/', name="class_api")
class ClassApiHandler(BaseRESTController):
    def post(self):
        """Create"""
        self._return({'id': 1})  # or some other int, otherwise - error

@routes('/api/timetable/', name="sched_api")
class TimetableApiHandler(BaseRESTController):
    def get(self):
        """Create"""
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
class GroupApiHandler(BaseRESTController):
    def post(self):
        """Post"""
        self._return({
                        'user_name': 'webknjaz',
                        #'user_picture_url': '',
                        'text': 'ololo',
                        'time': '08:00',
                    })  # or some other int, otherwise - error

    def get(self):
        """Get lesson messages"""
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
