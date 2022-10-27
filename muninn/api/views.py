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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
            req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
            req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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
            data = INSERT_MODEL_HERE.objects.all()
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
        req_object = .objects.get(pk=pk)
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

