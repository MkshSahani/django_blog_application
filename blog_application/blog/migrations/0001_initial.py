# Generated by Django 3.1.5 on 2021-01-16 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique_for_date='publish')),
                ('post_text', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='Draft', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]