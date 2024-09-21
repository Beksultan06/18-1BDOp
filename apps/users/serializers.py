from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=155, write_only=True
    )
    password2 = serializers.CharField(
        max_length=155, write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'password', 'password2')

    def validate(self, attrs):
        passwords = ['qwert', '1234']
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2': 'Пароли отличается'})
        for password in passwords:
            if password in attrs['password']:
                raise serializers.ValidationError({'password2' : 'Пароль слишком легкий'})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password': 'Меньше 8 символов'})

        return attrs

    def create(self, validate_data):
        validate_data.pop('password2')
        user = User.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            phone_number = validate_data['phone_number']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user