
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser,PatientProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password','groups','user_permissions','is_staff','last_login','is_active']
        
        
class RegisterSeializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=128)
    class Meta:
        model = CustomUser
        fields = ['username','password','confirm','email','first_name','last_name']
        
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError('Password Confirm bilan bir xil emas')
        return super().validate(attrs)
    
    
    def create(self, validated_data):
        validated_data.pop('confirm')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    
    
class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
    )
    

class PatientProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = PatientProfile
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_of_birth',
            'gender',
        )
    


