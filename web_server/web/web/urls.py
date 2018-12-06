from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


# from .views import login_redirect
from users import views as user_views

# we can have url keyword for matching
urlpatterns = [
    path('admin/', admin.site.urls),

    # url(r'^$', login_redirect, name='login_redirect'),

    path('', include('blog.urls')),
    path('register', user_views.register, name='register'),
    path('profile', user_views.profile, name='profile'),
    path('activate/<uidb64>/<token>/', user_views.activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # url(r'^signup/$', views.signup, name='signup'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)