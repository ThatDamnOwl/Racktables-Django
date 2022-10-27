from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET', 'POST'])
def UserAccount_List(request):
    match (request.method):
        case "GET":
            data = UserAccount.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view('GET',['PUT', 'DELETE'])
def UserAccount_Detail(request,pk):
    try:
        req_object = UserAccount.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def UserConfig_List(request):
    match(request.method)
        case "GET":
            data = UserConfig.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def UserConfig_Detail(request,pk):
    try:
        req_object = UserConfig.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Molecule_List(request):
    match(request.method)
        case "GET":
            data = Molecule.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Molecule_Detail(request,pk):
    try:
        req_object = Molecule.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Location_List(request):
    match(request.method)
        case "GET":
            data = Location.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Location_Detail(request,pk):
    try:
        req_object = Location.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Row_List(request):
    match(request.method)
        case "GET":
            data = Row.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Row_Detail(request,pk):
    try:
        req_object = Row.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Rack_List(request):
    match(request.method)
        case "GET":
            data = Rack.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Rack_Detail(request,pk):
    try:
        req_object = Rack.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Atom_List(request):
    match(request.method)
        case "GET":
            data = Atom.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Atom_Detail(request,pk):
    try:
        req_object = Atom.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Attribute_List(request):
    match(request.method)
        case "GET":
            data = Attribute.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Attribute_Detail(request,pk):
    try:
        req_object = Attribute.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Chapter_List(request):
    match(request.method)
        case "GET":
            data = Chapter.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Chapter_Detail(request,pk):
    try:
        req_object = Chapter.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Dictionary_List(request):
    match(request.method)
        case "GET":
            data = Dictionary.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Dictionary_Detail(request,pk):
    try:
        req_object = Dictionary.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def ObjectType_List(request):
    match(request.method)
        case "GET":
            data = ObjectType.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def ObjectType_Detail(request,pk):
    try:
        req_object = ObjectType.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Object_List(request):
    match(request.method)
        case "GET":
            data = Object.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Object_Detail(request,pk):
    try:
        req_object = Object.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeMap_List(request):
    match(request.method)
        case "GET":
            data = AttributeMap.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def AttributeMap_Detail(request,pk):
    try:
        req_object = AttributeMap.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeValueString_List(request):

    match(request.method)
        case "GET":
            data = AttributeValueString.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view('GET','PUT','DELETE')
def AttributeValueStrin_Detail(request,pk):
        try:
            req_object = AttributeValueStrin.objects.get(pk=pk)
        except req_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        match(request.method)
            case "GET":
                serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
            case "POST":
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            case "PATCH":
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            case "DELETE":
                req_object.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            case "PUT":
                    serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            case _:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    
