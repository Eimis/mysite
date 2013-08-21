from django.shortcuts import render
import datetime
from books.models import Book
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	books = Book.objects.all
	return render(request, "current_datetime.html", {"current_date" : now, "book_list" : books})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	return render(request, "future_time.html", {"offset" : offset, "new_time" : dt})

def display_meta(request):
	# url> view, view > template!
	#nesudaro lenteles palei knyga
	value = request.META["REMOTE_ADDR"]
	return render(request, "future_time.html", {"value": value})




