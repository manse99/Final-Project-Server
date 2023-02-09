from rest_framework import viewsets

from .serializers import UserSerializer,PostSerializer,CommentsSerializer,SubsSerializer
from .models import User,Post,Subs,Comments

class PostViewSet(viewsets.ModelViewSets):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSets):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SubsViewSet(viewsets.ModelViewSets):
    queryset = Subs.objects.all()
    serializer_class = SubsSerializer

class CommentsViewSet(viewsets.ModelViewSets):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer