from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveAPIView
from stibackend.models import *

from rest_auth.registration.views import RegisterView

class CustomRegisterView(RegisterView):
    queryset = CustomUser.objects.all()

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

class ListAllCourseAPIView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class ListCourseAPIView(ListAPIView):
    serializer_class = CourseSerializer
    def get_queryset(self):
        domain_id = self.kwargs.get('domain_id')
        return Course.objects.filter(domain=domain_id)
 

class CreateNotionAPIView(CreateAPIView):
    serializer_class = NotionSerializer
    queryset = Notion.objects.all()


class CreateChapterAPIView(CreateAPIView):
    serializer_class = SimpleChapterSerializer
    queryset = Chapter.objects.all()

class ChapterExtendAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

class CourseChaptersListAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Course.objects.all()
    serializer_class = CourseChapterSerializer


class DomainExtendAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = StudyDomainExtendSerializer
    queryset = StudyDomain.objects.all()

class NotionExtendAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = NotionExtendSerializer
    queryset = Notion.objects.all()

class CreateFileRessourceAPIView(CreateAPIView):
    serializer_class = FileRessourceCreateSerializer
    queryset = FileRessource.objects.all()

class CreateURLRessourceAPIView(CreateAPIView):
    serializer_class = URLRessourceCreateSerializer
    queryset = URLRessource.objects.all()