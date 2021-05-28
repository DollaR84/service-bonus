from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('balance/', views.BonusBalance.as_view()),
    path('operations/', views.OperationList.as_view()),
    path('operations/<int:pk>/', views.OperationDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
