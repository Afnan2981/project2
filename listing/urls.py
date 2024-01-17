from django.urls import path
from .views import ListingsView, ManageListingView, ListingDetailView, SearchListingsView 

urlpatterns = [
    path('manage/', ManageListingView.as_view(), name='manage_listing'),  
    path('detail/<slug:slug>/', ListingDetailView.as_view(), name='listing_detail'),
    path('get-listings/', ListingsView.as_view(), name='get_listings'),  # Updated URL name
    path('search/', SearchListingsView.as_view(), name='search_listings'),
]
