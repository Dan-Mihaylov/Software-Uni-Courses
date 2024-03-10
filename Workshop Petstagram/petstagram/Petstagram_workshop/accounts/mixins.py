from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileOwnerRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        result = super().dispatch(request, *args, **kwargs)
        if request.user.pk != kwargs['pk']:
            return self.handle_no_permission()
        return result

# We are using the kwargs['pk'] because dispatch is called before the get/post method, and
# the self.object does not exist yet, so we take the 'pk' from the url link instead.
