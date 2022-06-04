from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Activity
from django.http import JsonResponse



class ActivityView(TemplateView):
    template_name = 'activity.html'

class PostJsonListView(View):
    def get(self, *args, **kwargs):
        upper = kwargs.get('num_posts')
        lower = upper - 3

        posts = list(Activity.objects.values()[lower:upper])
        post_size = len(Activity.objects.all())
        size = True if upper >= post_size else False
        return JsonResponse({'data': posts, 'max': size}, safe=False)
