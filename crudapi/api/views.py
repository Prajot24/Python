
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view
def home(request):
    return Response({
        'code': 200,
        'name':"Prajot"       
    })