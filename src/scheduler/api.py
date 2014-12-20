"""API

This module contains functions to interact with different system entities
"""

from scheduler.model import *

def create_user(**kwargs):
    student = User(**kwargs)
    student.save(handle_user_saved)

def handle_user_saved(user):
    return user
