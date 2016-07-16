from django.contrib.auth import get_user_model

from tastypie import fields
from tastypie.api import Api
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import ReadOnlyAuthorization
from tastypie.contrib.gis.resources import ModelResource
from tastypie.resources import Bundle, ALL

from surfers.models import LatestPoint


class OwnerCanUpdate(ReadOnlyAuthorization):

    def create_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def update_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def delete_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user


class LatestPointResource(ModelResource):

    class Meta:

        queryset = LatestPoint.objects.all()

        authorization = OwnerCanUpdate()
        authentication = SessionAuthentication()

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']

        excludes = ['id']

        filtering = {
            'point': ALL,
            'updated_at': ['gte', 'lt']
        }

    def obj_create(self, bundle, **kwargs):
        return super().obj_create(bundle, user=bundle.request.user)

    def dispatch(self, request_type, request, **kwargs):
        if request_type == 'detail' and 'pk' in kwargs:
            if not kwargs['pk'].isdigit():
                try:
                    kwargs['pk'] = LatestPoint.objects.get(user__username=kwargs['pk']).id
                except LatestPoint.DoesNotExist:
                    pass
        return super().dispatch(request_type, request, **kwargs)

    def detail_uri_kwargs(self, bundle_or_obj=None):
        if isinstance(bundle_or_obj, Bundle):
            obj = bundle_or_obj.obj
        else:
            obj = bundle_or_obj
        return {'pk': obj.user.username}


class UserResourceAuthorization(ReadOnlyAuthorization):
    def update_detail(self, object_list, bundle):
        return bundle.obj == bundle.request.user


class UserResource(ModelResource):
    latest_point = fields.ToOneField(LatestPointResource, 'latest_point',
                                     null=True)

    class Meta:
        excludes = ['password', 'email', 'is_active', 'is_staff', 'is_superuser']
        queryset = get_user_model().objects.all()
        authorization = UserResourceAuthorization()
        authentication = SessionAuthentication()


latest_point = LatestPointResource()
user = UserResource()

v1_api = Api(api_name='v1')
v1_api.register(latest_point)
v1_api.register(user)
