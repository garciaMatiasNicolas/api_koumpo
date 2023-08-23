from django.urls import path
from users.views import UserEndpoints

read_all = UserEndpoints.read_all
detail_user = UserEndpoints.detail_user
create = UserEndpoints.create

urlpatterns = [
    path('get-all/', read_all, name='get_users'),
    path('detail/<int:pk>/', detail_user, name='get_user_id'),
    path('create/', create, name='create_user')
]