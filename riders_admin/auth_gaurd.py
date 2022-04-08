from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def auth_admin(func):
    def wrap(request, *args, **kwargs):
        if 'autherisation_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('')
            
    return wrap

