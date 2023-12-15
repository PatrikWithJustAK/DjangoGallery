from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtPieceForm
from .models import ArtPiece

from django.contrib.auth.decorators import login_required

@login_required
def add_artpieceview(request):
    if request.method == 'POST':
        form = ArtPieceForm(request.POST, request.FILES)
        if form.is_valid():
            artpiece = form.save(commit=False)
            artpiece.uploader = request.user
            artpiece.save()
            return redirect('dashboard')  # Redirect to a success page or home page
    else:
        form = ArtPieceForm()

    return render(request, 'add-artpiece.html', {'form': form})
def galleryindexview(request):
    images = ArtPiece.objects.filter(uploader=request.user)
    gallery = images.order_by('-created_at')
    context = {"gallery" : gallery}
    return render(request, 'dashboard.html', context)
