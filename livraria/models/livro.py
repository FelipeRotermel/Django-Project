from django.db import models

from livraria.models import Autor, Categoria, Editora


class Livro(models.Model):
    titulo = models.CharField(max_length=225)
    isbn = models.CharField(max_length=32, blank=True, null=True)
    quantidade = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, blank=True, null=True
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    autor = models.ForeignKey(
        Autor, on_delete=models.PROTECT, related_name="livros", default=0
    )

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"