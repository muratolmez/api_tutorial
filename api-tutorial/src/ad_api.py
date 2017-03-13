import endpoints
from protorpc import messages, message_types
from protorpc import remote

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
    ad_created_date = ndb.DateTimeProperty(required = True)
    ad_finish_date = ndb.DateTimeProperty(required = True)
    ad_status=ndb.BooleanProperty(required = True)
    
class AdList(messages.Message):
    ads = messages.MessageField(Ad,1,repeated = True)
    
@endpoints.api(name = 'adProfile', version='vGDL',
               description='API For Ad')    

class Ad_Api(remote.Service):
    @endpoints.method(Ad,Ad,
                      name='ad.insert',
                      path='ad_insert',
                      http_method= 'POST')
    
    def ad_insert(self,request):
        AdModel(
                  ad_title = request.ad_title,
                  ad_owner = request.ad_owner,
                  ad_info = request.info,
                  ad_cost = request.ad_cost,
                  ad_city = request.ad_city,
                  ad_ilce = request.ad_ilce,
                  ad_created_date = request.ad_created_date,
                  ad_start_date = request.ad_start_date,
                  ad_finish_date = request.ad_finish_date,
                  ad_status = request.ad_status).put()
        return request
    
    @endpoints.method(message_types.VoidMessage,AdList,
                      name='ad.list',
                      path= 'ad_list',
                      http_method='GET')
    
    def ad_list(self,unused_request):
        ads_list = []
        for ad in AdModel.query():
            ads_list.append(Ad(
                  ad_title = ad.ad_title,
                  ad_owner = ad.ad_owner,
                  ad_info = ad.info,
                  ad_cost = ad.ad_cost,
                  ad_city = ad.ad_city,
                  ad_ilce = ad.ad_ilce,
                  ad_created_date = ad.ad_created_date,
                  ad_start_date = ad.ad_start_date,
                  ad_finish_date = ad.ad_finish_date,
                  ad_status = ad.ad_status))
        
        return AdList(ads=ads_list)
    
api = endpoints.api_server([Ad_Api])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    