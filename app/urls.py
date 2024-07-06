from django.urls import path,include
from app import views
from app.models import JobPost



urlpatterns = [
    path('',views.job_list,name='jobs_home'),
    path('job/ <id>',views.job_detail,name='jobs_detail'),
    path('hello123/',views.hello),
]