# Generated by Django 5.1.6 on 2025-02-17 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Skills', models.ManyToManyField(related_name='jobs', to='skills.skill')),
            ],
        ),
    ]
