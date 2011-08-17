from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

class Account(DetailView):
    def get_object(self, queryset=None):
        return self.request.user
