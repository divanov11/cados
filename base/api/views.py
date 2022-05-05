from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from base.models import Post 

@api_view(['GET'])
def getRoutes(request):
    routes = {
        'users':'/api/users',
        'posts/':'/api/posts/'
    }
    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)