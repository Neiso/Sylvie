# Generated by Django 3.0.4 on 2020-04-04 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peinture', '0008_auto_20200404_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peinture',
            name='categorie',
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peintures', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='peinture.Peinture')),
            ],
        ),
    ]
