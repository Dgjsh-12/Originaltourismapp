from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="polls/login.html"), name='login'),
    path('index.html', views.index),
    path('kyoto.html', views.kyoto),
    path('kyotocty.html', views.kyotocty),
]
