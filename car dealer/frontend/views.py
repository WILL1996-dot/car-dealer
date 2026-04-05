from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Dealer, Review
from .serializers import DealerSerializer, ReviewSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout

# Dealer API
class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

    @action(detail=False, methods=['get'])
    def by_state(self, request):
        state = request.query_params.get('state')
        dealers = Dealer.objects.filter(state__iexact=state)
        serializer = self.get_serializer(dealers, many=True)
        return Response(serializer.data)

# Review API
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Auth API
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful"})
        return Response({"message": "Invalid credentials"}, status=400)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})