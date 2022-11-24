# Generated by Django 4.1.2 on 2022-11-21 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0001_initial"),
        ("Company", "0001_initial"),
        ("exams", "0002_examduration_companyid_examduration_jobid"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExamResult",
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
                ("totalScore", models.FloatField()),
                (
                    "candidateId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="can",
                        to="resume.candidate",
                    ),
                ),
                (
                    "companyId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="compR",
                        to="Company.companies",
                    ),
                ),
                (
                    "jobId",
                    models.ForeignKey(
                        default=13,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="joR",
                        to="Company.job_profiles",
                    ),
                ),
            ],
        ),
    ]
