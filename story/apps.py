from django.apps import AppConfig


class StoryConfig(AppConfig):
    name = 'story'




class IndexView(TemplateView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):

        recents = Post.objects.order_by('-timestamp')[0:4]
        recent = Post.objects.order_by('timestamp')[0:1]
        context = super().get_context_data(**kwargs)
        context['recents'] = recents
        context['recent'] = recent
        return context

class PageView(ListView):
    model = Post
    template_name = 'foods.html'
    context_object_name = 'queryset'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        recent = Post.objects.order_by('timestamp')[0:3]
        context = super().get_context_data(**kwargs)
        context['recent'] = recent
        #context['page_request_var'] = "page"
        return context

class CategoryDetailView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'slider.html'