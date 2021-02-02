from django.urls import path, include
from .views import *
urlpatterns = [
    path('domain/create/', CreateStudyDomainView.as_view(), name='create-domain'),
    path('domains/', ListDomainAPIView.as_view(), name='list-domain'),
    path('courses/<int:domain_id>', ListCourseAPIView.as_view(), name='list-course'),
    path('course/', CreateListCourseAPIView.as_view(), name='listcreate-course'),
    # path('sectioncourse/create/', CreateSectionCourse.as_view(), name='create-sectioncourse'),
    path('allcourses/', ListAllCourseAPIView.as_view()),
    # path('sectionscourse/<int:pk>', SectionCourseRetrieveAPIView.as_view(), name='sectionscourse' ),
    path('domains/<int:pk>', DomainExtendAPIView.as_view(), name='domain-extend'),
    path('chapters/<int:course_id>', CourseChaptersListAPIView.as_view()),
    path('notions/<int:chapter_id>', ChapterExtendAPIView.as_view()),
    path('createchap/', CreateChapterAPIView.as_view()),
    path('createnotion/', CreateNotionAPIView.as_view()),
    path('notion/<int:pk>', NotionExtendAPIView.as_view()),
    path('fileadd/', CreateFileRessourceAPIView.as_view()),
    path('urladd/', CreateURLRessourceAPIView.as_view()),
    path('chapter/<int:pk>', ChapterExtendAPIView.as_view()),
    # path('urladd/', CreateURLRessourceAPIView.as_view()),

]
