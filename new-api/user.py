from protorpc import message_types
from protorpc import messages
from google.appengine.ext import ndb


class UserMessage(messages.Message):
    def __init__(self):
        messages.Message.__init__(self)
        self.UID = messages.StringField(1, required=True)
        self.name = messages.StringField(2, required=True)
        self.surname = messages.StringField(3, required=True)
        self.email = messages.StringField(4, required=True)
        self.city = messages.StringField(5, required=True)
        self.gender = messages.StringField(6, required=True)
        self.phone = messages.IntegerField(7, required=True)
        self.birthday = message_types.DateTimeField(8, required=True)



class UserModel(ndb.Model):
    def __init__(self):
        ndb.Model.__init__(self)
        self.UID = ndb.StringProperty()
        self.name = ndb.StringProperty()
        self.surname = ndb.StringProperty()
        self.email = ndb.StringProperty()
        self.city = ndb.StringProperty()
        self.gender = ndb.StringProperty()
        self.phone = ndb.IntegerProperty()
        self.birthday = ndb.DateTimeProperty()
        self.flag = ndb.BooleanProperty()
