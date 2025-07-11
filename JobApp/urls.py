from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('recruiter_login/',views.recruiter_login,name='recruiter_login'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_signup/',views.user_signup,name='user_signup'),
    path('user_home/',views.user_home,name='user_home'),
    path('Logout/',views.Logout,name='Logout'),
    path('recruiter_signup/',views.recruiter_signup,name='recruiter_signup'),
    path('recruiter_home/',views.recruiter_home,name='recruiter_home'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('view_users/',views.view_users,name='view_users'),
    path('delete_user/<int:pk>/',views.delete_user,name='delete_user'),
    path('pending_recruiters/',views.pending_recruiters,name='pending_recruiters'),
    path('change_status/<int:pk>/',views.change_status,name='change_status'),
    path('accepted_recruiters/',views.accepted_recruiters,name='accepted_recruiters'),
    path('rejected_recruiters/',views.rejected_recruiters,name='rejected_recruiters'),
    path('all_recruiters/',views.all_recruiters,name='all_recruiters'),
    path('delete_recruiter/<int:pk>/',views.delete_recruiter,name='delete_recruiter'),
    path('change_password_admin/',views.change_password_admin,name='change_password_admin'),
    path('change_password_user/',views.change_password_user,name='change_password_user'),
    path('change_password_recruiter/',views.change_password_recruiter,name='change_password_recruiter'),
    path('add_job/',views.add_job,name='add_job'),
    path('job_list/',views.job_list,name='job_list'),
    path('edit_job_detail/<int:pk>/',views.edit_job_detail,name='edit_job_detail'),
    path('change_company_logo/<int:pk>/',views.change_company_logo,name='change_company_logo'),
    path('latest_jobs/',views.latest_jobs,name='latest_jobs'),
    path('job_list_user/',views.job_list_user,name='job_list_user'),
    path('job_detail/<int:pk>/',views.job_detail,name='job_detail'),
    path('apply_for_job/<int:pk>/',views.apply_for_job,name='apply_for_job'),
    path('candidate_applied/',views.candidate_applied,name='candidate_applied'),
    path('delete_candidate_application/<int:pk>/',views.delete_candidate_application,name='delete_candidate_application'),
    path('delete_job/<int:pk>/',views.delete_job,name='delete_job'),
    path('contact/',views.contact,name='contact'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)