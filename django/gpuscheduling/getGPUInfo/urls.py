from django.urls import path, include
#from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    path('getGPUInfo/', include('getGPUInfo.urls')),
#    path('admin/', admin.site.urls),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
