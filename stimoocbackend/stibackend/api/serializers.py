from rest_framework import serializers
from stibackend.models import StudyDomain, Course, SectionCourse 

class StudyDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDomain
        fields = '__all__'
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SectionCourseSerializer(serializers.ModelSerializer):
    subsections = serializers.SerializerMethodField(read_only=True, method_name="get_children_courses")
    class Meta:
        model = SectionCourse
        fields = ['name', 'text_content', 'subsections']

    def get_children_courses(self, obj):
        serializer = SectionCourseSerializer(instance=SectionCourse.objects.filter(section_parent=obj), many=True)
        return serializer.data

class SectionCourseForCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionCourse
        fields = '__all__'

class StudyDomainExtendSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = StudyDomain
        fields = ['pk', 'name', 'image', 'courses']



class CourseExtendSerializer(serializers.ModelSerializer):
    section_courses = SectionCourseSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['pk', 'name', 'section_courses']


# class SectionCourseSerializer(serializers.ModelSerializer):
#     section_parent = serializers.SerializerMethodField()
#     class Meta:
#         model = SectionCourse
#         fields = ['pk' ,'name', 'text_content', 'section_parent']

#     def get_section_parent(self, obj):
#         if obj.parent is not None:
#             return SectionCourseSerializer(obj.section_parent)
#         else:
#             return None



