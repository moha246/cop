from rest_framework import viewsets
from .models import User, Group, Post,Comment
from .serializers import UserSerializer, GroupSerializer, PostSerializer,CommentSerializer,UserSerializerWithToken
from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer,
                                                  api_settings)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes                                                    




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PhemTokenPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serilizer = UserSerializerWithToken(self.user).data
        
        for k, v in serilizer.items():
            data[k] = v
        
        return data


class PhemTokenPairView(TokenObtainPairView):
    serializer_class = PhemTokenPairSerializer


class LogoutAPIView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            print(e)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def me(request):
    data = UserSerializerWithToken(request.user).data
    return Response(data, status=201)

