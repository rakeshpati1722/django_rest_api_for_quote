from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from . serializers import abcSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import QuoteModel
from app.serializers import quoteSerializer

# Create your views here.
class quoteList(APIView):
    def get(self, request):
        xyz = QuoteModel.objects.all()
        serializer = quoteSerializer(xyz, many = True)
        return Response(serializer.data)
    
class quotepost(APIView):
    def post(self,request):

        print("\nrequest value--------------->",request.data)
        serializer_data = quoteSerializer(data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_data,status=status.HTTP_400_BAD_REQUEST)
         
class quoteUpdate(APIView):
    def get(self, request,pk):
        xyz = QuoteModel.objects.filter(id=pk)
        serializer = quoteSerializer(xyz, many = True)
        return Response(serializer.data)

    def put(self,request,pk):
        existing_data = QuoteModel.objects.get(id=pk)
        d = request.data
        serializer_data = quoteSerializer(existing_data,data=d)
        if serializer_data.is_valid():
            serializer_data.save()
            content = {'message':'data inserted'}
            return Response(content,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
class quoteDelete(APIView):
    def delete(self,request,pk):
        # print("hitting into api")
        to_delete = QuoteModel.objects.filter(id=pk)       
        a = to_delete.delete()
        content = {'message':'data deleted'}
        return Response(content,status=status.HTTP_200_OK)


import urllib.request
from bs4 import BeautifulSoup

class GenerateQuote(APIView):
    def get(self,request):
        url = 'https://www.goodreads.com/'
        
        quote_from_good_read = urllib.request.urlopen(url)

        soup = BeautifulSoup(quote_from_good_read)

        div_tags = soup.find("div",class_='featureTeaserBox__quotesBox').find("div",class_="featureTeaserBox__quotesBoxQuote")

        all_quotes = div_tags.findAll("div",class_="quoteText")

        final_data = []
        for i in all_quotes:
            q = i.find(text=True)
            q = q.replace("\n",'')
            q = q.lstrip()
            q = q.rstrip()
            a = i.find("span",class_="authorOrTitle").find(text=True)
            a = a.replace("\n",'')
            a = a.lstrip()
            a = a.rstrip()
            data = {
                "quote":q,
                "author":a
            }
            final_data.append(data)

        len_list = len(final_data)
        for k in range(0,len_list):
            quote = final_data[k]['quote']
            author = final_data[k]['author']

            print("data is saving")
            try:
                quote = QuoteModel(Quote=quote,Author=author)
                quote.save()
                print("data is saved")
            except:
                print("data is not saved")
                
        content = {"quote uploaded":final_data}
        return Response(content,status=status.HTTP_200_OK)

