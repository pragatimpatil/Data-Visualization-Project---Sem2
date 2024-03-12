from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/details1/<int:id>', views.details1, name='details1'),
    path('tasks/details2/<int:id>', views.details2, name='details2'),
    path('tasks/details3/<int:id>', views.details3, name='details3'),
    path('tasks/details4/<int:id>', views.details4, name='details4'),
    path('tasks/dv/<int:id>', views.dv, name='dv'),
    path('tasks/dot/<int:id>', views.dot, name='dot'),
    path('tasks/line/<int:id>', views.line, name='line'),
    path('tasks/heatmap/<int:id>', views.heatmap, name='heatmap'),
    path('tasks/pie/<int:id>', views.pie, name='pie'),
    path('tasks/scatter/<int:id>', views.scatter, name='scatter'),
    path('tasks/dendogram/<int:id>', views.dendogram, name='dendogram'),
    path('tasks/histogram/<int:id>', views.histogram, name='histogram'),
    path('tasks/boxplot/<int:id>', views.boxplot, name='boxplot'),
    path('tasks/qq/<int:id>', views.qq, name='qq'),
    path('tasks/bar/<int:id>', views.bar, name='bar'),
    path('tasks/knn/<int:id>', views.knn, name='knn'),
    path('tasks/lr/<int:id>', views.lr, name='lr'),
    path('tasks/ift/<int:id>', views.ift, name='ift'),
    path('tasks/gmm/<int:id>', views.gmm, name='gmm'),
    path('tasks/kms/<int:id>', views.kms, name='kms'),
]

urlpatterns += staticfiles_urlpatterns()