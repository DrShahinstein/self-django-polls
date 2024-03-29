# Generated by Django 5.0.1 on 2024-01-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_correlation_agreement_alter_question_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correlation',
            field=models.IntegerField(choices=[(1, '1 - Strongly Disagree'), (2, '2 - Disagree'), (3, '3 - Slightly Disagree'), (4, '4 - Neutral'), (5, '5 - Slightly Agree'), (6, '6 - Agree'), (7, '7 - Strongly Agree')], default=4, verbose_name='Correlation'),
        ),
        migrations.DeleteModel(
            name='Correlation',
        ),
    ]
