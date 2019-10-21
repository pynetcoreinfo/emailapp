from . import views
from django.urls import path
from django.conf.urls import url



urlpatterns = [
    url(r'^$',views.EmailListView.as_view(),name='mail-list'),
    #path('home/',views.home,name='mail-home'),
    path('user/<str:username>',views.UserEmailList.as_view(),name='mail-detail'),
    path('email/<int:pk>/',views.EmailDetail.as_view() ,name='mail-detail'),
    url(r'^email/new', views.send_email, name='mail-create'),

#url(r'^$', views.LIST.as_view(), name='list'),
]
