from rest_framework import serializers
from stibackend.models import * 
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'date_of_birth']

    
class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    role = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'date_of_birth': self.validated_data.get('date_of_birth', ''),
            'role': self.validated_data.get('role', ''),
        }

class StudyDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDomain
        fields = '__all__'
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudyDomainExtendSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = StudyDomain
        fields = ['pk', 'name', 'image', 'courses']


class NotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notion
        fields = '__all__'

class FileRessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileRessource
        fields = ['ressource_type', 'ressource_file']

class URLRessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLRessource
        fields = ['url']


class NotionExtendSerializer(serializers.ModelSerializer):
    files_ressources = FileRessourceSerializer(many=True, read_only=True)
    urls_ressources = URLRessourceSerializer(many=True, read_only=True)
    class Meta:
        model = Notion
        fields = ['title', 'text_content', 'files_ressources', 'urls_ressources']

class SimpleChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    notions_chapter = NotionSerializer(many=True, read_only = True)
    class Meta:
        model = Chapter
        fields = ['pk', 'name', 'text_description', 'notions_chapter']

class CourseChapterSerializer(serializers.ModelSerializer):
    chapters  = ChapterSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['pk', 'name', 'text_description', 'chapters']

class FileRessourceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileRessource
        fields = '__all__'

class URLRessourceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLRessource
        fields = '__all__'





