
from rest_framework.response import Response
from polls.models import *
from rest_framework.views import *
from rest_framework.decorators import *
from rest_framework.response import *

from polls.serializers import  *
from .models import *



@api_view(['POST'])
def makeContract(request):
    data=request.data
    male_firstName=data['male_firstName']
    male_lastName=data['male_lastName']
    femaleFather_firstName=data['femaleFather_firstName']
    femaleFather_lastName=data['femaleFather_lastName']
    place=data['place']
    placeType=data['placeType']
    query=MarriageContract.objects.filter(male_firstName=male_firstName,male_lastName=male_lastName,femaleFather_firstName=femaleFather_firstName,femaleFather_lastName=femaleFather_lastName)
    if query.exists():
        message = {'detail': 'this marriage contract already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    contract=MarriageContract(male_firstName=male_firstName,male_lastName=male_lastName,femaleFather_firstName=femaleFather_firstName,femaleFather_lastName=femaleFather_lastName,place=place,placeType=placeType)
    contract.save()
    message = {'detail': 'the marriage contract was send successfully'}
    return Response(message)


@api_view(['POST'])
def makeDate(request):

    data=request.data
    male_firstName=data['male_firstName']
    male_lastName=data['male_lastName']
    male_phoneNumber=data['male_phoneNumber']
    femaleFather_firstName=data['femaleFather_firstName']
    femaleFather_lastName=data['femaleFather_lastName']
    weekDay=data['weekDay']
    hijriDay=data['hijriDay']
    hijriMonth=data['hijriMonth']
    hijriYear=data['hijriYear']
    date=data['date']
    place=data['place']
    placeType=data['placeType']
    location=data['location']
    locationUrl=data['locationUrl']
    image=data['image']
    query=MarriageDate.objects.filter(male_firstName=male_firstName,
    male_lastName=male_lastName,
    femaleFather_firstName=femaleFather_firstName,
    femaleFather_lastName=femaleFather_lastName)
    if query.exists():
        message = {'detail': 'this marriage Date already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    Dat=MarriageDate(male_firstName=male_firstName,
    male_lastName=male_lastName,
    male_phoneNumber=male_phoneNumber,
    femaleFather_firstName=femaleFather_firstName,
    femaleFather_lastName=femaleFather_lastName,
    weekDay=weekDay,
    hijriDay=hijriDay,
    hijriMonth=hijriMonth,
    hijriYear=hijriYear,
    date=date,
    place=place,
    placeType=placeType,
    location=location,
    locationUrl=locationUrl,
    image=image
    )
    Dat.save()
    message = {'detail': 'the marriage Date was send successfully'}
    return Response(message)


@api_view(['GET', 'POST'])
def contract(request):
    if request.method == 'GET' : 
        query=MarriageContract.objects.filter(accept=False)
        serializer=MarriageContractSerializer(query,many=True)
        return Response({"datail":serializer.data})
    if request.method == 'POST' : 
        data=request.data
        cid=data['cid']
        accept=data['accept']
        query=MarriageContract.objects.get(id=cid)
        if accept==True:
            
            query.accept=True
            query.save() 
            message = {'detail': 'accept this marriage Contract'}
            return Response(message)
        else:
            query.accept=False
            query.save() 
            message = {'detail': 'reject this marriage Contract'}
            return Response(message)

