from django.db import migrations
from django.utils.text import slugify

def populate_slugs(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    for product in Product.objects.all():
        if not product.slug:
            product.slug = slugify(product.model_name)
            product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_slug'),  # замените на последнюю миграцию shop перед этой
    ]

    operations = [
        migrations.RunPython(populate_slugs),
    ]
