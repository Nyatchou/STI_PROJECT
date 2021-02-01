from django.db import models

# Create your models here.
class StudyDomain(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length = 100)
    text_description = models.TextField(default="")
    domain = models.ForeignKey(StudyDomain, on_delete=models.CASCADE, related_name='courses')
    def __str__(self):
        return self.name

class SectionCourse(models.Model):
    name = models.CharField(max_length = 100)
    text_content = models.TextField()
    section_parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE, related_name='section_courses')
    def __str__(self):
        return self.name
        