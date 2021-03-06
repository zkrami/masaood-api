from rest_framework import permissions 


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """
    user_property = 'user'

    def __init__(self, user_property='user'):
        self.user_property = user_property
        super().__init__()

    def has_object_permission(self, request, view, obj):

        # obj here is a UserProfile instance
        try:
            return obj[self.user_property] == request.user
        except:
            return False


class IsAdminOrReadOnly(permissions.BasePermission):

 
            
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and 
            request.user.is_staff 
        )
