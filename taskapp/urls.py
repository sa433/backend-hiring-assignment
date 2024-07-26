from django.urls import path
from taskapp.views import home,  project_create, user_signup, user_login, view_projects, del_project, view_client_project, add_task, view_tasks, del_task, view_project_task, upd_task, projects,tasks, single_project,single_task

urlpatterns = [
    path('', user_signup, name='signup'),
    path('login', user_login, name='login'),
    path('home', home, name='home'),
    path('view_projects', view_projects, name='view_projects'),
    path('project/<int:id>/', project_create, name='project_create'),
    path('project_delete/<int:id>/', del_project, name='del_project'),
    path('particular_project/<int:id>/', view_client_project, name='view_client_project'),
    path('add_task/<int:id>/', add_task, name='add_task'),
    path('view_tasks', view_tasks, name='view_tasks'),
    path('del_task/<int:id>/', del_task, name='del_task'),
    path('particular_project_task/<int:id>/', view_project_task, name='view_project_task'),
    path('upd_task/<int:id>/', upd_task, name='upd_task'), 
    path('projects', projects, name='projects'), 
    path('tasks', tasks, name='tasks'), 
    path('single_project/<int:id>/', single_project, name='single_project'),
    path('single_task/<int:id>/', single_task, name='single_task')
]
