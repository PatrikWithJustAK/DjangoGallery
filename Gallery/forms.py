from django import forms
from .models import ArtPiece

class ArtPieceForm(forms.ModelForm):
    class Meta:
        model = ArtPiece
        fields = ['title', 'image', 'description']

        # Adding tailwind classes for better control over HTML rendering
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control, bg-gray-300, grid, row-span-1'}),
            'description': forms.Textarea(attrs={'class': 'form-control, grid, row-span 1'}),
            # Image upload field:
            'image': forms.FileInput(attrs={'class': 'form-control-file, grid, row-span 1'}),
        }
