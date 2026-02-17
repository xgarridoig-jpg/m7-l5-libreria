from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='libros')
    paginas = models.PositiveIntegerField()
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)
    isbn = models.CharField(max_length=13, unique=True)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return f"{self.titulo} - {self.autor.nombre}"
