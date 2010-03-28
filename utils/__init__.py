from django.shortcuts import render_to_response
from django.template import RequestContext
 
def response(request, template, context):
    return render_to_response(template, context, context_instance=RequestContext(request))
 
def post_data(request):
    return request.POST.copy()
 
def get_data(request):
    return request.GET.copy()