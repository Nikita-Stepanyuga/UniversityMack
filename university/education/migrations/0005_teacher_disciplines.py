# Generated by Django 5.1.5 on 2025-04-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_alter_department_head_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='disciplines',
            field=models.ManyToManyField(through='education.Teaches', to='education.discipline'),
        ),
    ]
