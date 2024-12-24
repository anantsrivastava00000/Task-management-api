from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from django.utils import timezone
from datetime import datetime, date
# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_list_and_retrieve_one_task(request):
    id = request.query_params.get('id')
    due_date = request.query_params.get('due_date')
    completed = request.query_params.get('completed')
    limits = request.query_params.get('limits', 1)
    print(limits)
    page = request.query_params.get('page')

    if id:
        # if Task.objects.filter(user=request.user, id=id).exists():
            # task=Task.objects.get(user=request.user, id=id)
            task=get_object_or_404(Task, user=request.user, id=id)
            serializer = TaskSerializer(task).data
            return Response({'data': serializer,
                             'response_code':200})
    if due_date:
        print(due_date,'>>>>>>>>>>>')
        # datetime.strptime(due_date, '%Y-%m-%d')
        tasks = Task.objects.filter(user=request.user, due_date=due_date)


    elif completed:
        tasks = Task.objects.filter(user=request.user,completed=completed)
    
    else:
        tasks = Task.objects.filter(user=request.user)
        pagination = Paginator(tasks, limits)
    
        data = pagination.get_page(page)
    
        serializer = TaskSerializer(data, many=True).data
    
        return Response({'data':serializer,
                     'count':len(tasks),
                     'current_page':data.number,
                     'total_page':pagination.num_pages,
                     'response_code':200})


    serializer = TaskSerializer(tasks, many=True).data
    return Response({'data':serializer,
                     'response_code':200})

# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def tasklist_with_pagination(request):

#     limits = request.query_params.get('limits', 1)
#     print(limits)
#     page = request.query_params.get('page')

#     tasks = Task.objects.filter(user=request.user)
    
#     pagination = Paginator(tasks, limits)
    
#     data = pagination.get_page(page)
    
#     serializer = TaskSerializer(data, many=True).data
    
#     return Response({'data':serializer,
#                      'count':len(tasks),
#                      'current_page':data.number,
#                      'total_page':pagination.num_pages,
#                      'response_code':200})

 
     

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
def task_create(request):

    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()   
        return Response(serializer.data, status=201) 
    return Response(serializer.errors, status=400)   




@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
def Update_task(request):
    id = request.data.get('id')
    # print(timezone.now().today()) #output for this 2024-12-23 23:05:06.406747
    
    if not Task.objects.filter(id=id).exists():
        return Response({'msg':'Task not exists'})
    
    task=Task.objects.get(id=id)
    # print(type(date.today()))
    # print(type(task.due_date))
    # print(timezone.now())
    # if task.due_date and task.due_date < date.today(): #condition wrong hai bhaiya > ye sahi hai
    #     print('o nooooooooooooooooo nahi')
    
 

    if task.due_date and task.due_date > date.today():
        serializer=TaskUpdateSerializer(task, data=request.data, partial = True)
        if serializer.is_valid():
            task=serializer.save()
            task.save()
            return Response({'msg': 'data updated',
                        'data': serializer.data,
                        'reponse_code': 200})
        return Response({'msg' : serializer.errors,
                         'reponse_code': 400})
        # pass
        
    else:   
        return Response({'msg':'due date over'}) 
         
    # serializer=TaskUpdateSerializer(task, data=request.data, partial = True)
    # if serializer.is_valid():
    #     return Response({'msg': 'data updated',
    #                     'data': serializer.data,
    #                     'reponse_code': 200})
    # return Response({'msg' : serializer.errors,
    #                  'reponse_code': 400})
     



@api_view(['DELETE'])   
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])  
def delete_task(request):
    id=request.data.get('id')
    if not Task.objects.filter(id=id).exists():
         return Response({'msg':'Task not exists',
                          'response_code': 404})
    task=Task.objects.get(id=id)
    task.delete()
    return Response({'msg': 'data deleted'},status=200)




# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def filter_task_and_due_date_range(request):
 
#     tasks=Task.objects.filter(user=request.user)
     
#     completed = request.query_params.get('completed')
#     # print(type(bool(completed)))
#     completed = bool(completed)
#     print(completed, '>>>>')
    
#     if  completed:
#         tasks=tasks.filter(completed=completed)
#         serializer=TaskSerializer(tasks, many=True).data
#         return Response({'data':serializer})
    
#     start_date=request.query_params.get('start_date')
#     end_date=request.query_params.get('end_date')
    
#     print(start_date, end_date)
#     if not tasks.filter(due_date__range=(start_date, end_date), completed=completed).exists():
#         return Response('tasks not exists')
    
#     tasks.filter(due_date__range=(start_date, end_date), completed=False)
#     serializer=TaskSerializer(tasks, many=True).data
#     return Response({'data':serializer})









# def create_task(request): 
    # serializer = TaskSerializer(data=request.data)
    # print(request.data)
    
    # if serializer.is_valid():
    #     serializer.save(user=request.user)
    #     return Response(serializer.data, status=201)
    
    # return Response(serializer.errors, status=400)







# def validate_due_date(self, value):
#     # Ensure the due_date is not in the past
#     if value and value < date.today():
#         raise serializers.ValidationError("Due date cannot be in the past.")
#     return value

# from datetime import date

# from django.utils import timezone


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def saw(request):
#     return Response({'msg':'kkk',
#                      'date':date.today(),
#                      'date2':timezone.now().date()})

# @api_view(['GET'])
# def task_detail(request, task_id):
#     try:
#         task = Task.objects.get(id=task_id, user=request.user)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#     except Task.DoesNotExist:
#         return Response({"error": "Task not found"}, status=)

