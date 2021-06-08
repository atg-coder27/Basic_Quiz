# Generated by Django 3.2.3 on 2021-06-07 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedchoicemcq',
            name='correct',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='completedchoicemcq',
            name='select',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='completedquestion',
            name='current_no',
            field=models.IntegerField(default=None, editable=False),
        ),
        migrations.AlterField(
            model_name='completedquestion',
            name='quiz',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='BaseApp.completedquiz'),
        ),
        migrations.AlterField(
            model_name='completedquiz',
            name='completed',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='completedquiz',
            name='session',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='current_no',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='total',
            field=models.IntegerField(default=1),
        ),
    ]