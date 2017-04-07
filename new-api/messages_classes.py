from protorpc import message_types
from protorpc import messages


class UserMessage(messages.Message):
    auth_id = messages.StringField(1, required=True)
    name = messages.StringField(2, required=True)
    surname = messages.StringField(3, required=True)
    email = messages.StringField(4, required=True)
    city = messages.StringField(5, required=True)
    phone = messages.IntegerField(6, required=True)
    birthday = messages.StringField(7)
    rank = messages.IntegerField(8)


class UserMessageEmail(messages.Message):
    email = messages.StringField(1, required=True)


class UserMessagePhone(messages.Message):
    phone = messages.StringField(1, required=True)


class UserMessageCity(messages.Message):
    city = messages.StringField(1, required=True)


class UserGetResponse(messages.Message):
    user_get_response = messages.MessageField(UserMessage, 1, required=True)


class AdvertMessage(messages.Message):
    title = messages.StringField(1, required=True)
    owner = messages.StringField(2, required=True)
    info = messages.StringField(3, required=True)
    cost = messages.IntegerField(4, required=True)
    city = messages.StringField(5, required=True)
    district = messages.StringField(6, required=True)
    created_date = message_types.DateTimeField(7)
    start_date = message_types.DateTimeField(8, required=True)
    finish_date = message_types.DateTimeField(9, required=True)
    status = messages.BooleanField(10, default=True)

class AdvertMessageList(messages.Message):
    id = messages.IntegerField(11, required=True)
    title = messages.StringField(1, required=True)
    owner = messages.StringField(2, required=True)
    info = messages.StringField(3, required=True)
    cost = messages.IntegerField(4, required=True)
    city = messages.StringField(5, required=True)
    district = messages.StringField(6, required=True)
    created_date = message_types.DateTimeField(7)
    start_date = message_types.DateTimeField(8, required=True)
    finish_date = message_types.DateTimeField(9, required=True)
    status = messages.BooleanField(10, default=True)


class AdvertMessageInfo(messages.Message):
    info = messages.StringField(1, required=True)


class AdvertMessageCost(messages.Message):
    cost = messages.IntegerField(1, required=True)


class AdvertMessageFinishDate(messages.Message):
    finish_date = message_types.DateTimeField(1, required=True)


class AdvertMessageStartDate(messages.Message):
    start_date = message_types.DateTimeField(1, required=True)


class AdvertMessageStatus(messages.Message):
    status = messages.BooleanField(1, required=True)


class AdvertGetResponse(messages.Message):
    advert_get_response = messages.MessageField(AdvertMessage, 1, required=True)


class AdvertListResponse(messages.Message):
    advert_list_response = messages.MessageField(AdvertMessage, 1, required=True)
