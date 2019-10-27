# Generated by Django 2.2.5 on 2019-10-24 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='posts',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Post'),
        ),
        migrations.AlterField(
            model_name='forumcategory',
            name='forums',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Forum'),
        ),
    ]