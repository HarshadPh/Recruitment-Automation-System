# Generated by Django 4.1.2 on 2022-11-21 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("candidate_name", models.CharField(max_length=20000)),
                ("candidate_email", models.CharField(max_length=100)),
                ("pass1", models.CharField(default="", max_length=10)),
                ("pass2", models.CharField(default="", max_length=10)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("phno", models.CharField(max_length=1000)),
                ("address", models.CharField(max_length=7000)),
                ("college", models.CharField(max_length=4000)),
                ("cgpa", models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="resumedata",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20000)),
                ("phno", models.CharField(max_length=1000)),
                ("address", models.CharField(max_length=7000)),
                ("college", models.CharField(max_length=4000)),
                ("cgpa", models.CharField(max_length=2000)),
                ("comname", models.CharField(max_length=40000)),
                ("brief", models.CharField(max_length=200000)),
                ("start", models.CharField(max_length=4000)),
                ("end", models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name="Work_Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("companyName", models.TextField(max_length=100)),
                ("workDetails", models.TextField(max_length=5000)),
                ("internship", models.BooleanField(default=False)),
                (
                    "candidateId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work",
                        to="resume.candidate",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("skill", models.TextField(max_length=100)),
                (
                    "candidateId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skill",
                        to="resume.candidate",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("prj_name", models.TextField(max_length=100)),
                ("prj_link", models.TextField(max_length=100)),
                ("prj_des", models.TextField(max_length=5000)),
                (
                    "candidateId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project",
                        to="resume.candidate",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course", models.TextField(max_length=100)),
                ("platform", models.TextField(default="Edx", max_length=100)),
                (
                    "candidateId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course",
                        to="resume.candidate",
                    ),
                ),
            ],
        ),
    ]