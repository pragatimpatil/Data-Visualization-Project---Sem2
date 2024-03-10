from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/details1/<int:id>', views.details1, name='details1'),
    path('tasks/details2/<int:id>', views.details2, name='details2'),
    path('tasks/details3/<int:id>', views.details3, name='details3'),
    path('tasks/details4/<int:id>', views.details4, name='details4'),
]

urlpatterns += staticfiles_urlpatterns()