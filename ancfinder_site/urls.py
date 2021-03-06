from django.urls import path
from django.views.generic import TemplateView
from ancfinder_site.views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(template_name="ancfinder_site/index.html"), name='ancfinder_site_home'),
    path('about/', AboutTemplateView.as_view(template_name="ancfinder_site/about.html"), name="ancfinder_site_about"),
    path('what_are_ancs/', AboutTemplateView.as_view(template_name="ancfinder_site/what_are_ancs.html"), name="ancfinder_site_what_are_ancs"),
    path('explore_ancs/', ExploreAncs.as_view(template_name="ancfinder_site/explore_ancs.html"), name="ancfinder_site_explore_ancs"),
    path('api/locationSearch', location_search, name='api_location_search'),
    path('api/anc-geojson', fetch_anc_data, name='api-anc-geojson')
]
