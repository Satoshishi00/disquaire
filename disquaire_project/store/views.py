from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.template import loader

from .models import Album, Artist, Contact, Booking


def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    context = { 'albums': albums }
    return render(request, 'store/index.html', context)


def listing(request):
    albums = Album.objects.filter(available=True)
    context = { 'albums': albums }
    return render(request, 'store/listing.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artists_name = " ".join([artist.name for artist in album.artists.all()])
    context = {
        'album_title': album.title,
        'artist_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }
    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')
    

    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)

    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }

    return render(request, 'store/search.html', context)
