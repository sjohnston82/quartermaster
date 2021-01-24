from rest_framework import generics, viewsets, permissions, filters
from django.contrib.auth import get_user_model
from quartermaster import models
from .serializers import PantrySerializer, UserSerializer
from accounts.models import CustomUser

User = get_user_model()

class PantryViewSet(viewsets.ModelViewSet):
    queryset = models.PantryItem.objects.all()
    serializer_class = PantrySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('item_name', 'category', 'brand')

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteView(generics.DestroyAPIView):
    serializer_class = PantrySerializer
    queryset = models.PantryItem.objects.all()

class UpdateItem(generics.UpdateAPIView):
    serializer_class = PantrySerializer(partial=True)
    queryset = models.PantryItem.objects.all()