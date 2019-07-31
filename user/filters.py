from user import models
from django.contrib.auth.models import Group
import rest_framework_filters as filters


class GroupFilter(filters.FilterSet):
    class Meta:
        model = Group
        fields = {"id": "__all__" , "name" : "__all__"}


class UserFilter(filters.FilterSet):

    groups = filters.RelatedFilter(
        GroupFilter, field_name='groups', queryset=Group.objects.all())

    class Meta:
        model = models.User
        fields = {
             "email" : "__all__" , 
             "mobile" : "__all__" 
        }
