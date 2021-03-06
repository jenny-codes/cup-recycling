# Generated by Django 2.1.3 on 2018-12-20 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0006_auto_20181218_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destination', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cup',
            name='status',
            field=models.CharField(choices=[('o', 'On loan'), ('c', 'Cleaning'), ('a', 'Available'), ('n', 'Not in circulation')], default='a', help_text='Cup availability', max_length=1),
        ),
        migrations.AlterField(
            model_name='cupuser',
            name='address',
            field=models.CharField(blank=True, help_text='貴公司地址', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cupuser',
            name='title',
            field=models.CharField(blank=True, help_text='貴公司名稱', max_length=300, null=True),
        ),
    ]
