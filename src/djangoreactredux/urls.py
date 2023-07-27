from django.conf import Settings
from django.urls import include, path  # Updated import here
from django.views.decorators.cache import cache_page

from base import views as base_views

urlpatterns = [
    path('api/v1/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/v1/getdata/', include('base.urls', namespace='base')),

    # catch all others because of how history is handled by react router - cache this page because it will never change
    path('', cache_page(Settings.PAGE_CACHE_SECONDS)(base_views.IndexView.as_view()), name='index'),
]