@api_view('GET','POST')
def AttributeValueInt_List(request):
    match(request.method)
        case "GET":
            data = AttributeValueInt.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def AttributeValueInt_Detail(request,pk):
    try:
        req_object = AttributeValueInt.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeValueFloat_List(request):
    match(request.method)
        case "GET":
            data = AttributeValueFloat.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def AttributeValueFloat_Detail(request,pk):
    try:
        req_object = AttributeValueFloat.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeValueDict_List(request):
    match(request.method)
        case "GET":
            data = AttributeValueDict.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def AttributeValueDict_Detail(request,pk):
    try:
        req_object = AttributeValueDict.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeValueDate_List(request):
    match(request.method)
        case "GET":
            data = AttributeValueDate.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def AttributeValueDate_Detail(request,pk):
    try:
        req_object = AttributeValueDate.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4Address_List(request):
    match(request.method)
        case "GET":
            data = IPv4Address.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv4Address_Detail(request,pk):
    try:
        req_object = IPv4Address.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4VS_List(request):
    match(request.method)
        case "GET":
            data = IPv4VS.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv4VS_Detail(request,pk):
    try:
        req_object = IPv4VS.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4Allocation_List(request):
    match(request.method)
        case "GET":
            data = IPv4Allocation.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv4Allocation_Detail(request,pk):
    try:
        req_object = IPv4Allocation.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4RSPool_List(request):
    match(request.method)
        case "GET":
            data = IPv4RSPool.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv4RSPool_Detail(request,pk):
    try:
        req_object = IPv4RSPool.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4RS_List(request):
    match(request.method)
        case "GET":
            data = IPv4RS.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv4RS_Detail(request,pk):
    try:
        req_object = IPv4RS.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4LB_List(request):
    match(request.method)
        case "GET":
            data = IPv4LB.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv4LB_Detail(request,pk):
    try:
        req_object = IPv4LB.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4Log_List(request):
    match(request.method)
        case "GET":
            data = IPv4Log.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv4Log_Detail(request,pk):
    try:
        req_object = IPv4Log.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4NAT_List(request):
    match(request.method)
        case "GET":
            data = IPv4NAT.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv4NAT_Detail(request,pk):
    try:
        req_object = IPv4NAT.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4Network_List(request):
    match(request.method)
        case "GET":
            data = IPv4Network.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv4Network_Detail(request,pk):
    try:
        req_object = IPv4Network.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv6Address_List(request):
    match(request.method)
        case "GET":
            data = IPv6Address.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv6Address_Detail(request,pk):
    try:
        req_object = IPv6Address.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv6Allocation_List(request):
    match(request.method)
        case "GET":
            data = IPv6Allocation.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv6Allocation_Detail(request,pk):
    try:
        req_object = IPv6Allocation.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv6Log_List(request):
    match(request.method)
        case "GET":
            data = IPv6Log.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv6Log_Detail(request,pk):
    try:
        req_object = IPv6Log.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv6Network_List(request):
    match(request.method)
        case "GET":
            data = IPv6Network.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def IPv6Network_Detail(request,pk):
    try:
        req_object = IPv6Network.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Config_List(request):
    match(request.method)
        case "GET":
            data = Config.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Config_Detail(request,pk):
    try:
        req_object = Config.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def File_List(request):
    match(request.method)
        case "GET":
            data = File.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def File_Detail(request,pk):
    try:
        req_object = File.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkIPv4Network_List(request):
    match(request.method)
        case "GET":
            data = FileLinkIPv4Network.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def FileLinkIPv4Network_Detail(request,pk):
    try:
        req_object = FileLinkIPv4Network.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkIPv4RSPool_List(request):
    match(request.method)
        case "GET":
            data = FileLinkIPv4RSPool.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def FileLinkIPv4RSPool_Detail(request,pk):
    try:
        req_object = FileLinkIPv4RSPool.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkIPv4VS_List(request):
    match(request.method)
        case "GET":
            data = FileLinkIPv4VS.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def FileLinkIPv4VS_Detail(request,pk):
    try:
        req_object = FileLinkIPv4VS.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkIPv6Network_List(request):
    match(request.method)
        case "GET":
            data = FileLinkIPv6Network.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def FileLinkIPv6Network_Detail(request,pk):
    try:
        req_object = FileLinkIPv6Network.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkLocation_List(request):
    match(request.method)
        case "GET":
            data = FileLinkLocation.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def FileLinkLocation_Detail(request,pk):
    try:
        req_object = FileLinkLocation.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkObject_List(request):
    match(request.method)
        case "GET":
            data = FileLinkObject.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def FileLinkObject_Detail(request,pk):
    try:
        req_object = FileLinkObject.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkRack_List(request):
    match(request.method)
        case "GET":
            data = FileLinkRack.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def FileLinkRack_Detail(request,pk):
    try:
        req_object = FileLinkRack.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkRow_List(request):
    match(request.method)
        case "GET":
            data = FileLinkRow.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def FileLinkRow_Detail(request,pk):
    try:
        req_object = FileLinkRow.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkUser_List(request):
    match(request.method)
        case "GET":
            data = FileLinkUser.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def FileLinkUser_Detail(request,pk):
    try:
        req_object = FileLinkUser.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def MountOperation_List(request):
    match(request.method)
        case "GET":
            data = MountOperation.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def MountOperation_Detail(request,pk):
    try:
        req_object = MountOperation.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def ObjectHistory_List(request):
    match(request.method)
        case "GET":
            data = ObjectHistory.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def ObjectHistory_Detail(request,pk):
    try:
        req_object = ObjectHistory.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def ObjectLog_List(request):
    match(request.method)
        case "GET":
            data = ObjectLog.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def ObjectLog_Detail(request,pk):
    try:
        req_object = ObjectLog.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableConnector_List(request):
    match(request.method)
        case "GET":
            data = PatchCableConnector.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PatchCableConnector_Detail(request,pk):
    try:
        req_object = PatchCableConnector.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableType_List(request):
    match(request.method)
        case "GET":
            data = PatchCableType.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PatchCableType_Detail(request,pk):
    try:
        req_object = PatchCableType.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableConnectorCompat_List(request):

    match(request.method)
        case "GET":
            data = PatchCableConnectorCompat.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view('GET','PUT','DELETE')
