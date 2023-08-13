from django.shortcuts import render
from movieapp.models import movie
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

# def index(request):
#     movie=Movie.objects.all()
#     context={'movie_list':movie}
#     return render(request,"base.html",context)
class Movielistview(ListView):
    model=movie
    template_name="base.html"
    context_object_name="movie_list"

class Moviedetailview(DetailView):
    model=movie
    template_name="detail.html"
    context_objects_name="movie"

class createview(CreateView):
        model = movie
        template_name = "addmovie.html"
        fields=['name','desc','years','img']
        success_url=reverse_lazy('movieapp:index')


class updateview(UpdateView):
    model = movie
    template_name = "addmovie.html"
    fields = ['name', 'desc', 'years', 'img']
    success_url = reverse_lazy('movieapp:index')

class deleteview(DeleteView):
        model = movie
        template_name = "delete.html"
        success_url = reverse_lazy('movieapp:index')


# def addmovie(request):
#     if(request.method=="POST"):
#         n=request.POST['n']
#         d=request.POST['d']
#         y=request.POST['y']
#         i=request.FILES['i']
#         m=movie.objects.create(name=n, desc=d, years=y, img=i)
#         m.save()
#         return home(request)
#     return render(request,'addmovie.html')


# def home(request):
#     m=movie.objects.all()
#     return render(request,'home.html',{'m':m})
# def viewmovie(request):
#     m=movie.objects.get()
#     return render(request,'viewmovie.html',{'m':m})