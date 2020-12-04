from django.urls import path
from . import views # this indicates that the views file can be found in the same directory a s this file
# urlpatterns = [
#     path('', views.index), # '' just means the local host

#     path('bears', views.one_method),

#     path('bears/<int:my_val', views.another_method), # matches localhost:8000/bears

#     path('bears/<str:name>/poke', views.yet_another),# would match localhost:8000/bears/pooh/poke

#     path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown

# ]

urlpatterns = [
    path('', views.root_method),
    path('another_route', views.another_method),
    path('redirected_route', views.redirected_method)

]