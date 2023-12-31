from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .serializer import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(http_method_names=['POST'])
def view_register(request):
    data={}
    if request.method=='POST':
        user_ser=UserSerializer(data=request.data)
        if user_ser.is_valid():
            u= user_ser.save()
            data['register']='User Register SuccessFully!!'
            data['username']=u.username
            t=Token.objects.get(user=u)
            data['token']=t.key
        else:
            data['error']=user_ser.errors
        return Response(data=data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def view_secure(request):
    return Response(data="This is my Secure page can access only when Token is provided")        








        

    