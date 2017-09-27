from flask_peewee.rest import RestAPI, RestResource, UserAuthentication, AdminAuthentication, RestrictOwnerResource

from app import app
# from auth import auth


# user_auth = UserAuthentication(auth)
#
# # instantiate our api wrapper
# # api = RestAPI(app, default_auth=user_auth)
#
#
# class UserResource(RestResource):
#     exclude = ('password', 'email',)
#
#
# class MessageResource(RestrictOwnerResource):
#     owner_field = 'user'
#     include_resources = {'user': UserResource}
#
#
# # register our models so they are exposed via /api/<model>/
# api.register(User, UserResource, auth=admin_auth)
