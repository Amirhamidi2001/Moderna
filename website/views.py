from django.shortcuts import render, redirect
from .forms import ContactForm, NewsletterForm
from django.http import HttpResponseRedirect

def index_view(request):
    return render(request, "website/index.html")


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {"form":form}
    return render(request, "website/contact.html", context)


def detail_view(request):
    return render(request, "website/portfolio-details.html")


def portfolio_view(request):
    return render(request, "website/portfolio.html")


def services_view(request):
    return render(request, "website/services.html")


def team_view(request):
    return render(request, "website/team.html")


def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/kirkhar/")
    else:
        return HttpResponseRedirect("/")
