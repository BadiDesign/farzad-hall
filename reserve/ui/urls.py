from django.urls import path

from badi_utils.dynamic import model_to_path, generate_url, multi_generator_url
from .views import *
from ..models import Reserve

reserve_urls = multi_generator_url(Reserve(), create=ReserveCreateView, update=ReserveUpdateView, )
urlpatterns = [
                  path('reserve/detail/<int:pk>', ReserveDetailView.as_view(), name='reserve_detail')
              ] + reserve_urls
