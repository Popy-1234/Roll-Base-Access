# Generated by Django 5.1.1 on 2024-09-14 03:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=100, null=True)),
                ('Contact_number', models.CharField(max_length=100, null=True)),
                ('Career_Summary', models.TextField(max_length=100, null=True)),
                ('Experience_Title', models.CharField(max_length=100, null=True)),
                ('Skill_title', models.CharField(max_length=100, null=True)),
                ('Education_Title', models.CharField(max_length=100, null=True)),
                ('Language', models.CharField(max_length=100, null=True)),
                ('Interest', models.CharField(max_length=100, null=True)),
                ('Profile_Pic', models.ImageField(null=True, upload_to='Media/Profile_Pic')),
                ('Linkedin_URL', models.URLField(max_length=100, null=True)),
                ('Facebook_URL', models.URLField(max_length=100, null=True)),
                ('Instagram_URL', models.URLField(max_length=100, null=True)),
                ('GitHub_URL', models.URLField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
