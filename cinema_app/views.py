from django.shortcuts import render, get_object_or_404, redirect
from . models import Movies, Comment, Rating, Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm, RatingForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

@login_required
def index(request):
  
        
    favourite_count = request.user.favourite.count()
    
    return render(request, 'core/index.html',{'favourite_count':favourite_count})


def base(request):
    favourite_count = request.user.favourite.count()
    
    return render(request, 'core/base.html',{'favourite_count':favourite_count})


def movie(request):
    movies = Movies.objects.all().order_by('-id')
    favourite_count = request.user.favourite.count()
    form = CommentForm()
    category = Category.objects.all()
    query = request.GET.get('query', '')
    if query:
        movies = movies.filter((Q(name__icontains=query) | Q(movie__name__icontains=query)))
        if not movies:
            pass
        else:
            movies = movies.all()

    return render(request, 'core/movies.html',{'title':'Movie',"movies":movies,'favourite_count':favourite_count,'form':form,'query':query, 'category':category})

@csrf_exempt
def like(request):
    if request.POST.get('action') == 'post':
        result=  ''
        id = int(request.POST.get('movieid'))
        movie_like = get_object_or_404(Movies, id=id)
        
        if movie_like.like.filter(id=request.user.id).exists():
            movie_like.like.remove(request.user)
            movie_like.like_count -= 1
            result = movie_like.like_count
            movie_like.save()
            
        else:
            movie_like.like.add(request.user)
            movie_like.like_count += 1
            result =  movie_like.like_count
            movie_like.save()
            
        return JsonResponse({'result':result})
    

def favourites_list(request):
    favourite = Movies.objects.filter(favourites=request.user)
    favourite_count = request.user.favourite.count()
    
    return render(request, 'core/favourites_list.html', {'favourite':favourite,'favourite_count':favourite_count})

def favourite_add(request, pk):
    
    if request.method == 'POST':
        movie = get_object_or_404(Movies, pk=pk)
        
        if movie.favourites.filter(id=request.user.id).exists():
            movie.favourites.remove(request.user)
            added = False
        
        else:
            movie.favourites.add(request.user)
            
            added = True
        
        favourite_count = request.user.favourite.count()
        
        return JsonResponse({'added':added, 'favourite_count':favourite_count})
    return JsonResponse({'error':'Invalid request method'}, status=405)



@csrf_exempt
def movie_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            movie_id = request.POST.get('movie_id')
            try:
                movie = Movies.objects.get(id=movie_id)
            except Movies.DoesNotExist:
                return JsonResponse({'success':False, 'error':'post not found '})
            
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            
            return JsonResponse({'success':True, 'comment':comment.content, 'user':comment.user.username})
        
    return JsonResponse({'success':False})


