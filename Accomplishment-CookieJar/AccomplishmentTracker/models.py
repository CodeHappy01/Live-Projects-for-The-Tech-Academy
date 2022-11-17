from django.db import models


# Creating model for CookieJar.exe, title, date, text


class CookieJar(models.Model):
    Title = models.CharField(max_length=50)
    Date = models.DateTimeField(auto_now_add=True)
    Accomplishment = models.TextField(default='')

    # Object manager
    cookies = models.Manager()

    # Displays Cookie Title
    def __str__(self):
        return self.Accomplishment


# Create form for saving Jokes from Jokes API


class SaveJoke(models.Model):
    Setup = models.CharField(max_length=200, primary_key=True, unique=True)
    Delivery = models.CharField(max_length=200,  unique=True)
    # Object manager:
    jokes = models.Manager()

    def __str__(self):
        return self.Setup
