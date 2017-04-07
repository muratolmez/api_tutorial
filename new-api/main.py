import endpoints
from protorpc import remote
from models_classes import *
from messages_classes import *
import datetime

api_collection = endpoints.api(name='mobile', version='v1.0')


@api_collection.api_class(resource_name='UserTransactions')
class UserPut(remote.Service):
    @endpoints.method(UserMessage, message_types.VoidMessage,
                      name='user_put',
                      path='user_put',
                      http_method='POST')
    def user_put(self, request):
        UserModel(auth_id=request.auth_id,
                  name=request.name,
                  surname=request.surname,
                  email=request.email,
                  city=request.city,
                  phone=request.phone,
                  birthday=request.birthday,
                  rank=request.rank
                  ).put()
        return message_types.VoidMessage()


@api_collection.api_class(resource_name='UserTransactions')
class UserGet(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        auth_id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, UserGetResponse,
                      name='user_get',
                      path='user_get/{auth_id}',
                      http_method='GET')
    def user_get(self, request):

        user_model = UserModel.query(UserModel.auth_id == request.auth_id).get()

        user_message = UserMessage()

        user_message.auth_id = user_model.auth_id
        user_message.name = user_model.name
        user_message.surname = user_model.surname
        user_message.mail = user_model.mail
        user_message.city = user_model.city
        user_message.gender = user_model.gender
        user_message.phone = user_model.phone
        user_message.birthday = user_model.birthday
        user_message.created_date = user_model.created_date
        user_message.rank = user_model.rank
        return UserGetResponse(user_get_response=user_message)


@api_collection.api_class(resource_name='UserTransactions')
class UserUpdateCity(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        UserMessageCity,
        auth_id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, message_types.VoidMessage,
                      name='user_update_city',
                      path='user_update_city/{auth_id}',
                      http_method='POST')
    def user_update_city(self, request):
        user_model = UserModel.query(UserModel.auth_id == request.auth_id).get()
        user_model.city = request.city
        user_model.put()
        return message_types.VoidMessage()


@api_collection.api_class(resource_name='UserTransactions')
class UserUpdateEmail(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        UserMessageEmail,
        auth_id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, message_types.VoidMessage,
                      name='user_update_email',
                      path='user_update_email/{auth_id}',
                      http_method='POST')
    def user_update_email(self, request):
        user_model = UserModel.query(UserModel.auth_id == request.auth_id).get()
        user_model.email = request.email
        user_model.put()
        return message_types.VoidMessage()


@api_collection.api_class(resource_name='UserTransactions')
class UserUpdatePhone(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        UserMessagePhone,
        auth_id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, message_types.VoidMessage,
                      name='user_update_phone',
                      path='user_update_phone/{auth_id}',
                      http_method='POST')
    def user_update_city(self, request):
        user_model = UserModel.query(UserModel.auth_id == request.auth_id).get()
        user_model.city = request.phone
        user_model.put()
        return message_types.VoidMessage()


@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertPut(remote.Service):
    @endpoints.method(AdvertMessage, message_types.VoidMessage,
                      name='advert_put',
                      path='advert_put',
                      http_method='POST')
    def advert_put(self, request):
        AdvertModel(title=request.title,
                    owner=request.owner,
                    info=request.info,
                    cost=request.cost,
                    city=request.city,
                    district=request.district,
                    start_date=request.start_date,
                    finish_date=request.finish_date,
                    status=request.ad_status,
                    ).put()

        return message_types.VoidMessage()


@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertGet(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, AdvertGetResponse,
                      name='advert_get',
                      path='advert_get/{id}',
                      http_method='GET')
    def advert_get(self, request):

        advert_model = AdvertModel.get_by_id(id=int(request.id))

        advert_message = AdvertMessage()
        advert_message.title = advert_model.title
        advert_message.owner = advert_model.owner
        advert_message.info = advert_model.info
        advert_message.cost = advert_model.cost
        advert_message.city = advert_model.city
        advert_message.district = advert_model.district
        advert_message.created_date = advert_model.created_date
        advert_message.start_date = advert_model.start_date
        advert_message.finish_date = advert_model.finish_date
        advert_message.status = advert_model.status

        return AdvertGetResponse(advert_get_response=advert_message)