def PatchCableConnector_DetailCompat(request,pk):
        try:
            req_object = PatchCableConnector.objects.get(pk=pk)
        except req_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        match(request.method)
            case "GET":
                serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
            case "POST":
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            case "PATCH":
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            case "DELETE":
                req_object.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            case "PUT":
                    serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            case _:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    
@api_view('GET','POST')
def PatchCableHeap_List(request):
    match(request.method)
        case "GET":
            data = PatchCableHeap.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PatchCableHeap_Detail(request,pk):
    try:
        req_object = PatchCableHeap.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableHeapLog_List(request):
    match(request.method)
        case "GET":
            data = PatchCableHeapLog.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PatchCableHeapLog_Detail(request,pk):
    try:
        req_object = PatchCableHeapLog.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Plugin_List(request):
    match(request.method)
        case "GET":
            data = Plugin.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Plugin_Detail(request,pk):
    try:
        req_object = Plugin.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortInnerInterface_List(request):
    match(request.method)
        case "GET":
            data = PortInnerInterface.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PortInnerInterface_Detail(request,pk):
    try:
        req_object = PortInnerInterface.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortOuterInterface_List(request):
    match(request.method)
        case "GET":
            data = PortOuterInterface.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PortOuterInterface_Detail(request,pk):
    try:
        req_object = PortOuterInterface.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableOIFCompat_List(request):
    match(request.method)
        case "GET":
            data = PatchCableOIFCompat.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PatchCableOIFCompat_Detail(request,pk):
    try:
        req_object = PatchCableOIFCompat.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Port_List(request):
    match(request.method)
        case "GET":
            data = Port.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Port_Detail(request,pk):
    try:
        req_object = Port.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANDomain_List(request):
    match(request.method)
        case "GET":
            data = VLANDomain.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VLANDomain_Detail(request,pk):
    try:
        req_object = VLANDomain.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANDescription_List(request):
    match(request.method)
        case "GET":
            data = VLANDescription.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VLANDescription_Detail(request,pk):
    try:
        req_object = VLANDescription.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANIPv4_List(request):
    match(request.method)
        case "GET":
            data = VLANIPv4.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VLANIPv4_Detail(request,pk):
    try:
        req_object = VLANIPv4.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANIPv6_List(request):
    match(request.method)
        case "GET":
            data = VLANIPv6.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VLANIPv6_Detail(request,pk):
    try:
        req_object = VLANIPv6.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortAllowedVLAN_List(request):
    match(request.method)
        case "GET":
            data = PortAllowedVLAN.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PortAllowedVLAN_Detail(request,pk):
    try:
        req_object = PortAllowedVLAN.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortCompat_List(request):
    match(request.method)
        case "GET":
            data = PortCompat.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PortCompat_Detail(request,pk):
    try:
        req_object = PortCompat.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortInterfaceCompat_List(request):
    match(request.method)
        case "GET":
            data = PortInterfaceCompat.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PortInterfaceCompat_Detail(request,pk):
    try:
        req_object = PortInterfaceCompat.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortLog_List(request):
    match(request.method)
        case "GET":
            data = PortLog.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PortLog_Detail(request,pk):
    try:
        req_object = PortLog.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortVLANMode_List(request):
    match(request.method)
        case "GET":
            data = PortVLANMode.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def PortVLANMode_Detail(request,pk):
    try:
        req_object = PortVLANMode.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def RackObject_List(request):
    match(request.method)
        case "GET":
            data = RackObject.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def RackObject_Detail(request,pk):
    try:
        req_object = RackObject.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def RackSpace_List(request):
    match(request.method)
        case "GET":
            data = RackSpace.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def RackSpace_Detail(request,pk):
    try:
        req_object = RackSpace.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def RackThumbnail_List(request):
    match(request.method)
        case "GET":
            data = RackThumbnail.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def RackThumbnail_Detail(request,pk):
    try:
        req_object = RackThumbnail.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Script_List(request):
    match(request.method)
        case "GET":
            data = Script.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Script_Detail(request,pk):
    try:
        req_object = Script.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Tag_List(request):
    match(request.method)
        case "GET":
            data = Tag.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def Tag_Detail(request,pk):
    try:
        req_object = Tag.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagFile_List(request):
    match(request.method)
        case "GET":
            data = TagFile.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def TagFile_Detail(request,pk):
    try:
        req_object = TagFile.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagIPv4Network_List(request):
    match(request.method)
        case "GET":
            data = TagIPv4Network.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def TagIPv4Network_Detail(request,pk):
    try:
        req_object = TagIPv4Network.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagIPv4RSPool_List(request):
    match(request.method)
        case "GET":
            data = TagIPv4RSPool.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def TagIPv4RSPool_Detail(request,pk):
    try:
        req_object = TagIPv4RSPool.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagIPv4VS_List(request):
    match(request.method)
        case "GET":
            data = TagIPv4VS.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def TagIPv4VS_Detail(request,pk):
    try:
        req_object = TagIPv4VS.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagIPv6Network_List(request):
    match(request.method)
        case "GET":
            data = TagIPv6Network.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def TagIPv6Network_Detail(request,pk):
    try:
        req_object = TagIPv6Network.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagLocation_List(request):
    match(request.method)
        case "GET":
            data = TagLocation.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def TagLocation_Detail(request,pk):
    try:
        req_object = TagLocation.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagObject_List(request):
    match(request.method)
        case "GET":
            data = TagObject.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def TagObject_Detail(request,pk):
    try:
        req_object = TagObject.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagRack_List(request):
    match(request.method)
        case "GET":
            data = TagRack.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def TagRack_Detail(request,pk):
    try:
        req_object = TagRack.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANSTRule_List(request):
    match(request.method)
        case "GET":
            data = VLANSTRule.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VLANSTRule_Detail(request,pk):
    try:
        req_object = VLANSTRule.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANSwitchTemplate_List(request):
    match(request.method)
        case "GET":
            data = VLANSwitchTemplate.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VLANSwitchTemplate_Detail(request,pk):
    try:
        req_object = VLANSwitchTemplate.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANSwitch_List(request):
    match(request.method)
        case "GET":
            data = VLANSwitch.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VLANSwitch_Detail(request,pk):
    try:
        req_object = VLANSwitch.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANValidID_List(request):
    match(request.method)
        case "GET":
            data = VLANValidID.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VLANValidID_Detail(request,pk):
    try:
        req_object = VLANValidID.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VS_List(request):
    match(request.method)
        case "GET":
            data = VS.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VS_Detail(request,pk):
    try:
        req_object = VS.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VSEnabledIPs_List(request):
    match(request.method)
        case "GET":
            data = VSEnabledIPs.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VSEnabledIPs_Detail(request,pk):
    try:
        req_object = VSEnabledIPs.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VSEnabledPorts_List(request):
    match(request.method)
        case "GET":
            data = VSEnabledPorts.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VSEnabledPorts_Detail(request,pk):
    try:
        req_object = VSEnabledPorts.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VSIPs_List(request):
    match(request.method)
        case "GET":
            data = VSIPs.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VSIPs_Detail(request,pk):
    try:
        req_object = VSIPs.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VSPorts_List(request):
    match(request.method)
        case "GET":
            data = VSPorts.objects.all()
            serializer = INSERT_SERIALIZER_HERE(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = INSERT_SERIALIZER_HERE(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return.Response(status=status.HTTP_201_CREATED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PUT":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)            

@api_view('GET','PUT','DELETE')
def VSPorts_Detail(request,pk):
    try:
        req_object = VSPorts.objects.get(pk=pk)
    except req_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match(request.method)
        case "GET":
            serializer = INSERT_SERIALIZER_HERE(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = INSERT_SERIALIZER_HERE(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

