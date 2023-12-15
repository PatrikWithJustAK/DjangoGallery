from django.shortcuts import render, redirect
from .forms import ArtPieceForm
from django.contrib.auth.decorators import login_required

@login_required
def add_artpieceview(request):
    if request.method == 'POST':
        form = ArtPieceForm(request.POST, request.FILES)
        if form.is_valid():
            artpiece = form.save(commit=False)
            artpiece.uploader = request.user
            artpiece.save()
            return redirect('index')  # Redirect to a success page or home page
    else:
        form = ArtPieceForm()

    return render(request, 'add-artpiece.html', {'form': form})
def galleryindexview(request):
    context = {}
    return render(request, 'index.html', context)
