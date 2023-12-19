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

@login_required
def deleteartpiece_view(request, pk):
    if request.method == 'DELETE':
        artpiece = get_object_or_404(ArtPiece, id=pk, uploader=request.user)
        artpiece.delete()
        return redirect('dashboard')  # Redirect to gallery dashboard on delete
    else:
        return redirect('dashboard') 
    
def galleryindexview(request):
    images = ArtPiece.objects.filter(uploader=request.user) #filter all pieces the user has created
    gallery = images.order_by('-created_at') #filter by newest (this may be worth altering default in models.py)
    context = {"gallery" : gallery} #The template has access to the gallery as an array of ArtPieces
    return render(request, 'dashboard.html', context)
