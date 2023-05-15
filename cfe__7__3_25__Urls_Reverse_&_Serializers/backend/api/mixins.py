from .permissions import IsStaffEditorPermission
from rest_framework import permissions


class StaffEditorPermissionMixin():
    permisssion_class = [permissions.IsAdminUser, IsStaffEditorPermission]