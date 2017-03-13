import endpoints
from protorpc import messages, message_types
from protorpc import remote
from google.appengine.ext import ndb
from google.appengine.datastore.datastore_v4_pb import GqlQuery
import logging
from google.appengine._internal.django.core.mail.backends import console


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class User(messages.Message):
    user_auth_id = messages.StringField(1)
    user_name = messages.StringField(2,required = True)
    user_surname = messages.StringField(3,required = True)
    user_email = messages.StringField(4,required = True)
    user_city = messages.StringField(5,required = True)
    user_gender = messages.StringField(6,required = True)
    user_phone = messages.IntegerField(7,required = True)
    user_birthday = messages.StringField(8,required = True)
    user_created_date=messages.IntegerField(9)
    user_rank = messages.IntegerField(10)
    
  
class aluser(messages.Message):
    auth_id = messages.StringField(1)
  
  
    
        
class UserModel(ndb.Model):
    user_auth_id = ndb.StringProperty()
    user_name = ndb.StringProperty(required = True)
    user_surname = ndb.StringProperty(required = True)
    user_email = ndb.StringProperty(required = True)
    user_city = ndb.StringProperty(required = True)
    user_gender = ndb.StringProperty(required = True)
    user_phone = ndb.IntegerProperty(required = True)
    user_birthday = ndb.StringProperty(required = True)
    user_created_date=ndb.IntegerProperty(required = True)
    user_rank=ndb.IntegerProperty()

class UserList(messages.Message):
    users = messages.MessageField(User,1,repeated = True)
        



@endpoints.api(name = 'userProfile', version='vGDL',
               description='API For User')

class User_Api(remote.Service):

    @endpoints.method(User,User,
                      name='user.insert',
                      path='user_insert',
                      http_method= 'POST')
     
    def user_insert(self,request):
        UserModel(user_auth_id= request.user_auth_id,
                  user_name= request.user_name,
                  user_surname = request.user_surname,
                  user_email= request.user_email,
                  user_city= request.user_city,
                  user_gender= request.user_gender,
                  user_phone= request.user_phone,
                  user_birthday= request.user_birthday,
                  user_created_date = request.user_created_date,
                  user_rank = request.user_rank).put()
        return request
    @endpoints.method(message_types.VoidMessage,UserList,
                      name='user.list',
                      path= 'user_list',
                      http_method='GET')
    def user_list(self,unused_request):
        users_list = []
        for user in UserModel.query():
            users_list.append(User(user_auth_id= user.user_auth_id,
                  user_name= user.user_name,
                  user_surname = user.user_surname,
                  user_email= user.user_email,
                  user_city= user.user_city,
                  user_gender= user.user_gender,
                  user_phone= user.user_phone,
                  user_birthday= user.user_birthday,
                  user_created_date= user.user_created_date, 
                  user_rank=user.user_rank))
        
        return UserList(users=users_list)
        
    
    @endpoints.method(aluser,User,
        name='user.al',
        path= 'user_al',
        http_method='POST'
                     )
    def user_json(self,request):
        
        q = UserModel.gql("WHERE user_auth_id = '12'")
        for user in q:
            #print user.user_auth_id

            usera = User(user.user_auth_id,
                         user.user_name,
                         user.user_surname,
                         user.user_email,
                         user.user_city, 
                         user.user_gender,
                         user.user_phone,
                         user.user_birthday,
                         user.user_created_date,
                         user.user_rank) 
        
        return usera


api = endpoints.api_server([User_Api])