@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertUpdateInfo(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        AdvertMessageInfo,
        id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, message_types.VoidMessage,
                      name='advert_update_info',
                      path='advert_update_info/{id}',
                      http_method='POST')
    def advert_update_info(self, request):
        advert_model = AdvertModel.get_by_id(id=int(request.id))
        advert_model.info = request.info
        advert_model.put()
        return message_types.VoidMessage()


@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertUpdateCost(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        AdvertMessageCost,
        id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, message_types.VoidMessage,
                      name='advert_update_cost',
                      path='advert_update_cost/{id}',
                      http_method='POST')
    def advert_update_cost(self, request):
        advert_model = AdvertModel.get_by_id(id=int(request.id))
        advert_model.cost = request.cost
        advert_model.put()
        return message_types.VoidMessage()


@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertUpdateFinishDate(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        AdvertMessageFinishDate,
        id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, message_types.VoidMessage,
                      name='advert_update_finish_date',
                      path='advert_update_finish_date/{id}',
                      http_method='POST')
    def advert_update_finish_date(self, request):
        advert_model = AdvertModel.get_by_id(id=int(request.id))
        advert_model.finish_date = request.finish_date
        advert_model.put()
        return message_types.VoidMessage()


@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertUpdateStartDate(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        AdvertMessageStartDate,
        id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, message_types.VoidMessage,
                      name='advert_update_start_date',
                      path='advert_update_start_date/{id}',
                      http_method='POST')
    def advert_update_start_date(self, request):
        advert_model = AdvertModel.get_by_id(id=int(request.id))
        advert_model.start_date = request.start_date
        advert_model.put()
        return message_types.VoidMessage()


@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertUpdateStatus(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        AdvertMessageStatus,
        id=messages.StringField(1))

    @endpoints.method(GET_RESOURCE, message_types.VoidMessage,
                      name='advert_update_status',
                      path='advert_update_status/{id}',
                      http_method='POST')
    def advert_update_status(self, request):
        advert_model = AdvertModel.get_by_id(id=int(request.id))
        advert_model.status = request.status
        advert_model.put()
        return message_types.VoidMessage()


@api_collection.api_class(resource_name='AdvertTransactions')
class AdvertList(remote.Service):
    GET_RESOURCE = endpoints.ResourceContainer(
        city=messages.StringField(1),
        page=messages.IntegerField(2))
    @endpoints.method(GET_RESOURCE, AdvertListResponse,
                      name='advert_list',
                      path='advert_list/{city}/{page}',
                      http_method='GET')
    def advert_list(self, request):
        advert_model = AdvertModel.query(AdvertModel.city == request.city
                                         and AdvertModel.status == True
                                         and AdvertModel.status == True
                                         and AdvertModel.finish_date <=
                                         datetime.datetime.now()).fetch(20*request.page,offset=20*(int(request.page)-1))
        advert_list_response = AdvertListResponse()
        for advert_model_get in advert_model:
            advert_message_list = AdvertMessageList()
            advert_message_list.id = advert_model_get.key.id()
            advert_message_list.title = advert_model_get.title
            advert_message_list.owner = advert_model_get.owner
            advert_message_list.info = advert_model_get.info
            advert_message_list.cost = advert_model_get.cost
            advert_message_list.city = advert_model_get.city
            advert_message_list.district = advert_model_get.district
            advert_message_list.created_date = advert_model_get.created_date
            advert_message_list.start_date = advert_model_get.start_date
            advert_message_list.finish_date = advert_model_get.finish_date
            advert_message_list.status = advert_model_get.status
            advert_list_response = advert_message_list

        return advert_list_response


api = endpoints.api_server([
                            UserPut,
                            UserGet,
                            UserUpdateCity,
                            UserUpdatePhone,
                            UserUpdateEmail,
                            AdvertPut,
                            AdvertGet,
                            AdvertUpdateInfo,
                            AdvertUpdateCost,
                            AdvertUpdateFinishDate,
                            AdvertUpdateStartDate,
                            AdvertUpdateStatus,
                            AdvertList])

