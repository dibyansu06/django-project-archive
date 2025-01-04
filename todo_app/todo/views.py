from django.shortcuts import render, get_object_or_404, redirect
from datetime import date
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
def task_list(request):
    if request.method == "POST":
        task_title = request.POST.get('task')
        task_priority = request.POST.get("priority")
        due_date = request.POST.get("due_date")
        if task_title:
            Task.objects.create(title=task_title, priority=task_priority, due_date=due_date)
        return redirect('task_list')
    
    filter_option = request.GET.get('filter', 'all')
    tasks = []
    if filter_option == "completed":
        tasks = Task.objects.filter(completed=True)
    elif filter_option == 'pending':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()
    
    overdue_tasks = tasks.filter(due_date__lt=date.today(), completed=False) 
    
    return render(request, 'todo/task_list.html', {"tasks": tasks, "overdue_tasks": overdue_tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

def delete_task(request, task_id):
    print(f"Task ID: {task_id}")
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed 
    task.save()
    return redirect('task_list')

@csrf_exempt
def update_task_order(request):
    if request.method == "POST":
        try: 
            data = json.loads(request.body)
            task_ids = data.get('order', [])

            if not isinstance(task_ids, list):
                return JsonResponse({'status' : 'error', 'message' : 'Invalid data format'}, status=400)
            
            for index, task_id in enumerate(task_ids):
                task = Task.objects.get(id=task_id)
                task.order = index
                task.save()
            return JsonResponse({'status' : 'success'})
        except Exception as e:
            return JsonResponse({'status' : 'error', 'message' : str(e)}, status=500)
    return JsonResponse({'status' : 'error', 'message' : 'Invalid request method'}, status=400)
       