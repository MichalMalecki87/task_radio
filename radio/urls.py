from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from radio import views

urlpatterns = [
    path('hits/', views.ListCreateHitsView.as_view()),
    path('hits/<str:title_url>', views.hit_details),
    path('hits/test/<str:title_url>', views.ModifyHitView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)