from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from taskapp.models import ClientModel, TaskModel, ProjectModel
from django.contrib import messages
from datetime import datetime

def user_signup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pw1 = request.POST.get('pw1')
        pw2 = request.POST.get('pw2')
        if pw1 == pw2:
            try:
                user = User.objects.get(username=uname)
                return render(request, 'signup.html', {'msg':'User already registered'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=uname, password=pw1)
                user.save()
                return redirect('login')
        else:
            return render(request, "signup.html", {'msg':'Password not match'})
    else:
        return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pw = request.POST.get("pw")
        usr = authenticate(username=uname, password=pw)
        if usr is None:
            return render(request, "login.html", {"msg":"User Not Found"})
        else:
            login(request, usr)
            return redirect("home")
    else:
        return render(request, "login.html")

def home(request):
    if request.user.is_authenticated:
        client_data = ClientModel.objects.all()
        if request.method == "POST":
            cname = request.POST.get('cname')
            print("cname ",cname)
            c = ClientModel(cname=cname)
            c.save()
            msg = 'Client Added Successfully.'
            return render(request, 'home.html', {'msg':msg,'client_data':client_data})
        else:
            return render(request, 'home.html', {'client_data':client_data})
    else:
        return redirect('login')

def project_create(request, id):
    if request.method == "POST":
        pname = request.POST.get('pname')
        pdesc = request.POST.get('pdesc')
        st_date = datetime.strptime(request.POST.get('st_date'), '%Y-%m-%d').date()
        print("start_date ",st_date)
        end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
        print("end_date ",end_date)

        client = ClientModel.objects.get(id=id)
        print("client ",client)
        # client_name = client.cname
        proj = ProjectModel(pname=pname, pdesc=pdesc, client=client, start_date=st_date, end_date=end_date)
        proj.save()
        return render(request, "create_project.html", {'msg':'project saved successfully'})
    else:
        return render(request, 'create_project.html')

def view_projects(request):
    proj_data = ProjectModel.objects.all()
    return render(request, "view_projects.html", {'proj_data':proj_data})

def view_client_project(request, id):
    client = get_object_or_404(ClientModel, id=id)
    # print("client ",client)
    proj_data = client.clt.all()
    # print("Projects of Client ",proj_data)
    return render(request, "particular_project.html", {'proj_data1':proj_data})

def del_project(request, id):
    if request.method == "POST":
        p = get_object_or_404(ProjectModel, id=id)
        p.delete()
        messages.success(request, "Project Deleted Successfully.")
        return redirect('view_projects')
    return render(request, "view_projects.html")

def add_task(request, id):
    if request.method == "POST":
        tname = request.POST.get('tname')
        tdesc = request.POST.get('tdesc')
        status = request.POST.get('status')

        proj = ProjectModel.objects.get(id=id)
        task = TaskModel(tname=tname, tdesc=tdesc, status=status, proj_name=proj)
        task.save()
        return render(request, "create_task.html", {'msg':'Task Saved Successfully.'})
    else:
        status_choices = TaskModel._meta.get_field('status').choices
        return render(request, 'create_task.html', {'status_choices': status_choices})

def view_tasks(request):
    task_data = TaskModel.objects.all()
    return render(request, "view_tasks.html", {'task_data':task_data})

def del_task(request, id):
    if request.method == "POST":
        t = get_object_or_404(TaskModel, id=id)
        t.delete()
        messages.success(request, "Task Deleted Successfully.")
        return redirect('view_tasks')
    return render(request, "view_tasks.html")

def view_project_task(request, id):
    project = get_object_or_404(ProjectModel, id=id)
    task_data = project.task.all()
    return render(request, "particular_task.html", {'task_data':task_data})

def upd_task(request, id):
    task = TaskModel.objects.get(id=id)
    if request.method == "POST":
        tdesc = request.POST.get('tdesc')
        status = request.POST.get('status')
        
        task.tdesc = tdesc
        task.status = status
        task.save()
        messages.success(request, "Task updated successfully")
        return redirect('view_project_task', id=task.id)
    else:
        status_choices = TaskModel._meta.get_field('status').choices
        return render(request, 'upd_task.html', {'task':task, 'status_choices': status_choices})

################################################################################################################
from rest_framework.response import Response
from taskapp.serializers import ProjectSerializer, TaskSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def projects(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size = 2
        project_data = ProjectModel.objects.all()
        result_page = paginator.paginate_queryset(project_data, request)
        p1 = ProjectSerializer(result_page, many=True)
        return paginator.get_paginated_response(p1.data)

@api_view(['GET'])
def tasks(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size = 2
        task_data = TaskModel.objects.all()
        result_page = paginator.paginate_queryset(task_data, request)
        t1 = TaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(t1.data)
    
@api_view(['GET', 'DELETE'])
def single_project(request,id):
    if request.method == "GET":
        proj = ProjectModel.objects.get(id=id)
        p2 = ProjectSerializer(proj)
        return Response(p2.data)
    elif request.method == "DELETE":
        proj = ProjectModel.objects.get(id=id)
        proj.delete()
        return Response({'msg':'Project Deleted Successfully'}, status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def single_task(request,id):
    if request.method == "GET":
        task = TaskModel.objects.get(id=id)
        t2 = TaskSerializer(task)
        return Response(t2.data)
    elif request.method == "DELETE":
        task = TaskModel.objects.get(id=id)
        task.delete()
        return Response({'msg':'Task Deleted Successfully'}, status=status.HTTP_200_OK)