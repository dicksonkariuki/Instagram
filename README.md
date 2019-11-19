### Instapro
***
## Description
* Instapro is a web application that allows a user to create a profile,login, and upload images.
* The application allows a user to view other users phots and post comments.
***
## Author 
* Dickson Kariuki
***
## Features
#### A user on will be able to :
1. Sign up and login
2. Create profile.
3. View photos uploaded by other users.
4. Post a comment on uploaded photo.
5. Change profile.
6. Logout from the app.
***
### App's Specifications
| Behavior       | Input          | Output |
| ------------- |:-------------:| -----:|
| A user visits the login page     | login credentials else redirected to the registration page| User redirected to the homepage|
|A user visits the registration page     | Provides username,email,password   | Redirected to the homepage |
| A user visits the homepage  | Creates a profile with image and bio      |    A users image and bio is displayed |
| Image upload on the homepage             |A user uploads an image on the homepage             | An uploaded image is displayed on the homepage      |
|Comment          |A user writes a comment and post the comment           |A comment is added on the particular image  |
|  Logout       |    A user clicks on the settings icon           |A prompt to redirect a user to either logout ,cancel or edit profile       |
|               |               |       |

### Accessing the Application
#### Basic Requirements
* Python3.6 
* Django 1.1 
* virtual environment
* pip
***
### How to clone the app
* In your terminal run the command :git clone https://github.com/dicksonkariuki/Instagram.git
* Navigate to the application by typing cd instagram
### How to run the application
* Install virtual environment using :$ python3.6 -m venv --without-pip virtual
* Activate the virtual environment using:source virtual/bin/activate
* Install the latest version of pip using:curl https://bootstrap.pypa.io/get-pip.py | python
* Install Django using :python -m pip install django
* Install all the dependencies and put them in a requirements file.
* Create a database then add its credentials in the settings.py,then migrate.
* Run the application in your terminal using"python3.6 manage.py runserver
***
### Technologies used 
1. Python -for backend.
2. Django -for creating the admin dashboard.
3. Html5 for creating webpages.
4. CSS3 for styling.
5.Bootstrap3 -for creating elegant designs.
***
### Support 
* dicksonkariuki4@gmail.com
### Licence
This software is licenced under MIT licence.
