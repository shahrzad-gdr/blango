from django.urls import path
# import blog.views
from blog import views
urlpatterns = [
    # other patterns
    path("", views.index, name='index')
]
