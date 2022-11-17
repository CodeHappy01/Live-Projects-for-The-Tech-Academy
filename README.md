<br />
<div align="center">
  <a href="#">
    <img src="Accomplishment-CookieJar/images/ScreenShots/Thumbnail.png" alt="Logo" width="400" height="400">
  </a>

<h3 align="center">Accomplishment Cookie Jar</h3>
</div>

<br>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project:</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#cookiejarexe(crud)">CookieJar.exe(CRUD):</a>
      <ul>
        <li><a href="#create">Create</a></li>
        <li><a href="#read">Read</a></li>
        <li><a href="#update-and-delete">Update and Delete</a></li>
      </ul>
    </li>
    <li><a href="#beautiful-soup">Beautiful Soup</a></li>
    <li><a href="#joke-api">Joke API</a></li>
    <li><a href="#front-end-development">Front-End Development:</a></li>
    <li><a href="#skills-aquired">Skills Aquired:</a></li>
    <li><a href="#contact">Contact:</a></li>
    <li><a href="#acknowledgments">Acknowledgments:</a></li>
  </ol>
</details>

<br>

# About The Project:
During a two week springt at [The Tech Academy](https://www.learncodinganywhere.com/) I had the opportunity to work with a team of very talented peers on a web Application called the "Appbuilder9000"! We worked under Azure Devops environment being assigned 10 stories (2-9 being the main focus) to complete by the end of the sprint. 

<img src="Accomplishment-CookieJar/images/ScreenShots/AB9000.png" alt="The-Site" width="960" height="540">

Although, we worked on the same site we had the chance to work on are own individual applications that connected to the main page. This allowed my team and I to showcase are own skills while following the stories assigned to us along the way. 

<img src="Accomplishment-CookieJar/images/ScreenShots/Home.png" alt="My-Application" width="960" height="540">


I made my idea come to life by using the site [Canva](https://www.canva.com/), a graphic design platform that is used to create visual content for social media, presentations, websites, etc. 

<img src="Accomplishment-CookieJar/images/ScreenShots/Canva.png" alt="My-Application" width="960" height="540">

<br>

# Built With

HTML | CSS | JS | PYTHON | DJANGO | PYCHARM | CANVA
 

# CookieJar.exe(CRUD):

 <img src="https://github.com/CodeHappy01/Live-Projects-for-The-Tech-Academy/blob/main/Accomplishment-CookieJar/gifs/CookieJar.exe.gif" alt="CRUD" width="960" height="540">
 
 <br>

## Create 

[Story 2: Create your model] 

Story #2: Create your model 

Create a model for the collection item you will be tracking and add the ability to create a new item. 

Create your model and add a migration, make sure to plan out all the categories you want to track for your object. Include an objects manager for accessing the database. 

Create a model form that will include any inputs the user needs to make 

Add a template to your app folder for creating a new item. 

Add a views function that renders the create page and utilizes the model form to save the collection item to the database. 

Check the database to make sure your item saves without errors. 

Add whatever styling is appropriate to your templates. 

You are finished with the story when you have a functioning create page. This means the user can add to the database through your template rather than through admin. Make sure to test and debug before submitting. 

```xml
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
```

<br>

## Read 

[Story 3: Display all items from database] 

Display information from the database in a page. 

Create a new HTML page, link it from your home page 

Add in a function that gets all the items from the database and sends them to the template 

Display a list of items from the database, with some of the fields for that item displayed with labels/headers. 

Add whatever styling is appropriate to your templates. 

You are finished with the story when you have a functioning page that lists the items in the database. Make sure to test and debug before submitting. 

 

[Story 4: Details page] 

 

Create a details page that will show the details of any single item from within the database, as selected by the user. Link this to the index page for each item. 

Add a details template to the template folder, register the url pattern 

Create a views function that will find a single item from the database and send it to the template 

Add in a link for each item on the display all items page that will direct to the details page for that item 

Display all the details of the item on the details page. 

Add whatever styling is appropriate to your templates. 

<br> 

## Update and Delete 

[Story 5: Edit and Delete Functions] 

Allow for edits and delete functions to be done from the details page or from separate pages. Have confirmation before deleting. 

Add an edit page to the templates (another pattern url) 

Use model forms and instances to display the content of a single item from the database 

Have the views function send the information for the single item and save any changes. 

Include the option to delete an item with a confirmation that the user wants to delete. 

Add whatever styling is appropriate to your templates. 

You are finished with the story when you have a functioning edit page for any item in the database, and the ability to delete that item. Make sure to test and debug before submitting. 

Optional Add-On: 
-Use a modal and javascript for the delete confirmation message 

<br>

 
 <br>

# Beautiful Soup 

<img src="Accomplishment-CookieJar/images/ScreenShots/BeautifulSoup.PNG" alt="Web-Scraping" width="960" height="540">

[Stories 6 & 7: Beautiful Soup] 

Story 6: Create a new template for displaying information sourced from another website. Use Beautiful Soup to data scrape the site and find the relevant information. 

Create a new template for displaying the content 

Use Beautiful Soup to get the html data from your selected site as a navigable object 

Utilizing whatever options necessary, get the section of data you want to scrape 

Add comments to note which portions of the data you're trying to extract 

Link the data scraping page to the app's home page 

Story 7: Parse through the html returned and display the information you want to display. Make sure you are getting into the individual elements and stripping away any formatting you don't want. Add a link from your app's home page. 

Get elements out of your Beautiful Soup object, send just the values you want as relevant dictionary objects to the template (nested dictionaries are fine) 

Display all objects within the data scrape template 

Test to make sure everything works as expected, do error handling where necessary 

Add whatever styling is appropriate to your templates. 

This is the last Beautiful Soup story. Make sure it has all the functionality that you want. 

<br> 

# Joke API 

<img src="Accomplishment-CookieJar/gifs/JokeAPI.gif" alt="API" width="960" height="540">

[Stories 6 & 7: API] 

Story 6: Connect to your chosen API and get the JSON response, add in a template for displaying the information. 

Create a new API template and render with a function 

Go through the API documentation 

Connect to the API and write a basic JSON response (either to a txt file or the terminal) 

Add comments of which elements from the JSON response you're looking to get the value for 

Link the API request page to the app's home page. 

Story 7: Parse through the JSON file returned and display the information you want to display. Make additional queries to the API as necessary. Add a link from your app's home page. 

Get elements out of your API JSON response, send just the values you want as relevant dictionary objects to the template (nested dictionaries are fine) 

Display all objects either in the original API service page or in a new results page. 

Test to make sure all the options work as expected, do error handling where necessary 

Add whatever styling is appropriate to your templates. 

This is the last API story. Make sure it has all the functionality that you want. 

You are finished with the story when you have information displaying from the API on your API page, and you've added all functionality you want to interact with the API. Make sure to test and debug before submitting. 

 

 

[Story 9: Save API or scraped results] 

Allow the user to save "favorites" of an item either from the information detailed from the API or from Beautiful Soup. This could mean working with the existing model or creating a new one to pull the information from the response, create the appropriate object, and add it to the database. 

You are finished with the story when you have the ability to save an item to the database with a few clicks from either your API page or your Data Scraping page. It is fine to have additional pages for the confirmation and display process. 

<br>

# Front End Development:

<img src="Accomplishment-CookieJar/gifs/Full-Site.gif" alt="Front-End" width="960" height="540">

[Story 8: Front End Improvements] 

Go through your various templates and add improvements to the UI/UX. This may include hover effects, pop-ups, animations, changes to the existing styling, etc. Show off your creativity and styling ability with some JavaScript in this. Make sure to test and debug before submitting. 

### Window Browswer Scaling - 


<img src="Accomplishment-CookieJar/gifs/Browser-Window-Scaling.gif" alt="Logo" width="960" height="540">


## Christmas

<img src="Accomplishment-CookieJar/images/ScreenShots/ChristmasPNG.PNG" alt="Christmas" width="960" height="540">

At the end of my stories I decided to have a bit of fun with the time I had left and made a Christmas template through Canva and back in Pycharm I decided to add a Christams video along with a count down till Christmas counter using Javascript: 

### Counter

<img src="Accomplishment-CookieJar/images/ScreenShots/CountDown.PNG" alt="count-down" width="400" height="150">

```xml
/**
 * JavaScript function, which calculates the days, hours,
 * minutes and seconds left until Christmas day.
 * (link: https://thisinterestsme.com/javascript-christmas-countdown/)
 */
function calculateChristmasCountdown(){

    //Get today's date.
    var now = new Date();

    //Get the current month. Add a +1 because
    //getMonth starts at 0 for January.
    var currentMonth = (now.getMonth() + 1);

    //Get the current day of the month.
    var currentDay = now.getDate();

    //Work out the year that the next Christmas
    //day will occur on.
    var nextChristmasYear = now.getFullYear();
    if(currentMonth == 12 && currentDay > 25){
        //This year's Christmas Day has already passed.
        nextChristmasYear = nextChristmasYear + 1;
    }

    var nextChristmasDate = nextChristmasYear + '-12-25T00:00:00.000Z';
    var christmasDay = new Date(nextChristmasDate);

    //Get the difference in seconds between the two days.
    var diffSeconds = Math.floor((christmasDay.getTime() - now.getTime()) / 1000);

    var days = 0;
    var hours = 0;
    var minutes = 0;
    var seconds = 0;

    //Don't calculate the time left if it is Christmas day.
    if(currentMonth != 12 || (currentMonth == 12 && currentDay != 25)){
        //Convert these seconds into days, hours, minutes, seconds.
        days = Math.floor(diffSeconds / (3600*24));
        diffSeconds  -= days * 3600 * 24;
        hours   = Math.floor(diffSeconds / 3600);
        diffSeconds  -= hours * 3600;
        minutes = Math.floor(diffSeconds / 60);
        diffSeconds  -= minutes * 60;
        seconds = diffSeconds;
    }

    //Add our counts to their corresponding HTML elements.
    document.getElementById('days').innerHTML = days + ' Days';
    document.getElementById('hours').innerHTML = hours + ' Hours';
    document.getElementById('minutes').innerHTML = minutes + ' Minutes';
    document.getElementById('seconds').innerHTML = seconds + ' Seconds';

    //Recursive call after 1 second using setTimeout
    setTimeout(calculateChristmasCountdown, 1000);
}

calculateChristmasCountdown();
```

 <br>

# Skills Acquired: 

 

A skill that I found to be pretty good at is utilizing Canva’s to build my backgrounds and icons for my web application. Being able to express my creativity without spending too much time with my own drawings   definitely something that I will take with me and  

 

Another is being able to work with a team of others and communicating how my application works, and even helping others.  

 

Obvious skills that I note from the project was working with the model, view, templates layout of django,.  

<br>

# Contact:
 
