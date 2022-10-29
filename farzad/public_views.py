from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from badi_utils.utils import LoginRequiredMixin

from reserve.models import *


class IndexView(TemplateView):
    extra_context = {
        'title': 'صفحه اصلی'
    }
    template_name = "index.html"


class ReservesView(ListView):
    extra_context = {
        'title': 'ویدیو ها'
    }
    template_name = "reserves.html"
    paginate_by = 12
    model = Reserve


class ReserveView(DetailView):
    template_name = "reserve.html"
    model = Reserve

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_reserves'] = context['object'].category.films.exclude(id=context['object'].id)[:4]
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    extra_context = {
        'title': 'Dashboard',
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser and not request.user.is_admin:
            request.user.is_admin = True
            request.user.save()
        if not request.user.is_admin:
            return redirect('/')
        return super().get(request, *args, **kwargs)

    def get_template_names(self):
        return 'dashboard.html'


class NotFound404(TemplateView):
    template_name = '404.html'


def my_custom_page_not_found_view(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response
