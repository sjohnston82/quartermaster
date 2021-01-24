from rest_framework import serializers
from quartermaster import models
from django.contrib.auth import get_user_model

User = get_user_model()


class NestedPantrySerializer(serializers.ModelSerializer):
    expiration_date = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        fields = (
            'id', 
            'item_name', 
            'create_date',
            'expiration_date',
            'owner',
            'getting_low',
            
            'category',
            'quantity',
            'to_grocery',
            'slug',
            'amount_type',
            'expiring_soon',
            'brand',
            
        )
        model = models.PantryItem

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class UserSerializer(serializers.ModelSerializer):
    pantry_items = NestedPantrySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'pantry_items')

class PantrySerializer(serializers.ModelSerializer):
    owner_detail = NestedUserSerializer(read_only=True, source='owner')
    expiration_date = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        model = models.PantryItem
        fields = (
            'id', 
            'item_name', 
            'create_date',
            'expiration_date',
            'owner',
            'owner_detail',
            'getting_low',
            
            'category',
            'quantity',
            'to_grocery',
            'slug',
            'amount_type',
            'expiring_soon',
            'brand',
            
            
        )

