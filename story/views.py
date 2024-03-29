from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.views.generic import (View, ListView, FormView,
            TemplateView, DetailView, CreateView, UpdateView, DeleteView)
from django.views import generic
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
from itertools import chain
from .models import Post, Author, PostView, Category, Recipe, FeaturedPost, Advertise
from taggit.models import Tag

# class TagMixin(object):
#     def get_context_data(self, **kwargs):
#         context = super(TagMixin, self).get_context_data(**kwargs)
#         context['category'] = Category.objects.all()
#         return context


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


class SearchView(View):
    def get(self, request, *args, **kwargs):  
        queryset1 = Post.objects.all()
        queryset2 = Advertise.objects.all()
        queryset3 = FeaturedPost.objects.all()
        queryset4 = Recipe.objects.all()
        query = request.GET.get('q')
        if query:
            queryset1 = queryset1.filter(Q(title__icontains=query)|Q(overview__icontains=query)).distinct()
            queryset2 = queryset2.filter(Q(title__icontains=query)|Q(overview__icontains=query)).distinct()
            queryset3 = queryset3.filter(Q(title__icontains=query)|Q(overview__icontains=query)).distinct()
            queryset4 = queryset4.filter(Q(title__icontains=query)|Q(overview__icontains=query)).distinct()
            queryset = list(
                sorted(
                    chain(queryset1, queryset2, queryset3, queryset4),
                    key=lambda objects: objects.pk
                ))
        context = {
            'queryset': queryset,
          
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
        advertise = Advertise.objects.filter()[0:5]
        category = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['recents'] = recents
        context['recent'] = recent
        context['recipe'] = recipe
        context['featured'] = featured
        context['advertise'] = advertise
        context['category'] = category
        return context



class IndexDetailView(DetailView):
    model = Post
    context_object_name = 'queryset'
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        tags = Post.tags.all()
        category = Category.objects.all()
        recents = Post.objects.order_by('-timestamp')[0:4]  
        context = super().get_context_data(**kwargs)
        context['recents'] = recents
        context['category'] = category
        context['tags'] = tags
        return context

# class RecentDetailView(DetailView):
#     model= Post
#     context_object_name = 'queryset'
#     template_name = 'sing.html'

class AdDetailView(DetailView):
    model= Advertise
    context_object_name = 'queryset'
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        tags = Post.tags.all()
        recents = Post.objects.order_by('-timestamp')[0:4]  
        context = super().get_context_data(**kwargs)
        context['recents'] = recents
        context['tags'] = tags
        return context

class ReDetailView(DetailView):
    model= Recipe
    context_object_name = 'queryset'
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        tags = Post.tags.all()
        recents = Post.objects.order_by('-timestamp')[0:4]  
        context = super().get_context_data(**kwargs)
        context['recents'] = recents
        context['tags'] = tags
        return context
  

class FeDetailView(DetailView):
    model= FeaturedPost
    context_object_name = 'queryset'
    template_name = 'single.html'
    
    def get_context_data(self, **kwargs):
        tags = Post.tags.all()
        recents = Post.objects.order_by('-timestamp')[0:4]  
        context = super().get_context_data(**kwargs)
        context['recents'] = recents
        context['tags'] = tags
        return context
  



class PageView(ListView):
    model = Post
    template_name = 'foods.html'
    context_object_name = 'queryset'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        recent = Post.objects.order_by('timestamp')[0:4]
        category = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['recent'] = recent
        context['category'] = category
        #context['page_request_var'] = "page"
        return context

# class TagList(ListView):
#     model = Post
#     template_name = 'loan.html'
#     context_object_name = 'tags'

#     def get_context_data(self, **kwargs):
#         tags = Post.tags.all()
#         context = super().get_context_data(**kwargs)
#         context['tags'] = tags
#         #context['page_request_var'] = "page"
#         return context
        
    
class TagIndexView(ListView):
    model = Post
    model = Category
    paginate_by = 2
    template_name = 'sing.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        category = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
        
    def get_queryset(self):
        tags = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Post.objects.filter(tags=tags)

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

class ListCategory(ListView):
    model = Post
    model = Category
    template_name = 'shit.html'  # :)
    context_object_name = 'queryset'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        category = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

class CategoryDetailView(generic.DetailView, MultipleObjectMixin):
    model = Post
    model = Category
    context_object_name = 'queryset'
    template_name = 'slider.html'
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        category = Category.objects.all()
        object_list = Category.objects.all()
        context = super(CategoryDetailView, self).get_context_data(object_list=object_list, **kwargs)
        context['category'] = category
        return context

    # def get_context_data(self, **kwargs):
    #     category = Category.objects.all()
    #     object_list = Category.objects.filter(post=self.get_object())
    #     context = super(CategoryDetailView, self).get_context_data(object_list=object_list, **kwargs)
    #     context['category'] = category
    #     return context


class StyleView(ListView):
    model = Category
    model = Post
    template_name = 'lifestyle.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        category = Category.objects.all()
       # category = Post.category.filter(featured=True)
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

 
class CategorylView(generic.DetailView):
    model = Category
    context_object_name = 'queryset'
    template_name = 'slider.html'
   


class SingleView(TemplateView):
    template_name = 'single.html'

class AboutView(TemplateView):
    model = Category
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        category = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class ContactView(FormView):
    model = Category
    form_class = ContactForm
    success_url = reverse_lazy('contact') # we can have a specific page here..
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        category = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        from_email = form.cleaned_data['email']
        message = form.cleaned_data['message']  
        # emails = ['youremail@gmail.com']
        try:
            send_mail(name, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return super(ContactView, self).form_valid(form)


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

