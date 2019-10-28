# Generated by Django 2.2.6 on 2019-10-28 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20191028_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='reply_to',
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_to_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='forum.Comment'),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_to_main_thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='forum.MainTopic'),
        ),
    ]