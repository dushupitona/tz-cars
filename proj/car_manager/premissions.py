from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

class OwnerPermissionMixin(PermissionRequiredMixin):
    def has_permission(self):
        obj = self.get_object()
        if obj.owner.id != self.request.user.id:
            return False
        return True