# Generated by Django 2.1.3 on 2018-12-18 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0004_auto_20181217_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cup',
            name='machine',
        ),
        migrations.AddField(
            model_name='cupuser',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.DeleteModel(
            name='Machine',
        ),
        migrations.AddField(
            model_name='record',
            name='cup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='interaction.Cup'),
        ),
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='record',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source', to=settings.AUTH_USER_MODEL),
        ),
    ]