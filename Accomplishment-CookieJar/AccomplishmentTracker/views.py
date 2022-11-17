from django.shortcuts import render, redirect, get_object_or_404
from .models import CookieJar, SaveJoke
from .forms import CookieTracker, SaveJokeForm
import requests
from bs4 import BeautifulSoup
import json


# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def cookie_jar_home(request):
    return render(request, "AccomplishmentTracker/AccomplishmentTracker_home.html")


# For Full Screen Page -----------------------------------------------------------------------------------

def cookie_jar_home_fs(request):
    return render(request, "AccomplishmentTracker/AccomplishmentTracker_homeFS.html")


# For Welcome Page -----------------------------------------------------------------------------------

def cookie_welcome(request):
    return render(request, "AccomplishmentTracker/at_welcome.html")


# Change Background Page -----------------------------------------------------------------------------------

def cookie_change_bg(request):
    return render(request, "AccomplishmentTracker/AccomplishmentTracker_change_BG.html")


# Story #2: Create your model ------------------------------------------------------------------------------------------

def cookie_create(request):
    form = CookieTracker(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../create')
    content = {'form': form}
    return render(request, 'AccomplishmentTracker/AccomplishmentTracker_create.html', content)


# Story #3: Display all items from database ----------------------------------------------------------------------------

def cookie_read(request):
    entry = CookieJar.cookies.all()
    content = {'entry': entry}
    return render(request, 'AccomplishmentTracker/AccomplishmentTracker_read.html', content)


# Story #4: Details page -----------------------------------------------------------------------------------------------

def cookie_details(request, pk):
    entry = get_object_or_404(CookieJar, pk=pk)
    content = {'entry': entry}
    return render(request, 'AccomplishmentTracker/AccomplishmentTracker_details.html', content)


# Story #5: Edit and Delete Functions ----------------------------------------------------------------------------------

def cookie_update(request, pk):
    entry = get_object_or_404(CookieJar, pk=pk)
    form = CookieTracker(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'entry': entry}
    return render(request, 'AccomplishmentTracker/AccomplishmentTracker_update.html', content)


def cookie_delete(request, pk):
    entry = get_object_or_404(CookieJar, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../read')
    content = {'entry': entry}
    return render(request, 'AccomplishmentTracker/AccomplishmentTracker_delete.html', content)


# Story #6-(BS Pt 1): Setup Beautiful Soup -----------------------------------------------------------------------------
# Story #7-(BS Pt 2): Parse through html

def cookie_bs(request):
    page = requests.get("https://productiveclub.com/cookie-jar-method/#How_to_apply_the_cookie_jar_method")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all('p')[0].get_text()  # I extracted the first Paragraph
    info_quote = soup.find_all('blockquote')[2].p.get_text()  # I extracted the 2nd quote's paragraph
    content = {"info": info, "info_quote": info_quote}
    return render(request, 'AccomplishmentTracker/AccomplishmentTracker_bs.html', content)


# Story #6-(API Pt 1): Connect to API ----------------------------------------------------------------------------------
# Story #7-(API Pt 2): Parse through JSON


def cookie_joke_api(request):
    # url_1, info_1 = api for one-part joke | url_2, info_2 = api for two-part joke
    # NOTE: I only used the url_2, response_2, info_2, setup, and delivery for my api two part joke.
    url_1 = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,political,racist,sexist,explicit&type=single"
    url_2 = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,political,racist,sexist," \
            "explicit&type=twopart"
    response_1 = requests.request("GET", url_1)
    response_2 = requests.request("GET", url_2)
    info_1 = json.loads(response_1.text)
    info_2 = json.loads(response_2.text)
    # joke variable
    joke = str(info_1["joke"])
    # two-part joke variables
    setup = str(info_2["setup"])
    delivery = str(info_2["delivery"])
    content = {"setup": setup, "delivery": delivery, "joke": joke}
    return render(request, 'AccomplishmentTracker/at_joke_api.html', content)


# Story #9: Save API or scraped results --------------------------------------------------------------------------------

def cookie_save_joke(request):
    setup = request.POST.get('Setup', None)
    delivery = request.POST.get('Delivery', None)
    SaveJoke.jokes.create(Setup=setup, Delivery=delivery)
    form = SaveJokeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return redirect('cookie_joke_api')


def cookie_read_joke(request):
    entry = SaveJoke.jokes.all()
    content = {'entry': entry}
    return render(request, 'AccomplishmentTracker/at_read_joke_api.html', content)
