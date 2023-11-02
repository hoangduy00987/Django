from rest_framework import  serializers

from course.models import Course


class GetAllCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'title', )