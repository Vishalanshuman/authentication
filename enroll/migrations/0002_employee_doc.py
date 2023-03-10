# Generated by Django 4.0.8 on 2023-01-25 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_card', models.CharField(max_length=12)),
                ('adhar_card_file', models.ImageField(upload_to='adhar_card_file')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
