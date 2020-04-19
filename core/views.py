from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup
from csv import writer

# Create your views here.

class Scraper(APIView):

    def get(self, request):
        category = request.query_params.get('category', None)
        link = "https://inshorts.com/en/read/" + category

        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all(itemprop = "headline")

        news_headline = []
        for headline in headlines:
            news_headline.append(headline.get_text())

        contents = soup.find_all(itemprop = "articleBody")

        news_content = []
        for content in contents:
            news_content.append(content.get_text())

        news = []

        for i in range (len(news_content)):
            shorts = {"headline" : news_headline[i], "content" : news_content[i]}
            news.append(shorts)

        if (len(news)!=0):
            return Response({"news" : news}, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_404_NOT_FOUND)



