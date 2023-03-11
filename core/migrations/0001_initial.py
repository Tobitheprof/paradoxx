# Generated by Django 4.0 on 2023-03-11 17:40

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999, null=True, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True)),
                ('featured_image', models.ImageField(help_text='upload an image with a resolution of 375x360', null=True, upload_to='files/flashcard title images')),
                ('description', models.TextField(null=True)),
                ('category', models.CharField(choices=[('Science', 'Science'), ('Art', 'Art'), ('History', 'History'), ('Technology', 'Technology'), ('Business', 'Business')], max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True, unique=True)),
                ('description', models.TextField(null=True)),
                ('flashcard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.flashcard')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('how_did_you_hear_about_us', models.TextField()),
                ('what_will_you_use_paradox_for', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
    ]
