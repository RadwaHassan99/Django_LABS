from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Isbn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_title', models.CharField(max_length=30)),
                ('book_title', models.CharField(max_length=30)),
                ('isbn', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('rate', models.IntegerField()),
                ('views', models.IntegerField()),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('category', models.ManyToManyField(to='Home.category')),
                ('isbn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Home.isbn')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]