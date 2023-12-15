from django.contrib import admin
from .models import ArtPiece

class ArtPieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader', 'created_at', 'image_tag')
    search_fields = ['title', 'description']
    list_filter = ('created_at',)

    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="150" height="150" />'
        return "-"
    image_tag.short_description = 'Image'

admin.site.register(ArtPiece, ArtPieceAdmin)