"""Model

This module descibes DB models/entities implementation
"""


import calendar
import os
from base64 import b64decode, b64encode
from datetime import datetime, timedelta
from hashlib import sha256

from motorengine import Document, StringField, EmailField, DateTimeField, \
                        IntField, \
                        ReferenceField, ListField, EmbeddedDocumentField

from sqlalchemy.ext.hybrid import hybrid_property


__all__ = [
            "University", "Group", "User",
            "Schedule", "DayTimetable",
            "Lesson", "Comment"
            ]


class User(Document):
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    id = IntField()
    email = EmailField()

    _salt = StringField(12)
    # 64 is the length of the SHA-256 encoded string length
    _password = StringField(64)

    group = ReferenceField('Group')
    timetable = EmbeddedDocumentField('Schedule')

    @hybrid_property
    def salt(self):
        """Generates a cryptographically random salt and sets its Base64 encoded
        version to the salt column, and returns the encoded salt.
        """
        if not self.id and not self._salt:
            self._salt = b64encode(os.urandom(8))

        if isinstance(self._salt, str):
            self._salt = self._salt.encode('UTF-8')

        return self._salt

    def __encrypt_password(self, password, salt):
        """
        Encrypts the password with the given salt using SHA-256. The salt must
        be cryptographically random bytes.

        :param password: the password that was provided by the user to try and
                         authenticate. This is the clear text version that we
                         will need to match against the encrypted one in the
                         database.
        :type password: basestring

        :param salt: the salt is used to strengthen the supplied password
                     against dictionary attacks.
        :type salt: an 8-byte long cryptographically random byte string
        """

        if isinstance(password, str):
            password_bytes = password.encode("UTF-8")
        else:
            password_bytes = password

        hashed_password = sha256()
        hashed_password.update(password_bytes)
        hashed_password.update(salt)
        hashed_password = hashed_password.hexdigest()

        if not isinstance(hashed_password, str):
            hashed_password = hashed_password.decode("UTF-8")

        return hashed_password

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = self.__encrypt_password(password,
                                                 b64decode(str(self.salt)))

    def validate_password(self, password):
        """Check the password against existing credentials.

        :type password: str
        :param password: clear text password
        :rtype: bool
        """
        return self.password == self.__encrypt_password(password,
                                                        b64decode(str(self.salt)))


class Comment(Document):
    user = ReferenceField(reference_document_type=User)
    lesson = ReferenceField('Lesson')
    #user_picture_url
    text = StringField(required=True)
    time = DateTimeField()


class Lesson(Document):
    id = IntField()
    comments = ListField(EmbeddedDocumentField(embedded_document_type=Comment))
    day = ReferenceField('DayTimetable')


class DayTimetable(Document):
    name = StringField(required=True)
    lessons = ListField(EmbeddedDocumentField(Lesson()))
    schedule = ReferenceField('Schedule')


class Schedule(Document):
    days = ListField(EmbeddedDocumentField(DayTimetable()))
    user = ReferenceField(reference_document_type=User)
    group = ReferenceField('Group')
    pass


class Group(Document):
    id = IntField()
    name = StringField(required=True)
    users = ListField(ReferenceField('User'))
    university = ReferenceField('University')
    timetable = EmbeddedDocumentField(Schedule())


class University(Document):
    id = IntField()
    name = StringField(required=True)
    groups = ListField(EmbeddedDocumentField(Group()))
