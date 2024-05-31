from rest_framework import serializers
from .models import TODO


class TODOserializer(serializers.ModelSerializer):

        class Meta:
                model = TODO
                fields = '__all__'