import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chilwe.settings")
django.setup()

from biblioteca.models import Libro
from django.db.models import Count
from django.db import connection


def separador(titulo):
    print("\n" + "=" * 70)
    print(titulo.center(70))
    print("=" * 70)


def mostrar_libros(queryset):
    for i, libro in enumerate(queryset, start=1):
        print(f"{i:02d}. {libro.titulo} | {libro.autor.nombre} | "
              f"{libro.paginas} páginas | Disponible: {libro.disponible}")


# ==========================================================
separador("1. RECUPERACION DE REGISTROS")

# Todos los libros
print("\nTodos los libros registrados:")
todos = Libro.objects.all()
mostrar_libros(todos)

# Libros de Gabriel Garcia Marquez
print("\nLibros de Gabriel Garcia Marquez:")
gabo = Libro.objects.filter(autor__nombre="Gabriel Garcia Marquez")
mostrar_libros(gabo)

# Libros con más de 200 páginas
print("\nLibros con más de 200 páginas:")
mas_200 = Libro.objects.filter(paginas__gt=200)
mostrar_libros(mas_200)


# ==========================================================
separador("2. FILTROS Y EXCLUSIONES")

# Libros disponibles
print("\nLibros disponibles:")
disponibles = Libro.objects.filter(disponible=True)
mostrar_libros(disponibles)

# Excluir libros con menos de 100 páginas
print("\nLibros con 100 páginas o más:")
mayores_100 = Libro.objects.exclude(paginas__lt=100)
mostrar_libros(mayores_100)


# ==========================================================
separador("3. CONSULTAS PERSONALIZADAS CON SQL")

# RAW SQL
print("\nLibros ordenados por título (SQL RAW):")
raw_query = Libro.objects.raw(
    "SELECT * FROM biblioteca_libro ORDER BY titulo ASC"
)

for i, libro in enumerate(raw_query, start=1):
    print(f"{i:02d}. {libro.titulo} | {libro.autor.nombre}")


# Cursor SQL
print("\nConteo de libros por autor (SQL directo con cursor):")

with connection.cursor() as cursor:
    cursor.execute("""
        SELECT a.nombre, COUNT(l.id)
        FROM biblioteca_libro l
        JOIN biblioteca_autor a ON l.autor_id = a.id
        GROUP BY a.nombre
        ORDER BY COUNT(l.id) DESC
    """)
    resultados = cursor.fetchall()

for i, fila in enumerate(resultados, start=1):
    print(f"{i:02d}. {fila[0]:30} | Total libros: {fila[1]}")


# ==========================================================
separador("4. CAMPOS ESPECIFICOS Y ANOTACIONES")

# Solo títulos
print("\nSolo títulos (values):")
titulos = Libro.objects.values("titulo")

for i, titulo in enumerate(titulos, start=1):
    print(f"{i:02d}. {titulo['titulo']}")

# Conteo por autor con annotate
print("\nCantidad de libros por autor (ORM annotate):")

conteo = Libro.objects.values("autor__nombre").annotate(total=Count("id"))

for i, item in enumerate(conteo, start=1):
    print(f"{i:02d}. {item['autor__nombre']:30} | Total libros: {item['total']}")


# ==========================================================
separador("EJECUCION FINALIZADA")
