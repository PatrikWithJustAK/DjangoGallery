
from .models import User
from django.test import TestCase, Client
from django.urls import reverse

#SignupViewTest
#Contains all unit tests for the view "signupview"
class SignupViewTest(TestCase):

        #Register the client and the signup url as member variables for all tests on this view
    def setUp(self): 
        self.client = Client()  #test client
        self.signup_url = reverse('signup') #the name associated in "urls.py"

        #Testing the signupview() to ensure that it responds to GET with a 200 status code
    def test_signup_view_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html') 

        #Testing the signupview() to ensure that a new user can be created via POST request
    def test_signup_view_POST_creates_user(self):
        #The view utilizes a UserCreationForm class to collect credentials from the client
        #To mimic this, we send a post request with "user_data" dictionary as context.
        #These fields match the required fields as defined in forms.CustomUserCreationForm
        user_data = {} 
        user = "newuser"
        email = "newuser@example.com"
        password1 = "T3sTinG123"
        password2 = "T3sTinG123"
        user_data = {
            "name" : user, 
            "email" : email, 
            "password1" :password1,
            "password2" : password2}
        response = self.client.post(self.signup_url, user_data) #send POST request to signupview(), including the user_data{} for our test user
        self.assertEqual(response.status_code, 302)  #Succesful POST requests to this view will return a redirect as defined in views.py. We check this behavior by confirming HTTP status code 302 (redirect)
        self.assertTrue(User.objects.filter(name='newuser').exists()) #Sucessful POST requests to this view will generate a User object and save to the DB. We check this behavior using User.objects.filter.

    # Add more tests as needed (e.g., testing form validation, error messages, etc.)
    #
    #
    #
#CustomUserModel
#Contains all unit tests for the custom model "User"
class CustomUserModelTest(TestCase):
    def setUp(self):
        # Create a user instance for testing
        User.objects.create(name='testuser', email='test@example.com')

    def test_get_short_name_returns_string(self):
        #Test that the get_short_name method returns a string.
        user = User.objects.get(name='testuser')
        short_name = user.get_short_name()
        self.assertIsInstance(short_name, str)         # Assert that the returned value is a string
    #
    #
    #

#LoginViewTest
#Contains all unit tests for the view "loginview()"
class LoginViewTest(TestCase):
        #Set up client and URL for all tests in this view
    def setUp(self): 
        self.client = Client()
        self.login_url = reverse('login')

        #Testing the loginview() to ensure that it responds to GET with a 200 status code
    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html') 
    # STILL NEED TO IMPLEMENT: 
    # test_login_view_authentication()
    # test_loginform_validation()

#IndexViewTest
#Contains all unit tests for the view "indexview()"
class IndexViewTest(TestCase):
        #Set up client and URL for all tests in this view
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        #Testing the indexview() to ensure that it responds to GET with a 200 status code
    def test_index_view_GET(self):
        response = self.client.get(self.index_url) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

### END UNIT TESTS ###

