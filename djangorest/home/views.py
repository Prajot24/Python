from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Todo
from home.serializer import TodoSerializers

# Create your views here.

@api_view(['POST','GET'])
def home(request):
    if request.method == 'POST':
        return Response(
            {
                'Type':"This is Post method"
            }
        )
    return Response(
        {
            'status':200,
            'name':"Prajot",
            'city':"Kolhapur"
        }
    )

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        print(data)
        serial = TodoSerializers(data=data)
        if serial.is_valid():
            serial.save()
            return Response(
            {
            'status':200,
            'message':"Success todo created",
            'data': serial.data
            })

        return Response(
        {
            'status':404,
            'message':serial.errors
        }
    )
    except Exception as e:
        print(e)
    return Response(
        {
            'status':404,
            'message':"Something went wrong"
        }
    )


@api_view(['GET'])
def get_todo(request):
    todo_obj = Todo.objects.all()
    serializer = TodoSerializers(todo_obj,many = True)

    return Response(
        {
            "message":"Success",
            "data":serializer.data
        }
    )

