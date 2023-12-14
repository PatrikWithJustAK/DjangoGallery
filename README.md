This project intends to be a gallery for AI art.
There are currently 2 apps under development: "User", and "Gallery"

"CustomUser.User" (henceforth referred to as User) is a custom user model defined with django's "AbstractBaseUser". It uses an email for login (not username), and has a shorthand "name" which is optional.
"User" can be authenticated using login() and logout() with the corresponding endpoints 
"User" can be created via the signup() view, which utilizes a custom UserCreationForm instance from django.contrib.auth. This form is then validated as POST data and saved to the DB if validation is TRUE

"Gallery.Artipiece" is a model that represents an artpiece.
"Artpiece" can be added using the addartpiece() view, which utilizes a custom ModelForm to request an image upload, as well as a "description" text for the image
"Artpiece" can be made public, making it searchable on the "index.html" page. 
"Artpiece" can be made private, only visible to the creator if they are Authenticated 
"Artpiece" has a ForeignKey relation to the "CustomUser.User" model, allowing for a gallery to be filtered by creator
"Artpiece" will require the dependency Pillow for Django, in order to handle compression/storage of image files on the server


I am developing this project as the sole dev to showcase my abilities as a full-stack developer. I intend to follow this project until completion of a MVP (Minimum Viable Product). 
Once this project has reached minimum viability (ie: both apps have passing unit tests for basic CRUD features), I will manage the deployment of this application

Current Deployment Strategy:
>Clean ubuntu install
>install OpenLightSpeedServer (potentially nginx/gunicorn)
>install python
>create virtualenv
>git clone from repo
>pip install requirements.txt
>configure HTTP server (OLS/nginx) for WSGI


