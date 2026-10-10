from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from .models import *
from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from .models import Course, Student

#обычный сериализатор курса
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title' , 'description']

#обычный сериализатор студента для КРАД
#при POST и PUT поле course передается через ID

class StudentSerializer(serializers.ModelSerializer):
    course_title = serializers.SerializerMethodField()
    is_new = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = [ 'id', 'full_name', 'email', 'course', 'course_title', 'is_new', 'created_at',]
        read_only_fields = ['id', 'created_at']

    def get_course_title(self, obj):
        return obj.course.title

    def get_is_new(self, obj):
        return obj.created_at >= timezone.now() - timedelta(days=7)


#сериализатор студента с вложенным курсом
class StudentWithCourseSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id' , 'full_name' , 'email' , 'course']
    def get_course(self, obj):
        return {
            'id' : obj.course.id ,
            'title' : obj.course.title ,
        }


#курс со списком студентов
class StudentShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email']
class CourseWithStudentsSerializer(serializers.ModelSerializer):
    students = StudentShortSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'students']


# курс с количеством студентов
class CourseCountSerializer(serializers.ModelSerializer):
    students_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'students_count']


# сериализатор итогового представления студента
class StudentRepresentationSerializer(serializers.ModelSerializer):
    is_new = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'course', 'is_new', ]
    def get_is_new(self, obj):
        return obj.created_at >= timezone.now() - timedelta(days=7)
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'student': { 'full_name': data['full_name'], 'email': data['email'], },
            'course': instance.course.title,
            'is_new': data['is_new'], }
