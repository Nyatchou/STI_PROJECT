from django.urls import path, include
from .views import *
urlpatterns = [
    path('domain/create/', CreateStudyDomainView.as_view(), name='create-domain'),
    path('domains/', ListDomainAPIView.as_view(), name='list-domain'),
    path('courses/<int:domain_id>', ListCourseAPIView.as_view(), name='list-course'),
    path('course/', CreateListCourseAPIView.as_view(), name='listcreate-course'),
    path('sectioncourse/create/', CreateSectionCourse.as_view(), name='create-sectioncourse'),
    path('course/<int:pk>', CourseExtendAPIView.as_view(), name='course-extend' ),
    path('sectionscourse/<int:pk>', SectionCourseRetrieveAPIView.as_view(), name='sectionscourse' ),
    path('domains/<int:pk>', DomainExtendAPIView.as_view(), name='domain-extend' ),

]
