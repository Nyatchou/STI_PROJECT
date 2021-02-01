from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveAPIView
from stibackend.models import *

class CreateStudyDomainView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      domainSerializer = StudyDomainSerializer(data=request.data)

      if domainSerializer.is_valid():
          domainSerializer.save()
          return Response(domainSerializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(domainSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListDomainAPIView(ListAPIView):
    serializer_class = StudyDomainSerializer
    queryset = StudyDomain.objects.all()


class CreateListCourseAPIView(ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        domain_id = self.kwargs.get('domain_id')
        return Course.objects.filter(domain=domain_id)


class ListCourseAPIView(ListAPIView):
    serializer_class = CourseExtendSerializer
    def get_queryset(self):
        domain_id = self.kwargs.get('domain_id')
        return Course.objects.filter(domain=domain_id)
 

class CreateSectionCourse(CreateAPIView):
    serializer_class = SectionCourseForCreateSerializer
    queryset = SectionCourse.objects.all()


class CourseExtendAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = CourseExtendSerializer
    queryset = Course.objects.all()


class SectionCourseRetrieveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = SectionCourseSerializer
    queryset = SectionCourse.objects.all()

class DomainExtendAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = StudyDomainExtendSerializer
    queryset = StudyDomain.objects.all()