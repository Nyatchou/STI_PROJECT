from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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

class Chapter(models.Model):
    name = models.CharField(max_length = 100)
    text_description = models.TextField(default="")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    def __str__(self):
        return self.name

class Notion(models.Model):
    title = models.CharField(max_length=100)
    text_content = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='notions_chapter')
    def __str__(self):
        return self.title

class FileRessource(models.Model):
    CHOICES_RESSOURCES = (("video", "video"), ("document", "document"))
    ressource_type =  models.CharField(max_length=40, choices=CHOICES_RESSOURCES)
    ressource_file = models.FileField()
    notion = models.ForeignKey(Notion, on_delete=models.CASCADE, related_name='files_ressources')

class URLRessource(models.Model):
    url = models.URLField()
    notion = models.ForeignKey(Notion, on_delete=models.CASCADE, related_name='urls_ressources')


class CustomUser(AbstractUser):
    ROLES = (("ET", "ETUDIANT"), ("ENS", "ENSEIGNANT"), ("ADMINPL", "ADMINPLATEFORME"))
    role = models.CharField(max_length=30, choices=ROLES)
    date_of_birth = models.DateField(blank=True, null=True)

class CourseInscription(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, name, date_of_birth, role, password=None):
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            role=role,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, date_of_birth, role, password):
        user = self.create_user(
            email=email,
            password=password,
            role=None,
            date_of_birth=date_of_birth,
            name= "True",
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user