from rest_framework import viewsets
from .models import User, Group, Post, Comment
from .serializers import (
    UserSerializer,
    GroupSerializer,
    PostSerializer,
    CommentSerializer,
    UserSerializerWithToken,
    JWTTokenObtainPairSerializer,
    ConfirmAccountSerializer,
    JWTTokenObtainPairSerializer,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework import views
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
import sendgrid
from sendgrid.helpers.mail import Mail


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by()
    serializer_class = UserSerializer

    @action(detail=True)
    def me(request):
        data = UserSerializerWithToken(request.user).data
        return Response(data, status=status.HTTP_201_CREATED)

# added this new
class ConfirmAccountView(APIView):
    def post(self, request):
        serializer = ConfirmAccountSerializer(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JWTTokenObtainPairView(TokenObtainPairView):
    serializer_class = JWTTokenObtainPairSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.order_by()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by()
    serializer_class = CommentSerializer



class JWTTokenObtainPairSerializer(TokenObtainPairView):
    serializer_class = JWTTokenObtainPairSerializer


class LogoutAPIView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            print(e)
        return Response(status=status.HTTP_200_OK)

# added this new
class RegisterView(views.APIView):
   def post(self, request):
            # Create a new user
     if User.objects.filter(email=request.data['email']).exists():
        return Response("User already exists with this email address", status=400)
     else:
        user = User.objects.create(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )
        user.save()
        
        # Send confirmation email
        subject = "Confirm Your Email Address"
        message = "Please click the link below to confirm your email address: http://localhost:8000/confirm{}".format(user.email)
        
        sg = sendgrid.SendGridAPIClient(api_key="api key")
        from_email = "musamohammaddal@gmail.com"
        to_email = user.email
        mail = Mail(from_email, subject, to_email, message)
        sg.send(mail)
        
        return Response(status=201)