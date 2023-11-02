from rest_framework import serializers
from .models import Course

# Serializer lay du lieu tu model dua qua jason vva dua ve cho client nguoc lai
#model serializer


class getAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')
