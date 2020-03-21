from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Task
from django.template import loader

# Create your views here.
def index(request):
    task_list = Task.objects.all()
    # 1. output = ', '.join([q.task_name for q in task_list])
    # 2. template = loader.get_template('todo_app/index.html')
    context = {
        'task_list': task_list
    }
    # 2. return HttpResponse(template.render(context, request))
    return render(request, 'todo_app/index.html', context)

def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404('Task does not exist.')
        # TODO: Design template for error page
    context = {
        'task': task,
    }
    return render(request, 'todo_app/detail.html', context)