import endpoints
from protorpc import messages, message_types
from protorpc import remote
from time import time

import httplib

from google.appengine.ext import ndb

class Ad(messages.Message):
    ad_title = messages.StringField(1,required = True)
    ad_owner = messages.StringField(2,required = True)
    ad_info = messages.StringField(3,required = True)
    ad_cost = messages.IntegerField(4,required = True)
    ad_city = messages.StringField(5,required = True)
    ad_ilce = messages.StringField(6,required = True)
    ad_created_date= message_types.DateTimeField(7)
    ad_start_date=message_types.DateTimeField(8,required=True)
    ad_finish_date=message_types.DateTimeField(9,required = True)
    ad_status = messages.BooleanField(10)

class AdModel(ndb.Model):
    ad_title = ndb.StringProperty()
    ad_owner = ndb.StringProperty(required = True)
    ad_info = ndb.StringProperty(required = True)
    ad_cost = ndb.IntegerProperty(required = True)
    ad_city = ndb.StringProperty(required = True)
    ad_ilce = ndb.StringProperty(required = True)
    ad_created_date = ndb.DateTimeProperty()
    ad_start_date = ndb.DateTimeProperty(required = True)
    ad_finish_date = ndb.DateTimeProperty(required = True)
    ad_status=ndb.BooleanProperty(required = True)
    
class AdList(messages.Message):
    ads = messages.MessageField(Ad,1,repeated = True)


class Response(messages.Message):
    ok = messages.IntegerField(1)



@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertInsert(remote.Service):
    @endpoints.method(Ad, Response,
                      name='advert_put',
                      path='advert_put',
                      http_method='POST')
    
    def advert_insert(self, request):
        
        AdModel(ad_title=request.ad_title,
                  ad_owner=request.ad_owner,
                  ad_info=request.ad_info,
                  ad_cost=request.ad_cost,
                  ad_city=request.ad_city,
                  ad_ilce=request.ad_ilce,
                  ad_created_date=request.ad_created_date,
                  ad_start_date=request.ad_start_date,
                  ad_finish_date=request.ad_finish_date,
                  ad_status=request.ad_status,
                  
           ).put()

        return Response(ok=httplib.OK)
    

@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertGet(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        # The request body should be empty.
        message_types.VoidMessage,
        # Accept one url parameter: an integer named 'id'
    ad_title = messages.StringField(1,required = True),
    ad_owner = messages.StringField(2,required = True),
    ad_info = messages.StringField(3,required = True),
    ad_cost = messages.IntegerField(4,required = True),
    ad_city = messages.StringField(5,required = True),
    ad_ilce = messages.StringField(6,required = True),
    ad_created_date= message_types.DateTimeField(7),
    ad_start_date=message_types.DateTimeField(8,required=True),
    ad_finish_date=message_types.DateTimeField(9,required = True),
    ad_status = messages.BooleanField(10))

    @endpoints.method(GET_RESOURCE, AdList,
                      name='advert_get',
                      path='advert_get/{advert.id()}',
                      http_method='GET')
    def ad_get(self,request):
        q = AdModel.query(AdModel.id == request.id()).fetch()

        a = Ad()
        a.ad_title = q[0].ad_title;
        a.ad_owner=q[0].ad_owner;
        a.ad_info=q[0].ad_info;
        a.ad_cost=q[0].ad_cost;
        a.ad_city=q[0].ad_city;
        a.ad_ilce=q[0].ad_ilce;
        a.ad_created_date=q[0].ad_created_date;
        a.ad_start_date=q[0].ad_start_date;
        a.ad_finish_date=q[0].ad_finish_date;
        a.ad_status=q[0].ad_status;
        return AdList(ads=a)


api = endpoints.api_server([AdvertInsert,AdvertGet])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    