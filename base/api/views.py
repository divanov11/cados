from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import *
from base.models import Post, Profile, Company
from django.contrib.auth.models import User 


@api_view(['GET'])
def getRoutes(request):
    routes = {
        'users':'/api/users',
        'user object':'/api/users/<username>',
        'posts':'/api/posts/',
        'post object':'/api/posts/<pk>',
        'post add':'/api/posts/add/<pk>',
        'post update':'/api/posts/edit/<pk>',
        'post delete':'/api/posts/delete/<pk>',
        
    }
    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addPost(request):
    data = request.data
    user = request.user
    post = Post.objects.create(
        owner=user,
        body=data['body']
    )
    serializer = PostSerializer(post, many=False)
    return Response({'message':'Post was added!', 'data':serializer.data})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editPost(request, pk):
    data = request.data
    user = request.user


    post = Post.objects.get(id=pk)
    if user == post.owner:            
        post.body = data['body']
        post.save()

        serializer = PostSerializer(post, many=False)
        return Response({'message':'Post was updated!', 'data':serializer.data})
    else:
        return Response('Get the hell out!')


@api_view(['DELETE'])
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    user = request.user
    if user == post.owner:    
        post.delete()
        return Response('Post was deleted')
    else:
        return Response('Get the hell out!')

@api_view(['GET'])
def getPost(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = Profile.objects.all()
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRecommendedUsers(request):
    users = Profile.objects.filter(verified=True).order_by('?')[0:10]
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, username):
    user = Profile.objects.get(user__username=username)
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getCompanies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCompany(request, pk):
    company = Company.objects.get(id=pk)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getLatestJobs(request):
    latestJobs = JobOpening.objects.all().order_by('-created')[0:10]
    serializer = JobOpeningSerializer(latestJobs, many=True)
    return Response(serializer.data)