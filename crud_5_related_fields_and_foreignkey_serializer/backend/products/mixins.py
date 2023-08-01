from .permissions import IsStaffEditorPermission
from rest_framework import permissions 
from rest_framework import authentication
from .authentication import BearTokenAuthentication 

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class BearTokenAuthenticationMixin(BearTokenAuthentication):   
 
    authentication_classes = [
        authentication.SessionAuthentication,
        BearTokenAuthentication
              
        ]

class UserQuerySetMixin():
    user_field = 'user'   

    def get_queryset(self, *args, **kwargs):
               
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user      
        # print(lookup_data)
        qs = super().get_queryset(*args, **kwargs)      
      
        return qs.filter(**lookup_data) 
     