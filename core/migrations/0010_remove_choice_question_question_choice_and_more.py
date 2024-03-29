# Generated by Django 5.0.1 on 2024-01-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_question_correlation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='choice',
            field=models.ManyToManyField(to='core.choice'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(choices=[(0, 'Neutral'), (1, 'Strongly Agree'), (2, 'Agree'), (3, 'Disagree'), (4, 'Strongly Disagree')], default=0, max_length=20),
        ),
    ]
