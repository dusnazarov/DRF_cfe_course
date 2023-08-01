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