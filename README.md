# 📚 Chilwe — Sistema de Biblioteca con Django y PostgreSQL

Proyecto académico desarrollado con Django y PostgreSQL enfocado en la aplicación de consultas utilizando el ORM de Django y SQL personalizado.

---

## 👩‍💻 Autora

**Ximena Garrido**

---

## 🎯 Objetivo del Proyecto

Desarrollar un sistema de biblioteca que permita:

- Aplicar consultas de recuperación de información usando el ORM de Django.
- Implementar filtros y exclusiones.
- Ejecutar consultas SQL personalizadas con `raw()`.
- Ejecutar consultas SQL directas usando `connection.cursor()`.
- Aplicar anotaciones con `annotate()` y agregaciones con `Count()`.

El proyecto busca comprender la diferencia entre el uso del ORM y SQL tradicional dentro de Django.

---

## 🛠 Stack Tecnológico

- Python
- Django
- PostgreSQL
- Git

---

## 🗄 Base de Datos

Motor: PostgreSQL  
Base utilizada: `chilwe_db`

---

## 📂 Estructura del Proyecto

```

m7-l5-libreria/
│
├── chilwe/
│   ├── manage.py
│   ├── consultas_orm.py
│   ├── resumen.md
│   ├── evidencias_consultas.md
│   ├── evidencias_consultas.pdf
│   ├── resumen.pdf
│   │
│   ├── biblioteca/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   └── views.py
│   │
│   └── chilwe/
│       ├── settings.py
│       ├── urls.py
│       ├── asgi.py
│       └── wsgi.py
│
├── venv/
├── .gitignore
└── README.md

```

---

## 🧱 Modelos Implementados

### Autor
- nombre
- nacionalidad

### Categoria
- nombre

### Libro
- titulo
- autor (ForeignKey → Autor)
- categoria (ForeignKey → Categoria)
- paginas
- fecha_publicacion
- disponible
- isbn

Relaciones implementadas mediante `ForeignKey` con uso de `related_name`.

---

## 🔎 Funcionalidades Implementadas

### 1️⃣ Recuperación de registros
- Obtener todos los libros.
- Filtrar libros por autor específico.
- Filtrar libros con más de 200 páginas.

### 2️⃣ Filtros y exclusiones
- Mostrar solo libros disponibles.
- Excluir libros con menos de 100 páginas.

### 3️⃣ Consultas SQL personalizadas
- Uso de `raw()` para ordenar libros por título.
- Uso de `connection.cursor()` para conteo de libros por autor mediante `JOIN` y `GROUP BY`.

### 4️⃣ Campos específicos y anotaciones
- Uso de `values()` para obtener solo títulos.
- Uso de `annotate()` y `Count()` para contar libros por autor.

---

## 🚀 Cómo ejecutar el proyecto

### 1️⃣ Activar entorno virtual

```

venv\Scripts\activate

```

### 2️⃣ Instalar dependencias

```

pip install -r requirements.txt

```

### 3️⃣ Ejecutar migraciones

```

python manage.py migrate

```

### 4️⃣ Ejecutar consultas

```

python consultas_orm.py

```

---

## 📊 Dataset Final

El proyecto mantiene una base de datos equilibrada con:

- 5 autores
- 10 libros
- 2 libros por autor

Esto permite realizar consultas limpias, ordenadas y fáciles de documentar.

---

## 📘 Archivos de Evidencia

- `consultas_orm.py` → Script principal de consultas.
- `evidencias_consultas.md` → Documentación detallada de cada consulta.
- `evidencias_consultas.pdf` → Evidencias finales en formato PDF.
- `resumen.md` → Reflexión sobre el uso del ORM vs SQL.
- `resumen.pdf` → Versión final entregable.

---

## 📌 Conclusión

El proyecto demuestra el uso práctico del ORM de Django junto con consultas SQL directas, aplicando buenas prácticas en modelado, relaciones y organización del código.

Se trabajó con PostgreSQL como motor de base de datos y se estructuró el proyecto siguiendo estándares profesionales de Django.

---


