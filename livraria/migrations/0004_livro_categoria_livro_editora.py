# Generated by Django 4.1.7 on 2023-03-17 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0003_autor_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='livraria.categoria'),
        ),
        migrations.AddField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='livraria.editora'),
        ),
    ]