from django.contrib import admin
from django.urls import path
from toiletapp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name = 'main'),
    path('main2/', views.main2, name="main2"),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('review/', views.review, name = 'review'),
    path('new/', views.new, name="new"),
    path('create/', views.create, name = 'create'),
    # path('<str:id>', views.detail, name = 'detail'),
    # path('edit/<str:id>', views.edit, name = 'edit'),
    # path('update/<str:id>', views.update, name = 'update'),
    # path("comment", views.comment, name="comment"),
    path('detail_com/', views.detail_com, name = 'detail_com'),
    path('detail/', views.detail, name = "detail"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
