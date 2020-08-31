# THE MOKSHA CENTRE

### Fullstack Milestone Project

This project follows a theme that has been prevalent in most of my work.  My projects thus far have revolved around the subject of holistic health, in one form or another.  It is hardly surprising then, that I remained with this theme for my final fullstack project.

The name for the project was inspired by the contents of the wikipedia entry for [yoga](https://en.wikipedia.org/wiki/Yoga).  The ultimate goal of yoga is cited as being *Moksha*, or enlightenment.

The primary purpose of the project is to encourage users to purchase products related to yoga.  The includes clothing, equipment and nutrition products.  Secondary to this, is a goal to encourage users to engage in discussions around all topics related to yoga and beyond.  It is also hoped that users will encourage others to join the community and may comment upon or even recommend products from the store.

The incorporation of HTML, CSS, JavaScript and Python elements in an organised, well-structured manner should satisfy the last goal of displaying the developers's talents as a junior fullstack web developer. The site can be viewed [here](https://moksha-centre.herokuapp.com/)


***
## UX 

### Initial design decisions

Initial design ideas were drawn from a variety of sources, in particular the following sites:

* [Fitocracy](https://www.fitocracy.com/)
* [Fitness Blender](https://www.fitnessblender.com/)
* [The Yoga House Roma](https://www.theyogahouseroma.com/)
* [Our Yoga Shop](https://ouryogashop.com/)
* [Back 2 Basics](https://back2basics.ie/)


### Strategy & Planning
The UX design process revolves around a mobile-first design.  As the focus for the site is purchasing goods, most of the attention has been given to providing the user with a range of products and a means to purchase these products.

The design also reflects many of the ideas presented in the course curriculum.  They have, naturally enough, been adapted to reinforce the site's own identity.


#### User Stories
* As a shopper I want to be able to:
  * view a list of products
  * sort the products according to categories
  * search for products and find deals or special offers
  * easily purchase these products
  * view a summary of my order and adjust it as necessary
  * receive confirmation or my order once placed
* As a casual site user, I want to complete the above without the hassle of signing up, logging in, or joining a mailing list.
* As a regular site user, I want to complete the above but also:
  * signup and create an account
  * easily login and logout
  * receive email confirmation
  * recover my password, if I forget it
* As a forum user, I want to:
  * read about other user's experiences
  * share my own experiences
  * share interesting posts with other friends
  * comment on posts that interest me
  * sort posts by categories / tags to only select posts about subjects that interest me.
* As a site owner, I would like an administration site to manage products, user accounts, forum posts and comments, etc. 


#### Prioritization
As stated the priority for this project was to create a functioning shop, that would facilitate users in the viewing and purchasing of shop products.


### Scope
The scope of the project was guided by the need to create a functioning shop.  The forum was created as an alternative avenue to encourage users to visit the site, share their ideas and experiences; share these (or other) ideas and experiences with other non-site users (hopefully attracting them to the site), and perhaps make a purchase while visiting the site.

The various elements that were included in the core scope include:

* A landing page that clearly indicates the broad nature of the site.  This is apparent in the design of the navigation bar, with quick access to shop products.
* A brief introduction makes the site's purpose clear.
* A search filter to allow users to search for products and, upon searching, they are informed of the number of products that match their search term.
* Pagination also provides an visual indicator of how many products the user might expect to see.
* The navigation bar is uncluttered and responds to the user's login status.


### Structure
The site incorporate a main navigation menu and structured layout (using Bootstrap to accomplish this).

Casual users can view products but are encouraged to become engaged users.  Engaged users are rewarded with access to the forum.


### Skeleton
Ideas for the design were drawn from the research carried out during the initial design phase.  The design of wireframe reflects these choices.  A pdf of the wireframes is available [here](https://res.cloudinary.com/bogtrotter72/image/upload/v1598903750/The%20Moksha%20Centre/xi17vzrxkvw3lvlvyrx2.pdf).


### Surface
The aesthetic of the site is clean, fresh and bright. On desktop, gentle animations provide interesting visual stimulation for users as does the change in the navbar opacity.  The idea for the colours comes from the site's main image, and this image is prevalent throughout the site. Some of the buttons retain their default bootstrap colours, while others use the *outline* class; others still include icons. Subtle shading offers a sense of depth - something that features in most of my work.



***
## Features
### Existing features
* **Responsive Navigation** - The *Accounts* dropdown in the navigation bar adapts to the user's login status - displaying _signup_ and _login_ if the user is not logged in and _logout_ if they are.
* **Toasts** - Users are provided with feedback of virtually every action taken on the site.  Apart from the *success* messages, toasts are automatically hidden after a short delay.  This is due to the fact that success message include adding items to the shopping bag.


### Planned features 
* Ithe inclusion of a user profile page with an order / forum post history
* A membership subscription facility to include offering yoga or pilates classes


***
## Technologies Used
* [HTML](https://en.wikipedia.org/wiki/HTML) - Providing the basic structure for content.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Styling the site, providing responsive design and adding button animations.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Adding a small amount of functionality to the site. 
* [JQuery](https://jquery.com/) - Supporting library for much of the JavaScript functionality.
* [Django](https://www.djangoproject.com/) - Supporting library for much of the JavaScript functionality.
* [Balsamiq](https://balsamiq.com/) - Creating wireframes at project inception

***
## Testing 

### Data Testing
All CRUD operation were checked, including:
* Creating a user account, including email verification, etc
* Creating forum posts and adding comments
* Sharing forum posts
* Viewing products
* Searching for products, and filtering these by categories(tags)
* Purchasing products
* Updating products
* Removing products

### Manual Testing
Throughout the project, the terminal window and dev tools window were used extensively, as were print statements in the code.  All clickable elements were thoroughly tested.


The website was also tested in the Blisk browser, on a variety of devices, including:
* Samsung Galaxy S5
* iPhone 5/SE
* iPhone 6/7/8
* iPhone X
* iPad
* iPad Pro

Chrome and Blisk developer tools were used for testing the site, and were of particular use in positioning the graphics and confirming control flow.

### Cross-Browser Compatability
The website was tested in the following browsers:
* Blisk
* Firefox
* Google Chrome
* Microsoft Edge
* Opera

### Live Testing
The project was viewed and tested on mobile tablet, laptop and desktop devices.  Work colleagues, friends and families were invited to review and feedback on the site; all of which positive.  The site was thoroughly tested by my mentor and I am grateful to him for expanding my understanding of testing.


### Interesting bug - resolved
The interplay between development environment and production environment was tested when it was noticed that a field was missing form the *checkout order model*.  After the field was added and the necessary migrations made, orders failed to be processed with an error message stating that the field was not found in the *checkout_order* table.
**WARNING**
The simple solution was to delete the *sqlite* file and make migrations anew.  This, however, also deletes the entire database, including all products, tags, forum posts, etc.  A more elegant solution was found by simply modifying the file using the [DB Browser for SQLite](https://sqlitebrowser.org/).


At one point, the checkout form failed to post.  After several hours debugging, no error in the code was found.  Finally, the code was cut and pasted into another text editor and then re-entered line by line (without alteration).  After doing this, the form functioned as expected.

## Deployment
This site is hosted using Github pages, and is deployed directly from the master branch.  To use the resource, clone or download the respository, and create and activate a local environment ([virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)). If you download the zip file, extract the files and open the folder in your chosen IDE. Open a terminal window and navigate to the root folder.  To install all the dependencies enter `pip install -r requirements.txt` into the command line.  Before using the application check the status of the database migrations by entering *python manage.py showmigrations* into the command line and ensure that all migrations are crossed off.  If not, enter *python manage.py migrate* to create the necessary database tables.  To allow debugging, change the `debug` setting in the `run.py` file to `True`.  To run the application enter `python run.py` into the command line and then point your browser to the url shown (usually http://127.0.0.1:8000)

***

### Media
Favicon created at [favicon.io](https://favicon.io/favicon-converter/).  All of the recipe images and texts have been taken from [Forks Over Knives](https://www.forksoverknives.com) and are largely unaltered.



### Acknowledgements
I would like to acknowledge the code institute tutors for providing me with the basis for this project, in particular the framework for the shop.  While the code for the shop is based on the course curriculum, it has been adapted (where possible) to either conform to the site identity.  At times, these adaptation have come about through simple experimentation.  This has not been the case with adding products with sizes to the shopping bag.  Several attempts were made to adapt the code; each revealing new and interesting bugs.  Much of the code for the bag app’s *contexts.py* and handling of sizes in its *views.py* file has been repeated here verbatim.  In other areas, such as in the *quantity_input_script.html*, the function has been altered somewhat, simply to reflect my own learning.

The clothing and equipment products have been sourced from [McSport](https://www.mcsport.ie/) and [Sports Direct Ireland](https://ie.sportsdirect.com/) and the nutrition products have been sourced from [Yoga Nutrition](https://yoganutrition.co.uk/).

All other imagery has been taken from [Unsplash](https://yoganutrition.co.uk/)

**Disclaimer**

The content of this website is for educational purposes only.