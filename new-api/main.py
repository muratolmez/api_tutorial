
import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote
from google.appengine.ext import ndb
import httplib


api_collection = endpoints.api(name='mobile', version='v1.0')



class User(messages.Message):
    auth_id = messages.StringField(1)

class UserModel(ndb.Model):
    auth_id = ndb.StringProperty()



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
           ).put()

        return Response(ok=httplib.OK)

@api_collection.api_class(resource_name='UserTransactions')
class UserGet(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        # The request body should be empty.
        message_types.VoidMessage,
        # Accept one url parameter: an integer named 'id'
        auth_id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, UserList,
                      name='user_get',
                      path='user_get/{auth_id}',
                      http_method='GET')
    def user_get(self,request):
        q = UserModel.query(UserModel.auth_id == request.auth_id).fetch()

        a = User()
        a.auth_id = q[0].auth_id
        return UserList(users=a)



"""
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

"""




api = endpoints.api_server([UserInsert,UserGet])
