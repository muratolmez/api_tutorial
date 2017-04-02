
import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote
from google.appengine.ext import ndb
import httplib


api_collection = endpoints.api(name='mobile', version='v1.0')



class User(messages.Message):
    auth_id = messages.StringField(1)
    user_name = messages.StringField(2)
    user_surname = messages.StringField(3)
    user_email = messages.StringField(4)
    user_city = messages.StringField(5)
    user_gender = messages.StringField(6)
    user_phone = messages.IntegerField(7)
    user_birthday = messages.StringField(8)
    user_created_date=messages.IntegerField(9)
    user_rank = messages.IntegerField(10)

class UserModel(ndb.Model):
    auth_id = ndb.StringProperty()
    user_name = ndb.StringProperty()
    user_surname = ndb.StringProperty()
    user_email = ndb.StringProperty()
    user_city = ndb.StringProperty()
    user_gender = ndb.StringProperty()
    user_phone = ndb.IntegerProperty()
    user_birthday = ndb.StringProperty()
    user_created_date=ndb.IntegerProperty()
    user_rank=ndb.IntegerProperty()



class UserList(messages.Message):
    users = messages.MessageField(User, 1)


class Response(messages.Message):
    ok = messages.IntegerField(1)



@api_collection.api_class(resource_name='UserTransactions')
class UserInsert(remote.Service):
    @endpoints.method(User, Response,
                      name='user_put',
                      path='user_put',
                      http_method='POST')
    
    def user_insert(self, request):
        UserModel(auth_id=request.auth_id,
                  user_name= request.user_name,
                  user_surname = request.user_surname,
                  user_email= request.user_email,
                  user_city= request.user_city,
                  user_gender= request.user_gender,
                  user_phone= request.user_phone,
                  user_birthday= request.user_birthday,
                  user_created_date = request.user_created_date,
                  user_rank = request.user_rank
           ).put()

        return Response(ok=httplib.OK)

@api_collection.api_class(resource_name='UserTransactions')
class UserGet(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        # The request body should be empty.
        message_types.VoidMessage,
        # Accept one url parameter: an integer named 'id'
        auth_id=messages.StringField(1),
        user_name = messages.StringField(2),
        user_surname = messages.StringField(3),
        user_email = messages.StringField(4),
        user_city = messages.StringField(5),
        user_gender = messages.StringField(6),
        user_phone = messages.IntegerField(7),
        user_birthday = messages.StringField(8),
        user_created_date=messages.IntegerField(9),
        user_rank = messages.IntegerField(10))

    @endpoints.method(GET_RESOURCE, UserList,
                      name='user_get',
                      path='user_get/{auth_id}',
                      http_method='GET')
    def user_get(self,request):
        q = UserModel.query(UserModel.auth_id == request.auth_id).fetch()

        a = User()
        a.auth_id = q[0].auth_id
        a.user_name=q[0].user_name;
        a.user_surname=q[0].user_surname;
        a.user_mail=q[0].user_mail;
        a.user_city=q[0].user_city;
        a.user_gender=q[0].user_gender;
        a.user_phone=q[0].user_phone;
        a.user_birthday=q[0].user_birthday;
        a.user_created_date=q[0].user_created_date;
        a.user_rank=q[0].user_rank;
        return UserList(users=a)




@api_collection.api_class(resource_name='UserTransactions')
class UserUpdate(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        # The request body should be empty.
        User,
        # Accept one url parameter: an integer named 'id'
        auth_id=messages.StringField(1))



    @endpoints.method(User, Response,
                      name='user_update',
                      path='user_update/{auth_id}',
                      http_method='POST')
    def user_update(self, request):

        UserModel(auth_id=request.auth_id).put()

        q = UserModel.query(UserModel.auth_id == request.auth_id).fetch()

        return Response(ok = httplib.OK)

                             
class UserRemove(remote.Service):
    @endpoints.method(User, Response,
                      name='user_insert',
                      path='user_insert',
                      http_method='POST')
    def user_insert(self, request):

        UserModel(auth_id=request.auth_id,
           ).put()

        return Response(ok = httplib.OK)






api = endpoints.api_server([UserInsert,UserGet])
