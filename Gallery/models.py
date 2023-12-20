from django.db import models
from django import forms
from CustomUser.models import User 
from django.template.defaultfilters import filesizeformat #for file sizing
from django.utils.translation import gettext_lazy as _

class ImageOnlyRestrictedFileField(models.FileField): #inheriting filefield to add additional restrictions on filetype/size
        
        


        def __init__(self, *args, **kwargs):
            self.content_types = ['image/gif', 'image/jpeg', 'image/png', ]
            self.max_upload_size = 5242880 #5mb

            super(ImageOnlyRestrictedFileField, self).__init__(*args, **kwargs)

        def clean(self, *args, **kwargs):
            data = super(ImageOnlyRestrictedFileField, self).clean(*args, **kwargs)
            file = data.file
            try:
                content_type = file.content_type
                if content_type in self.content_types:
                    if file._size > self.max_upload_size:
                        raise forms.ValidationError(_('Please keep filesize under'
                                                    '%s. Current filesize %s')
                                                    % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
                else:
                    raise forms.ValidationError(_('Filetype not supported.'))
            except AttributeError:
                pass

            return data

class ArtPiece(models.Model):
    # Foreign Key to link the artwork to a user
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    # Image field for the artwork
    image = ImageOnlyRestrictedFileField(upload_to='static/art_pieces')

    # Additional fields
    title = models.CharField(max_length=100,)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def usergallery(self, user):
        userid = user.id 
        galleryquery = self.objects.filter(uploader=userid)

        return galleryquery