from django.db import models
from django.contrib.auth.models import AbstractUser

from hotlibalphaV1 import settings
from hotlibrary.choices import *


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


class FileItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    @property
    def title(self):
        return str(self.name)


class AdminTutorial(models.Model):
    tutorial_type = models.CharField(max_length=10, choices=TutorialTypes)
    tutorial_name = models.CharField(max_length=50)
    tutorial_description = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.tutorial_name, self.tutorial_url)

    class Meta:
        db_table = 'HotLib Tutorials'


class AdminResource(models.Model):
    resource_type = models.CharField(max_length=15, choices=ResourceTypes)
    resource_name = models.CharField(max_length=50)
    resource_description = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.resource_name, self.resource_url)

    class Meta:
        db_table = 'HotLib Resources'


class AdminChallenge(models.Model):
    challenge_name = models.CharField(max_length=50)
    challenge_category = models.CharField(max_length=15, choices=ResourceTypes)
    challenge_level = models.CharField(max_length=13, choices=ChallengeLevel)
    challenge_description = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.challenge_name

    class Meta:
        db_table = 'HotLib Challenges '


class AdminHowToRepo(models.Model):
    howto_description = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.howto_description

    class Meta:
        db_table = 'HotLib HowTO '


class MsuFacultyList(models.Model):
    """ MSU FACULTY LIST model."""
    faculty_code = models.CharField(primary_key=True, max_length=8)
    faculty_name = models.CharField(max_length=50)
    faculty_dean = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.faculty_name

    class Meta:
        db_table = 'MSU Faculty'


class MsuDepartmentList(models.Model):
    """Master MSU DEPARTMENT LIST model."""
    dept_id = models.CharField(primary_key=True, max_length=8)
    dept_name = models.CharField(max_length=50)
    faculty_name = models.ForeignKey(MsuFacultyList, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.dept_name, self.faculty_name)

    class Meta:
        db_table = 'Department'


class StudySemester(models.Model):
    """ MSU SEMESTER LIST model."""
    semester = models.CharField(max_length=4, choices=stdySemester)
    academic_year = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.semester, self.academic_year)

    class Meta:
        db_table = 'Semester'


class DeptCourse(models.Model):
    course_name = models.CharField(max_length=50)
    department = models.ForeignKey(MsuDepartmentList, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'Department Courses'


class DeptUnit(models.Model):
    """ DEPT UNIT LIST model."""
    unit_code = models.CharField(primary_key=True, max_length=6)
    unit_name = models.CharField(max_length=50)
    department = models.ForeignKey(MsuDepartmentList, on_delete=models.CASCADE)
    course = models.ForeignKey(DeptCourse, on_delete=models.CASCADE)
    semester = models.ForeignKey(StudySemester, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.unit_code

    class Meta:
        db_table = 'Units'


class LecturerResource(models.Model):
    course = models.ForeignKey(DeptCourse, on_delete=models.CASCADE)
    unit_code = models.ForeignKey(DeptUnit, on_delete=models.CASCADE)
    semester = models.ForeignKey(StudySemester, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=10, choices=lecturer_resources)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Lecturer Uploads'


class LibrarianResource(models.Model):
    academic_year = models.CharField(max_length=20)
    course_name = models.ForeignKey(MsuDepartmentList, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Librarian Uploads'
