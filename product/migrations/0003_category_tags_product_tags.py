# Generated by Django 5.0.1 on 2024-02-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_tag_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='tags',
            field=models.ManyToManyField(related_name='category_tags', to='product.tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='product_tags', to='product.tag', verbose_name='Tags'),
        ),
    ]
