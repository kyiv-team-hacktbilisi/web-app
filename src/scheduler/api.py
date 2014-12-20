"""API

This module contains functions to interact with different system entities
"""

from scheduler.model import *

def create_user(writer, **kwargs):
    student = User(**kwargs)
    student.save(writer)

def handle_user_saved(user):
    return user

        #authenticate_user(**kwargs):
        #logout_user(**kwargs):
        #create_university(**kwargs):
        #get_universities(**kwargs):
        #create_group(**kwargs)
        #get_groups(**kwargs)
        #create_class(**kwargs)
        #create_timetable(**kwargs)
        #create_comment(**kwargs)
