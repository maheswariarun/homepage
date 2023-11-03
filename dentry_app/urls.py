from django.urls import path
from dentry_app import views
from django.conf.urls.static import static
from dataentry import settings

urlpatterns=[
    path('home',views.home),
    path('login',views.user_login),
    path('register',views.user_register),
    path('logout',views.user_logout),
    path('pdetails/<pid>',views.product),

 #   path('addcart/<pid>',views.addcart),
   # path('viewcart',views.viewcart),
   # path('remove/<cid>',views.remove)
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)