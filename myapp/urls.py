from django.urls import path
from .views import ( CourseListCreateView, CourseDetailView, StudentListCreateView, StudentDetailView,
    StudentWithCourseListView, CourseWithStudentsListView, CourseCountListView, statistics_view,
    StudentMethodFieldListView, StudentRepresentationListView, )

urlpatterns = [
    # course crud
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    # student crud
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

    # select related
    path( 'students-with-courses/', StudentWithCourseListView.as_view(), name='students-with-courses' ),

    #prefetch_related
    path( 'courses-with-students/', CourseWithStudentsListView.as_view(), name='courses-with-students'),

    # annotate + count
    path('courses-count/', CourseCountListView.as_view(), name='courses-count'),

    #aggregate statistics
    path('statistics/', statistics_view, name='statistics'),

    #SerializerMethodField
    path( 'students-method-fields/', StudentMethodFieldListView.as_view(), name='students-method-fields'),

    #to_representation
    path( 'students-representation/', StudentRepresentationListView.as_view(), name='students-representation'),
]
