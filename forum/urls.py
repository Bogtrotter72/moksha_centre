from django.urls import path
from .views import post_detail, post_list


app_name = 'forum'
urlpatterns = [
    path('', post_list, name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', post_detail, name="post_detail"),
]