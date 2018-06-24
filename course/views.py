# coding=utf-8
from django.shortcuts import render_to_response, render
from django.views import generic

from course.models import App, AppCategory


class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return App.objects.order_by("id")[:6]


class AppView(generic.ListView):
    template_name = 'course.html'

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            return App.objects.filter(title__icontains=search)
        category_id = self.request.GET.get("category_id")
        if category_id:
            return App.objects.filter(category_id=category_id)
        return App.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AppView, self).get_context_data(**kwargs)
        context['categories'] = AppCategory.objects.all()
        return context


def get_id(request,pk):
    list = App.objects.get(id=pk)
    context = {}
    context['list']= list
    return render(request,'course-intro.html',context)


class ContactView(generic.View):
    def get(self, *args, **kwargs):
        return render_to_response(template_name='contact.html')

