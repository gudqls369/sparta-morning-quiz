from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.models import Article
from articles.serializers import ArticleSerializer

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        print('get!!')
        return Response({'message': 'get success!!'})
    
    if request.method == 'POST':
        print('post!!')
        return Response({'message': 'post success!!'})
    
class ArticleView(APIView):
    def get(self,request):
        all_articles = Article.objects.all()
        
        return Response(ArticleSerializer(all_articles, many=True).data)
    
    def post(self, request):
        article = ArticleSerializer(data=request.data)
        #검증
        article.is_valid(raise_exception=True)
        #생성
        article.save()
        
        return(article.data)