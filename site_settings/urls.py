from django.urls import path
from .views import SiteSettingList, LanguageList, AdList, PineconeIndexList

app_name = 'site_settings'

urlpatterns = [
    # SiteSettings list endpoint
    path('settings/', SiteSettingList.as_view(), name='settings-list'),

    # Languages list endpoint
    path('languages/', LanguageList.as_view(), name='languages-list'),

    # Ads list endpoint
    path('ads/', AdList.as_view(), name='ads-list'),

    # Pinecone Idx list endpoint
    path('pinecone/', PineconeIndexList.as_view(), name='pinecone-index'),
]
