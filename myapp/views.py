from django.db.models import Count, Avg, Min, Max
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, Student
from .serializers import ( CourseSerializer, StudentSerializer, StudentWithCourseSerializer, CourseWithStudentsSerializer, CourseCountSerializer, StudentRepresentationSerializer,)

#course crud
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



#student crud
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.select_related('course').all().order_by('id')
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.select_related('course').all()
    serializer_class = StudentSerializer



#select_related
class StudentWithCourseListView(generics.ListAPIView):
    queryset = Student.objects.select_related('course').all().order_by('id')
    serializer_class = StudentWithCourseSerializer



#prefetch_related
class CourseWithStudentsListView(generics.ListAPIView):
    queryset = Course.objects.prefetch_related('students').all().order_by('id')
    serializer_class = CourseWithStudentsSerializer



#annotate + count
class CourseCountListView(generics.ListAPIView):
    queryset = Course.objects.annotate( students_count=Count('students') ).order_by('id')
    serializer_class = CourseCountSerializer



#aggregate statistics
@api_view(['GET'])
def statistics_view(request):
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    course_stats = Course.objects.annotate( student_count=Count('students')).aggregate(
        average_students=Avg('student_count'),
        min_students=Min('student_count'),
        max_students=Max('student_count'), )

    return Response({
        'total_students': total_students, 'total_courses': total_courses,
        'average_students': course_stats['average_students'],
        'min_students': course_stats['min_students'],
        'max_students': course_stats['max_students'], })



#serializermethodfield
class StudentMethodFieldListView(generics.ListAPIView):
    queryset = Student.objects.select_related('course').all().order_by('id')
    serializer_class = StudentSerializer



#to_representation
class StudentRepresentationListView(generics.ListAPIView):
    queryset = Student.objects.select_related('course').all().order_by('id')
    serializer_class = StudentRepresentationSerializer


