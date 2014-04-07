from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from share.models import FileData

def upload_page(request):
	#return HttpResponse("upload page")
	return render_to_response('upload.html', {}, context_instance = RequestContext(request))

def about(request):
	return render_to_response('about.html', {}, context_instance = RequestContext(request))

def contact(request):
	return render_to_response('contact.html', {}, context_instance = RequestContext(request))

def home(request):
	file_list = FileData.objects.all()
	return render_to_response('index.html', {'list':file_list}, context_instance = RequestContext(request))

def file_submit(request):
	if request.method == "POST":
		course_name = request.POST['course-name']
		department_code = request.POST['dept']
		course_code = request.POST['course-code']
		category = request.POST['category']
		a = FileData(course_name = course_name, department_code = department_code, course_code = course_code, category = category)

		if request.POST['year']!='':
			a.year = int(request.POST['year'])

		"""if request.POST['prof']!='':
			a.year = request.POST['prof']"""

		"""if request.POST['description']!='':
			a.year = request.POST['description']"""

		a.save()
		return HttpResponseRedirect('/')
