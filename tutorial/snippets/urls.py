from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
#from tutorial.snippets.views import api_view
from snippets import views

urlpatterns = [
    path('tasks/', views.task_list),
    path('tasks/<int:id>', views.task_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
