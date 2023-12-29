from django.core.files.uploadedfile import SimpleUploadedFile
import io
from CustomUser.models import User
from PIL import Image
from .models import ArtPiece
from .forms import ArtPieceForm
from django.test import TestCase
from django.urls import reverse

class AddArtPieceViewTest(TestCase):

    def setUp(self):
        # Create a dummy user for testing
        self.user = User.objects.create_user(email='T3Sting123@test.com', password='T3stC@sE12345')
        self.client.login(email='T3Sting123@test.com', password='T3stC@sE12345')

    def generate_test_image(self):
        # Create an image file
        file = io.BytesIO()
        image = Image.new('RGB', (100, 100), color = 'red')
        image.save(file, 'PNG')
        file.name = 'test.png'
        file.seek(0)
        return file
    

    def test_post_request_with_valid_image(self):
        # Generate a test image
        test_image = self.generate_test_image()
        uploaded_file = SimpleUploadedFile('test.png', test_image.read(), content_type='image/png')

        form_data = {
            'title': 'Test Art',
            'description': 'A test art piece',
            # Other fields as required
            'image': uploaded_file,  # Include the image file here
        }
        response = self.client.post(reverse('add_artpiece'), form_data)
        self.assertEqual(response.status_code, 302)  # 302 is HTTP Redirect status code - add-artpiece should redirect to 'dashboard' on success
        self.assertTrue(ArtPiece.objects.exists())  # Check if ArtPiece was created
        
    def test_get_request_returns_form(self):
        response = self.client.get(reverse('add_artpiece'))
        self.assertEqual(response.status_code, 200) #Check HTTP-OK response code
        self.assertIsInstance(response.context['form'], ArtPieceForm) #a blank form should be generated as context for get requests


class DashboardViewTest:
    def setUp(self):
        # Create a dummy user for testing auth
        self.user = User.objects.create_user(email='T3Sting123@test.com', password='T3stC@sE12345')

    def test_add_artpiece_view_authentication_required(self):
        # Test dashboard without logging in
        response = self.client.get(reverse('dashboard'))
        self.assertNotEqual(response.status_code, 200)#should not return 200 as view @require_login 

        # Test dashboard response with login
        self.client.login(email='T3Sting123@test.com', password='T3stC@sE12345')
        response = self.client.get(self.add_artpiece_url)
        self.assertEqual(response.status_code, 200) #authenticated user gets 200 code



