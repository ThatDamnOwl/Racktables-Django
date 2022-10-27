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
            serializer = UserAccountSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = UserAccountSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = UserAccountSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = UserAccountSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def UserConfig_List(request):
    match (request.method):
        case "GET":
            data = UserConfig.objects.all()
            serializer = UserConfigSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = UserConfigSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = UserConfigSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = UserConfigSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Molecule_List(request):
    match (request.method):
        case "GET":
            data = Molecule.objects.all()
            serializer = MoleculeSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = MoleculeSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = MoleculeSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = MoleculeSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Location_List(request):
    match (request.method):
        case "GET":
            data = Location.objects.all()
            serializer = LocationSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = LocationSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = LocationSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = LocationSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Row_List(request):
    match (request.method):
        case "GET":
            data = Row.objects.all()
            serializer = RowSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = RowSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = RowSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = RowSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Rack_List(request):
    match (request.method):
        case "GET":
            data = Rack.objects.all()
            serializer = RackSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = RackSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = RackSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = RackSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Atom_List(request):
    match (request.method):
        case "GET":
            data = Atom.objects.all()
            serializer = AtomSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = AtomSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = AtomSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = AtomSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Attribute_List(request):
    match (request.method):
        case "GET":
            data = Attribute.objects.all()
            serializer = AttributeSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = AttributeSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = AttributeSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = AttributeSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Chapter_List(request):
    match (request.method):
        case "GET":
            data = Chapter.objects.all()
            serializer = ChapterSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = ChapterSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = ChapterSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = ChapterSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Dictionary_List(request):
    match (request.method):
        case "GET":
            data = Dictionary.objects.all()
            serializer = DictionarySerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = DictionarySerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = DictionarySerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = DictionarySerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def ObjectType_List(request):
    match (request.method):
        case "GET":
            data = ObjectType.objects.all()
            serializer = ObjectTypeSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = ObjectTypeSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = ObjectTypeSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = ObjectTypeSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Object_List(request):
    match (request.method):
        case "GET":
            data = Object.objects.all()
            serializer = ObjectSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = ObjectSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = ObjectSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = ObjectSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeMap_List(request):
    match (request.method):
        case "GET":
            data = AttributeMap.objects.all()
            serializer = AttributeMapSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = AttributeMapSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = AttributeMapSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = AttributeMapSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeValueString_List(request):

    match (request.method):
        case "GET":
            data = AttributeValueString.objects.all()
            serializer = AttributeValueStringSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = AttributeValueStringSerializer(data=request.data)
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


        match (request.method):
            case "GET":
                serializer = AttributeValueStrinSerializer(req_object, context={'request': request}, many=False)
            case "POST":
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            case "PATCH":
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            case "DELETE":
                req_object.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            case "PUT":
                    serializer = AttributeValueStrinSerializer(req_object, data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            case _:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    
@api_view('GET','POST')
def AttributeValueInt_List(request):
    match (request.method):
        case "GET":
            data = AttributeValueInt.objects.all()
            serializer = AttributeValueIntSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = AttributeValueIntSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = AttributeValueIntSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = AttributeValueIntSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeValueFloat_List(request):
    match (request.method):
        case "GET":
            data = AttributeValueFloat.objects.all()
            serializer = AttributeValueFloatSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = AttributeValueFloatSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = AttributeValueFloatSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = AttributeValueFloatSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeValueDict_List(request):
    match (request.method):
        case "GET":
            data = AttributeValueDict.objects.all()
            serializer = AttributeValueDictSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = AttributeValueDictSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = AttributeValueDictSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = AttributeValueDictSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def AttributeValueDate_List(request):
    match (request.method):
        case "GET":
            data = AttributeValueDate.objects.all()
            serializer = AttributeValueDateSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = AttributeValueDateSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = AttributeValueDateSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = AttributeValueDateSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4Address_List(request):
    match (request.method):
        case "GET":
            data = IPv4Address.objects.all()
            serializer = IPv4AddressSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv4AddressSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv4AddressSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv4AddressSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4VS_List(request):
    match (request.method):
        case "GET":
            data = IPv4VS.objects.all()
            serializer = IPv4VSSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv4VSSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv4VSSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv4VSSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4Allocation_List(request):
    match (request.method):
        case "GET":
            data = IPv4Allocation.objects.all()
            serializer = IPv4AllocationSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv4AllocationSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv4AllocationSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv4AllocationSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4RSPool_List(request):
    match (request.method):
        case "GET":
            data = IPv4RSPool.objects.all()
            serializer = IPv4RSPoolSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv4RSPoolSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv4RSPoolSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv4RSPoolSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4RS_List(request):
    match (request.method):
        case "GET":
            data = IPv4RS.objects.all()
            serializer = IPv4RSSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv4RSSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv4RSSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv4RSSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4LB_List(request):
    match (request.method):
        case "GET":
            data = IPv4LB.objects.all()
            serializer = IPv4LBSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv4LBSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv4LBSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv4LBSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4Log_List(request):
    match (request.method):
        case "GET":
            data = IPv4Log.objects.all()
            serializer = IPv4LogSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv4LogSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv4LogSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv4LogSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4NAT_List(request):
    match (request.method):
        case "GET":
            data = IPv4NAT.objects.all()
            serializer = IPv4NATSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv4NATSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv4NATSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv4NATSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv4Network_List(request):
    match (request.method):
        case "GET":
            data = IPv4Network.objects.all()
            serializer = IPv4NetworkSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv4NetworkSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv4NetworkSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv4NetworkSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv6Address_List(request):
    match (request.method):
        case "GET":
            data = IPv6Address.objects.all()
            serializer = IPv6AddressSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv6AddressSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv6AddressSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv6AddressSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv6Allocation_List(request):
    match (request.method):
        case "GET":
            data = IPv6Allocation.objects.all()
            serializer = IPv6AllocationSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv6AllocationSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv6AllocationSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv6AllocationSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv6Log_List(request):
    match (request.method):
        case "GET":
            data = IPv6Log.objects.all()
            serializer = IPv6LogSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv6LogSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv6LogSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv6LogSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def IPv6Network_List(request):
    match (request.method):
        case "GET":
            data = IPv6Network.objects.all()
            serializer = IPv6NetworkSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = IPv6NetworkSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = IPv6NetworkSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = IPv6NetworkSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Config_List(request):
    match (request.method):
        case "GET":
            data = Config.objects.all()
            serializer = ConfigSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = ConfigSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = ConfigSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = ConfigSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def File_List(request):
    match (request.method):
        case "GET":
            data = File.objects.all()
            serializer = FileSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkIPv4Network_List(request):
    match (request.method):
        case "GET":
            data = FileLinkIPv4Network.objects.all()
            serializer = FileLinkIPv4NetworkSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileLinkIPv4NetworkSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileLinkIPv4NetworkSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileLinkIPv4NetworkSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkIPv4RSPool_List(request):
    match (request.method):
        case "GET":
            data = FileLinkIPv4RSPool.objects.all()
            serializer = FileLinkIPv4RSPoolSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileLinkIPv4RSPoolSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileLinkIPv4RSPoolSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileLinkIPv4RSPoolSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkIPv4VS_List(request):
    match (request.method):
        case "GET":
            data = FileLinkIPv4VS.objects.all()
            serializer = FileLinkIPv4VSSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileLinkIPv4VSSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileLinkIPv4VSSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileLinkIPv4VSSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkIPv6Network_List(request):
    match (request.method):
        case "GET":
            data = FileLinkIPv6Network.objects.all()
            serializer = FileLinkIPv6NetworkSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileLinkIPv6NetworkSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileLinkIPv6NetworkSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileLinkIPv6NetworkSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkLocation_List(request):
    match (request.method):
        case "GET":
            data = FileLinkLocation.objects.all()
            serializer = FileLinkLocationSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileLinkLocationSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileLinkLocationSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileLinkLocationSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkObject_List(request):
    match (request.method):
        case "GET":
            data = FileLinkObject.objects.all()
            serializer = FileLinkObjectSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileLinkObjectSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileLinkObjectSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileLinkObjectSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkRack_List(request):
    match (request.method):
        case "GET":
            data = FileLinkRack.objects.all()
            serializer = FileLinkRackSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileLinkRackSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileLinkRackSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileLinkRackSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkRow_List(request):
    match (request.method):
        case "GET":
            data = FileLinkRow.objects.all()
            serializer = FileLinkRowSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileLinkRowSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileLinkRowSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileLinkRowSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def FileLinkUser_List(request):
    match (request.method):
        case "GET":
            data = FileLinkUser.objects.all()
            serializer = FileLinkUserSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = FileLinkUserSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = FileLinkUserSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = FileLinkUserSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def MountOperation_List(request):
    match (request.method):
        case "GET":
            data = MountOperation.objects.all()
            serializer = MountOperationSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = MountOperationSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = MountOperationSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = MountOperationSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def ObjectHistory_List(request):
    match (request.method):
        case "GET":
            data = ObjectHistory.objects.all()
            serializer = ObjectHistorySerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = ObjectHistorySerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = ObjectHistorySerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = ObjectHistorySerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def ObjectLog_List(request):
    match (request.method):
        case "GET":
            data = ObjectLog.objects.all()
            serializer = ObjectLogSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = ObjectLogSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = ObjectLogSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = ObjectLogSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableConnector_List(request):
    match (request.method):
        case "GET":
            data = PatchCableConnector.objects.all()
            serializer = PatchCableConnectorSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PatchCableConnectorSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PatchCableConnectorSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PatchCableConnectorSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableType_List(request):
    match (request.method):
        case "GET":
            data = PatchCableType.objects.all()
            serializer = PatchCableTypeSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PatchCableTypeSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PatchCableTypeSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PatchCableTypeSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableConnectorCompat_List(request):

    match (request.method):
        case "GET":
            data = PatchCableConnectorCompat.objects.all()
            serializer = PatchCableConnectorCompatSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PatchCableConnectorCompatSerializer(data=request.data)
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


        match (request.method):
            case "GET":
                serializer = PatchCableConnectorSerializer(req_object, context={'request': request}, many=False)
            case "POST":
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            case "PATCH":
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            case "DELETE":
                req_object.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            case "PUT":
                    serializer = PatchCableConnectorSerializer(req_object, data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            case _:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    
@api_view('GET','POST')
def PatchCableHeap_List(request):
    match (request.method):
        case "GET":
            data = PatchCableHeap.objects.all()
            serializer = PatchCableHeapSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PatchCableHeapSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PatchCableHeapSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PatchCableHeapSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableHeapLog_List(request):
    match (request.method):
        case "GET":
            data = PatchCableHeapLog.objects.all()
            serializer = PatchCableHeapLogSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PatchCableHeapLogSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PatchCableHeapLogSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PatchCableHeapLogSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Plugin_List(request):
    match (request.method):
        case "GET":
            data = Plugin.objects.all()
            serializer = PluginSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PluginSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PluginSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PluginSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortInnerInterface_List(request):
    match (request.method):
        case "GET":
            data = PortInnerInterface.objects.all()
            serializer = PortInnerInterfaceSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PortInnerInterfaceSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PortInnerInterfaceSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PortInnerInterfaceSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortOuterInterface_List(request):
    match (request.method):
        case "GET":
            data = PortOuterInterface.objects.all()
            serializer = PortOuterInterfaceSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PortOuterInterfaceSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PortOuterInterfaceSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PortOuterInterfaceSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PatchCableOIFCompat_List(request):
    match (request.method):
        case "GET":
            data = PatchCableOIFCompat.objects.all()
            serializer = PatchCableOIFCompatSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PatchCableOIFCompatSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PatchCableOIFCompatSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PatchCableOIFCompatSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Port_List(request):
    match (request.method):
        case "GET":
            data = Port.objects.all()
            serializer = PortSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PortSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PortSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PortSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANDomain_List(request):
    match (request.method):
        case "GET":
            data = VLANDomain.objects.all()
            serializer = VLANDomainSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VLANDomainSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VLANDomainSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VLANDomainSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANDescription_List(request):
    match (request.method):
        case "GET":
            data = VLANDescription.objects.all()
            serializer = VLANDescriptionSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VLANDescriptionSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VLANDescriptionSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VLANDescriptionSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANIPv4_List(request):
    match (request.method):
        case "GET":
            data = VLANIPv4.objects.all()
            serializer = VLANIPv4Serializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VLANIPv4Serializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VLANIPv4Serializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VLANIPv4Serializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANIPv6_List(request):
    match (request.method):
        case "GET":
            data = VLANIPv6.objects.all()
            serializer = VLANIPv6Serializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VLANIPv6Serializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VLANIPv6Serializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VLANIPv6Serializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortAllowedVLAN_List(request):
    match (request.method):
        case "GET":
            data = PortAllowedVLAN.objects.all()
            serializer = PortAllowedVLANSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PortAllowedVLANSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PortAllowedVLANSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PortAllowedVLANSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortCompat_List(request):
    match (request.method):
        case "GET":
            data = PortCompat.objects.all()
            serializer = PortCompatSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PortCompatSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PortCompatSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PortCompatSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortInterfaceCompat_List(request):
    match (request.method):
        case "GET":
            data = PortInterfaceCompat.objects.all()
            serializer = PortInterfaceCompatSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PortInterfaceCompatSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PortInterfaceCompatSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PortInterfaceCompatSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortLog_List(request):
    match (request.method):
        case "GET":
            data = PortLog.objects.all()
            serializer = PortLogSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PortLogSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PortLogSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PortLogSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def PortVLANMode_List(request):
    match (request.method):
        case "GET":
            data = PortVLANMode.objects.all()
            serializer = PortVLANModeSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = PortVLANModeSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = PortVLANModeSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = PortVLANModeSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def RackObject_List(request):
    match (request.method):
        case "GET":
            data = RackObject.objects.all()
            serializer = RackObjectSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = RackObjectSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = RackObjectSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = RackObjectSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def RackSpace_List(request):
    match (request.method):
        case "GET":
            data = RackSpace.objects.all()
            serializer = RackSpaceSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = RackSpaceSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = RackSpaceSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = RackSpaceSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def RackThumbnail_List(request):
    match (request.method):
        case "GET":
            data = RackThumbnail.objects.all()
            serializer = RackThumbnailSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = RackThumbnailSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = RackThumbnailSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = RackThumbnailSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Script_List(request):
    match (request.method):
        case "GET":
            data = Script.objects.all()
            serializer = ScriptSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = ScriptSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = ScriptSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = ScriptSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def Tag_List(request):
    match (request.method):
        case "GET":
            data = Tag.objects.all()
            serializer = TagSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = TagSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = TagSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = TagSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagFile_List(request):
    match (request.method):
        case "GET":
            data = TagFile.objects.all()
            serializer = TagFileSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = TagFileSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = TagFileSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = TagFileSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagIPv4Network_List(request):
    match (request.method):
        case "GET":
            data = TagIPv4Network.objects.all()
            serializer = TagIPv4NetworkSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = TagIPv4NetworkSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = TagIPv4NetworkSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = TagIPv4NetworkSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagIPv4RSPool_List(request):
    match (request.method):
        case "GET":
            data = TagIPv4RSPool.objects.all()
            serializer = TagIPv4RSPoolSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = TagIPv4RSPoolSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = TagIPv4RSPoolSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = TagIPv4RSPoolSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagIPv4VS_List(request):
    match (request.method):
        case "GET":
            data = TagIPv4VS.objects.all()
            serializer = TagIPv4VSSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = TagIPv4VSSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = TagIPv4VSSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = TagIPv4VSSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagIPv6Network_List(request):
    match (request.method):
        case "GET":
            data = TagIPv6Network.objects.all()
            serializer = TagIPv6NetworkSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = TagIPv6NetworkSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = TagIPv6NetworkSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = TagIPv6NetworkSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagLocation_List(request):
    match (request.method):
        case "GET":
            data = TagLocation.objects.all()
            serializer = TagLocationSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = TagLocationSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = TagLocationSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = TagLocationSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagObject_List(request):
    match (request.method):
        case "GET":
            data = TagObject.objects.all()
            serializer = TagObjectSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = TagObjectSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = TagObjectSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = TagObjectSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def TagRack_List(request):
    match (request.method):
        case "GET":
            data = TagRack.objects.all()
            serializer = TagRackSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = TagRackSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = TagRackSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = TagRackSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANSTRule_List(request):
    match (request.method):
        case "GET":
            data = VLANSTRule.objects.all()
            serializer = VLANSTRuleSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VLANSTRuleSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VLANSTRuleSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VLANSTRuleSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANSwitchTemplate_List(request):
    match (request.method):
        case "GET":
            data = VLANSwitchTemplate.objects.all()
            serializer = VLANSwitchTemplateSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VLANSwitchTemplateSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VLANSwitchTemplateSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VLANSwitchTemplateSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANSwitch_List(request):
    match (request.method):
        case "GET":
            data = VLANSwitch.objects.all()
            serializer = VLANSwitchSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VLANSwitchSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VLANSwitchSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VLANSwitchSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VLANValidID_List(request):
    match (request.method):
        case "GET":
            data = VLANValidID.objects.all()
            serializer = VLANValidIDSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VLANValidIDSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VLANValidIDSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VLANValidIDSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VS_List(request):
    match (request.method):
        case "GET":
            data = VS.objects.all()
            serializer = VSSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VSSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VSSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VSSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VSEnabledIPs_List(request):
    match (request.method):
        case "GET":
            data = VSEnabledIPs.objects.all()
            serializer = VSEnabledIPsSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VSEnabledIPsSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VSEnabledIPsSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VSEnabledIPsSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VSEnabledPorts_List(request):
    match (request.method):
        case "GET":
            data = VSEnabledPorts.objects.all()
            serializer = VSEnabledPortsSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VSEnabledPortsSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VSEnabledPortsSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VSEnabledPortsSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VSIPs_List(request):
    match (request.method):
        case "GET":
            data = VSIPs.objects.all()
            serializer = VSIPsSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VSIPsSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VSIPsSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VSIPsSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view('GET','POST')
def VSPorts_List(request):
    match (request.method):
        case "GET":
            data = VSPorts.objects.all()
            serializer = VSPortsSerializer(data, context={'request':request},many=True)
            return Response(serializer.data)
        case "POST":
            serializer = VSPortsSerializer(data=request.data)
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

    match (request.method):
        case "GET":
            serializer = VSPortsSerializer(req_object, context={'request': request}, many=False)
        case "POST":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "PATCH":
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        case "DELETE":
            req_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        case "PUT":
            serializer = VSPortsSerializer(req_object, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

