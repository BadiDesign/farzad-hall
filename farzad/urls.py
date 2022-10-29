from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from farzad import settings
from farzad.public_views import *

from reserve.ui.views import *

handler404 = 'farzad.public_views.my_custom_page_not_found_view'

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # Public Views
                  path('', IndexView.as_view(), name='index'),
                  path('video', ReservesView.as_view(), name='video'),
                  path('video/<int:pk>', ReserveView.as_view(), name='video'),

                  # Dashboard Views
                  path('dashboard', DashboardView.as_view(), name='dashboard'),
                  path('dashboard/', include('badi_user.ui.urls')),
                  path('dashboard/', include('badi_ticket.urls')),
                  path('dashboard/wallet/', include('badi_wallet.ui.urls')),
                  path('dashboard/', include('reserve.ui.urls')),

                  # Api Views
                  path('api/v1/', include('badi_user.api.routers')),
                  path('api/v1/', include('badi_wallet.api.routers')),
                  path('api/v1/', include('badi_ticket.routers')),
                  path('api/v1/', include('reserve.api.routers')),

                  # Select2 Views
                  path('select2/', include('farzad.select2_urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
