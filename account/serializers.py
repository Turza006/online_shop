from rest_framework import serializers
from .models import User
# from .models import Language
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'email','password','address', 'type')

