# Generated by Django 4.1.2 on 2022-10-18 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Companies",
            fields=[
                ("company_name", models.CharField(max_length=100)),
                ("company_contact_no", models.CharField(max_length=100)),
                ("company_email", models.CharField(max_length=100)),
                (
                    "companyuserid",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("state", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("pass1", models.CharField(default="", max_length=10)),
                ("pass2", models.CharField(default="", max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Job_Profiles",
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
                ("profile_name", models.CharField(max_length=100)),
                ("job_info", models.TextField()),
                ("salary", models.IntegerField()),
                (
                    "company_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Company.companies",
                    ),
                ),
            ],
        ),
    ]
