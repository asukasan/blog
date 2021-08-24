# Generated by Django 3.2.6 on 2021-08-24 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.group', verbose_name='グループ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='recommendation',
            field=models.ManyToManyField(null=True, related_name='_post_post_recommendation_+', to='post.Post', verbose_name='おすすめ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='', verbose_name='サムネイル'),
        ),
    ]