from django.db import models
from CustomUser.models import User

class ArtPiece(models.Model):
    # Foreign Key to link the artwork to a user
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    # Image field for the artwork
    image = models.ImageField(upload_to='static/art_pieces')

    # Additional fields
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def usergallery(self, user):
        userid = user.id 
        galleryquery = self.objects.filter(uploader=userid)

        return galleryquery