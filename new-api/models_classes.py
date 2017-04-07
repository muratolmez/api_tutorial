from google.appengine.ext import ndb


class UserModel(ndb.Model):
    auth_id = ndb.StringProperty()
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    email = ndb.StringProperty()
    city = ndb.StringProperty()
    phone = ndb.IntegerProperty()
    birthday = ndb.StringProperty()
    created_date = ndb.DateProperty(auto_now_add=True)
    rank = ndb.IntegerProperty()


class AdvertModel(ndb.Model):
    title = ndb.StringProperty()
    owner = ndb.StringProperty()
    info = ndb.StringProperty()
    cost = ndb.IntegerProperty()
    city = ndb.StringProperty()
    district = ndb.StringProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    start_date = ndb.DateTimeProperty()
    finish_date = ndb.DateTimeProperty()
    status = ndb.BooleanProperty()
