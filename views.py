from django.http import HttpResponse
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect

from django.template import RequestContext
from django.shortcuts import render_to_response

def my_homepage_view(request, homepage_template):
    if request:
        return render_to_response(homepage_template, locals(), context_instance=RequestContext(request))
    return render_to_response(homepage_template, locals())

def hello(request):
    return HttpResponse("Hello world")

#def response(template, params={}, request=None):
#    if request:
#        return render_to_response(template, params, context_instance=RequestContext(request))
#    return render_to_response(template, params)
