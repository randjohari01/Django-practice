from django.shortcuts import render

from .models import article

def year_archive(request, year):
    a_list = article.objects.filter(date__year=year)
    context = {"year": year,"article_list": a_list }
    return render(request,"news/year_archive.html",context)
   