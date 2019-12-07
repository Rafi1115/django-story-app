from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.views.generic import (View, ListView, 
            TemplateView, DetailView, CreateView, UpdateView, DeleteView)
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
from .models import Post, Author, PostView, Category, Recipe, FeaturedPost, Advertise


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

class SearchView(View):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(overview__icontains=query)
            ).distinct()
        context = {
            'queryset': queryset
        }
        return render(request, 'search_results.html', context)

class IndexView(TemplateView):
    model = Post
    model = Recipe
    model = Category
    model = FeaturedPost
    model = Advertise
    template_name = 'index.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):

        recents = Post.objects.order_by('-timestamp')[0:4]
        recent = Post.objects.order_by('timestamp')[0:1]
        featured = FeaturedPost.objects.filter()[0:3]
        recipe = Recipe.objects.filter()[0:2]
        category = Category.objects.all()[0:4]
        advertise = Advertise.objects.filter()[0:5]
        
        context = super().get_context_data(**kwargs)
        context['recents'] = recents
        context['recent'] = recent
        context['recipe'] = recipe
        context['featured'] = featured
        context['advertise'] = advertise
        context['category'] = category
        return context


class IndexDetailView(DetailView):
    model= Post
    context_object_name = 'queryset'
    template_name = 'single.html'
    
class AdDetailView(DetailView):
    model= Advertise
    context_object_name = 'queryset'
    template_name = 'single.html'

class ReDetailView(DetailView):
    model= Recipe
    context_object_name = 'queryset'
    template_name = 'single.html'

class FeDetailView(DetailView):
    model= FeaturedPost
    context_object_name = 'queryset'
    template_name = 'single.html'



class PageView(ListView):
    model = Post
    template_name = 'foods.html'
    context_object_name = 'queryset'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        recent = Post.objects.order_by('timestamp')[0:3]
        context = super().get_context_data(**kwargs)
        context['recent'] = recent
        context['page_request_var'] = "page"
        return context
    
# class PostCategory(ListView):
#     model = Post
#     template_name = 'cat.html'
#     def get_queryset(self):
#         self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
#         return Post.objects.filter(category=self.category)

#     def get_context_data(self, **kwargs):
#         context = super(PostCategory, self).get_context_data(**kwargs)
#         context['category'] = self.category
#         return context


class CategoryDetailView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'slider.html'


class SingleView(TemplateView):
    template_name = 'single.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class StyleView(TemplateView):
    template_name = 'lifestyle.html'


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

