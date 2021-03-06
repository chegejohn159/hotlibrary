# Generated by Django 2.1.7 on 2019-04-13 10:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_lecturer', models.BooleanField(default=False)),
                ('is_librarian', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminChallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_name', models.CharField(max_length=50)),
                ('challenge_category', models.CharField(choices=[('PROGRAMMING', 'Programming'), ('NETWORKING', 'Networking'), ('BLOCKCHAIN', 'Blockchain'), ('DATASCIENCE', 'Data Science'), ('WEBDEV', 'Web Development'), ('SCRIPTING', 'Scripting'), ('A-INTELLIGENCE', 'Artificial Intelligence')], max_length=15)),
                ('challenge_level', models.CharField(choices=[('BEGINNER', 'Beginner Level'), ('INTERMEDIATE', 'Intermediate Level'), ('ADVANCED', 'Advanced Level')], max_length=13)),
                ('challenge_description', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('path', models.TextField(blank=True, null=True)),
                ('size', models.BigIntegerField(default=0)),
                ('file_type', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uploaded', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'HotLib Challenges ',
            },
        ),
        migrations.CreateModel(
            name='AdminHowToRepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('howto_description', models.TextField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('path', models.TextField(blank=True, null=True)),
                ('size', models.BigIntegerField(default=0)),
                ('file_type', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uploaded', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'HotLib HowTO ',
            },
        ),
        migrations.CreateModel(
            name='AdminResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_type', models.CharField(choices=[('PROGRAMMING', 'Programming'), ('NETWORKING', 'Networking'), ('BLOCKCHAIN', 'Blockchain'), ('DATASCIENCE', 'Data Science'), ('WEBDEV', 'Web Development'), ('SCRIPTING', 'Scripting'), ('A-INTELLIGENCE', 'Artificial Intelligence')], max_length=15)),
                ('resource_name', models.CharField(max_length=50)),
                ('resource_description', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('path', models.TextField(blank=True, null=True)),
                ('size', models.BigIntegerField(default=0)),
                ('file_type', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uploaded', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'HotLib Resources',
            },
        ),
        migrations.CreateModel(
            name='AdminTutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_type', models.CharField(choices=[('TUTORIAL', 'Hot Tutorials'), ('PDF', 'Free Pdfs'), ('CHALLENGES', 'Challenges')], max_length=10)),
                ('tutorial_name', models.CharField(max_length=50)),
                ('tutorial_description', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('path', models.TextField(blank=True, null=True)),
                ('size', models.BigIntegerField(default=0)),
                ('file_type', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uploaded', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'HotLib Tutorials',
            },
        ),
        migrations.CreateModel(
            name='DeptCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Department Courses',
            },
        ),
        migrations.CreateModel(
            name='DeptUnit',
            fields=[
                ('unit_code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('unit_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotlibrary.DeptCourse')),
            ],
            options={
                'db_table': 'Units',
            },
        ),
        migrations.CreateModel(
            name='LecturerResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_type', models.CharField(choices=[('NOTES', 'Lecturer Notes'), ('ASSIGNMENT', 'Assignments|CATS'), ('BOOKS', 'Extra Class Books')], max_length=10)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('path', models.TextField(blank=True, null=True)),
                ('size', models.BigIntegerField(default=0)),
                ('file_type', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uploaded', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotlibrary.DeptCourse')),
            ],
            options={
                'db_table': 'Lecturer Uploads',
            },
        ),
        migrations.CreateModel(
            name='LibrarianResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=20)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('path', models.TextField(blank=True, null=True)),
                ('size', models.BigIntegerField(default=0)),
                ('file_type', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uploaded', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Librarian Uploads',
            },
        ),
        migrations.CreateModel(
            name='MsuDepartmentList',
            fields=[
                ('dept_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='MsuFacultyList',
            fields=[
                ('faculty_code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('faculty_name', models.CharField(max_length=50)),
                ('faculty_dean', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'MSU Faculty',
            },
        ),
        migrations.CreateModel(
            name='StudySemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('SEM1', 'Semester 1'), ('SEM2', 'Semester 11')], max_length=4)),
                ('academic_year', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Semester',
            },
        ),
        migrations.AddField(
            model_name='msudepartmentlist',
            name='faculty_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotlibrary.MsuFacultyList'),
        ),
        migrations.AddField(
            model_name='librarianresource',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotlibrary.MsuDepartmentList'),
        ),
        migrations.AddField(
            model_name='librarianresource',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lecturerresource',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotlibrary.StudySemester'),
        ),
        migrations.AddField(
            model_name='lecturerresource',
            name='unit_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotlibrary.DeptUnit'),
        ),
        migrations.AddField(
            model_name='lecturerresource',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deptunit',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotlibrary.MsuDepartmentList'),
        ),
        migrations.AddField(
            model_name='deptunit',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotlibrary.StudySemester'),
        ),
        migrations.AddField(
            model_name='deptcourse',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotlibrary.MsuDepartmentList'),
        ),
    ]
