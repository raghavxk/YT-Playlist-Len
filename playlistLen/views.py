from django.shortcuts import render, redirect
from .forms import URLform
from django.http import HttpResponse
from .script import playlistId


def main(request):
    if request.method == "POST":
        form = URLform(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get("url_of_playlist")
            try:
                playtime = playlistId(url)
            except:
                playtime = "Please enter a valid YouTube playlist URL."
            context = {"time": playtime}
            return render(request, "playlistLen/result.html", context)
        
    else:
        form = URLform()
        context = {"form": form}
        return render(request, "playlistLen/home.html", context)
