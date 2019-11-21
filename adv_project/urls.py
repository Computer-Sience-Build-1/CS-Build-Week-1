from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
# from rest_framework.authtoken import views as drf_views
from rest_framework.authtoken import views
# from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('login/', views.obtain_auth_token, name='auth')
    # path('registration/')
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]
