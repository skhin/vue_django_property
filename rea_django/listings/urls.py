from django.urls import path, include
from listings import views

urlpatterns = [
    path('latest-listings/', views.LatestListingsList.as_view()),
    path('listings/search/', views.search),
    path('listings/<slug:country_slug>/<slug:listings_slug>/', views.ListingsDetail.as_view()),
    path('listings/<slug:country_slug>/', views.CountryDetail.as_view())
    
]