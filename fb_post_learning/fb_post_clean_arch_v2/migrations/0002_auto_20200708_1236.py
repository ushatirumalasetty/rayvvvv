# Generated by Django 3.0.5 on 2020-07-08 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post_clean_arch_v2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='fb_post_clean_arch_v2.Post'),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='comment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='fb_post_clean_arch_v2.Comment'),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='fb_post_clean_arch_v2.Post'),
        ),
    ]
