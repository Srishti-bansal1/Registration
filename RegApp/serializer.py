from .models import Registration
from rest_framework import serializers

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('id','name', 'dob','email','email','state','city','pin')
