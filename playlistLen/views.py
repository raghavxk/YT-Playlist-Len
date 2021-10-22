from django.shortcuts import render, redirect
from .forms import URLform
from django.http import HttpResponse
from .script import playlistId


def main(request):
    if request.method == "POST":
        form = URLform(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get("url_of_playlist")
            playtime = playlistId(url)
            context = {"time": playtime}
            return render(request, "playlistLen/result.html", context)
        else:
            return HttpResponse("<h1>hello</h1>")
    else:
        form = URLform()
        context = {"form": form}
        return render(request, "playlistLen/home.html", context)
