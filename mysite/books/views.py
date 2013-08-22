from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite.books.models import Book
from django.core.mail import send_mail


def search(request):
	errors = []
	if "q" in request.GET:
		q = request.GET['q']
		if not q:
			errors.append("Please enter a search term")
		elif len(q) > 20:
			errors.append("Please enter at most 20 characters")
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, "search_results.html", {"books" : books, "query": q})
	return render(request, "search_form.html", {"errors" : errors}) #wintest_last

def contact(request):
	errors = []
	