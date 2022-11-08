# Generated by Django 4.1.2 on 2022-11-01 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="questions",
            name="companyId",
        ),
        migrations.AlterField(
            model_name="options",
            name="questionId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="exams.questions",
            ),
        ),
    ]