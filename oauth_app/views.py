from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


@login_required
def logged_in(request):
    return render(request, 'oauth_app/logged_in.html',
    )