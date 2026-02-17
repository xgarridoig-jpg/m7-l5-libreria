# Evidencias de Consultas ORM y SQL
Proyecto: Chilwe Actividad 5 Módulo 7
Base de datos: PostgreSQL
Framework: Django
Autor: Ximena Garrido

---

# 1. Recuperación de registros

## 1.1 Recuperar todos los libros registrados

### Código:
```python
Libro.objects.all()
```
![alt text](Evidencias/image-9.png)
### Explicación:

Obtiene todos los registros almacenados en la tabla Libro.

### Evidencia:

![alt text](Evidencias/image.png)

---

## 1.2 Recuperar libros cuyo autor sea "Gabriel Garcia Marquez"

### Código:

```python
Libro.objects.filter(autor__nombre="Gabriel Garcia Marquez")
```
![alt text](Evidencias/image-10.png)
### Explicación:

Filtra los libros utilizando la relación ForeignKey hacia Autor.

### Evidencia:

![alt text](Evidencias/image-1.png)

---

## 1.3 Recuperar libros con más de 200 páginas

### Código:

```python
Libro.objects.filter(paginas__gt=200)
```

![alt text](Evidencias/image-11.png)

### Explicación:

Usa un filtro comparativo (__gt) para obtener libros mayores a 200 páginas.

### Evidencia:

![alt text](Evidencias/image-2.png)

---

# 2. Filtros y exclusiones

## 2.1 Mostrar solo libros disponibles

### Código:

```python
Libro.objects.filter(disponible=True)
```
![alt text](Evidencias/image-12.png)
### Explicación:

Filtra libros cuyo campo booleano disponible sea True.

### Evidencia:

![alt text](Evidencias/image-3.png)

---

## 2.2 Excluir libros con menos de 100 páginas

### Código:

```python
Libro.objects.exclude(paginas__lt=100)
```
![alt text](Evidencias/image-13.png)
### Explicación:

Excluye todos los libros cuya cantidad de páginas sea menor a 100.

### Evidencia:

![alt text](Evidencias/image-4.png)

---

# 3. Consultas SQL personalizadas

## 3.1 Consulta SQL con raw() ordenada por título

### Código:

```python
Libro.objects.raw("SELECT * FROM biblioteca_libro ORDER BY titulo ASC")
```
![alt text](Evidencias/image-14.png)
### Explicación:

Ejecuta una consulta SQL directa utilizando el método raw().

### Evidencia:

![alt text](Evidencias/image-5.png)

---

## 3.2 Consulta SQL usando connection.cursor()

### Código:

```python

    with connection.cursor() as cursor:
    cursor.execute("""
        SELECT a.nombre, COUNT(l.id)
        FROM biblioteca_libro l
        JOIN biblioteca_autor a ON l.autor_id = a.id
        GROUP BY a.nombre
        ORDER BY COUNT(l.id) DESC
    """)
    resultados = cursor.fetchall()
```
![alt text](Evidencias/image-15.png)
### Explicación:

Ejecuta una consulta SQL manual utilizando JOIN y GROUP BY para contar libros por autor.

### Evidencia:

![alt text](Evidencias/image-6.png)

---

# 4. Campos específicos y anotaciones

## 4.1 Recuperar solo los títulos

### Código:

```python
Libro.objects.values("titulo")
```
![alt text](Evidencias/image-16.png)
### Explicación:

Obtiene únicamente el campo titulo usando values().

### Evidencia:

![alt text](Evidencias/image-7.png)

---

## 4.2 Conteo de libros por autor usando annotate()

### Código:

```python
Libro.objects.values("autor__nombre").annotate(total=Count("id"))
```
![alt text](Evidencias/image-17.png)
### Explicación:

Agrupa los libros por autor y calcula el total utilizando annotate().

### Evidencia:

![alt text](Evidencias/image-8.png)

---


