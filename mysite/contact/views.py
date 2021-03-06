from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

def contact(request):
	errors = []
	if request.method == "POST":
		if not request.POST.get("subject", ""):
			errors.append("Enter a subject")
		if not request.POST.get("message", ""):
			errors.append("Please enter message")
		if request.POST.get("email") and "@" not in request.POST["email"]:
			errors.append("Please enter a valid email address")
		if not errors:
			send_mail(
				request.POST["subject"],
				request.POST["message"],
				request.POST.get("email", "noreply@example.com"), # from-jauciu defaultas, nes "not required" fieldas modelyje
				["siteowner@example.com"], #to
			)
			return HttpResponseRedirect("/contact/thanks/")
	return render(request, "contact_form.html", {"errors" : errors})

def thanks(request):
	return HttpResponse("Thank you for your message")