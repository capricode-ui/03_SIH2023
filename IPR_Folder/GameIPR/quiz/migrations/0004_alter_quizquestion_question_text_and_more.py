# Generated by Django 4.2.5 on 2023-09-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quizquestion_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='question_text',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='solution_text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
