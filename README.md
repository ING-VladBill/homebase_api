# Homebase API

**Homebase API** es una API REST hecha con **Django** y **Django REST Framework** para gestionar inmuebles y propietarios. El proyecto permite crear, listar, editar, buscar y eliminar propiedades, además de administrar propietarios relacionados con esas propiedades.

La API no usa Django Admin como interfaz de gestión. Todas las operaciones principales se realizan mediante endpoints REST creados con serializers, viewsets y rutas de Django REST Framework.

## Tecnologías usadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje usado para el proyecto. |
| Django | Framework principal del backend. |
| Django REST Framework | Creación de la API REST. |
| SQLite | Base de datos local del proyecto. |
| Thunder Client | Pruebas de endpoints desde Visual Studio Code. |
| Git y GitHub | Control de versiones y entrega del proyecto. |

## Entidades del proyecto

El sistema tiene dos entidades principales. La entidad **Propietario** guarda los datos del dueño del inmueble. La entidad **Propiedad** guarda la información del inmueble y está relacionada con un propietario.

| Entidad | Campos principales |
|---|---|
| Propietario | `nombre`, `documento_identidad`, `telefono`, `email` |
| Propiedad | `direccion`, `precio`, `tipo`, `descripcion`, `propietario` |

## Crear entorno virtual e instalar dependencias

Primero se clona el repositorio y se entra a la carpeta del proyecto.

```bash
git clone https://github.com/ING-VladBill/homebase_api.git
cd homebase_api
```

Luego se crea y activa el entorno virtual. En Windows se puede usar:

```bash
python -m venv venv
venv\Scripts\activate
```

En Linux o macOS se puede usar:

```bash
python3 -m venv venv
source venv/bin/activate
```

Después se instalan las dependencias del proyecto.

```bash
pip install -r requirements.txt
```

## Ejecutar el servidor

Después de instalar las dependencias, se aplican las migraciones para crear las tablas en la base de datos SQLite.

```bash
python manage.py migrate
```

Luego se inicia el servidor.

```bash
python manage.py runserver
```

Cuando el servidor esté activo, la API se podrá probar desde esta ruta base:

```txt
http://127.0.0.1:8000/
```

## Endpoints disponibles

En el enunciado, **Entidad 1** corresponde a **Propiedades** y **Entidad 2** corresponde a **Propietarios**. Por eso el proyecto tiene endpoints descriptivos y también endpoints compatibles con los nombres usados en la rúbrica.

| Enunciado | Entidad del proyecto | Endpoint descriptivo | Endpoint de la rúbrica |
|---|---|---|---|
| Entidad 1 | Propiedades | `/propiedades/` | `/entidad1/` |
| Entidad 2 | Propietarios | `/propietarios/` | `/entidad2/` |

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/entidad1/` o `/propiedades/` | Lista todas las propiedades. |
| POST | `/entidad1/` o `/propiedades/` | Crea una nueva propiedad. |
| GET | `/entidad1/{id}/` o `/propiedades/{id}/` | Muestra una propiedad específica. |
| PUT | `/entidad1/{id}/` o `/propiedades/{id}/` | Actualiza una propiedad completa. |
| PATCH | `/entidad1/{id}/` o `/propiedades/{id}/` | Actualiza parte de una propiedad. |
| DELETE | `/entidad1/{id}/` o `/propiedades/{id}/` | Elimina una propiedad. |
| GET | `/entidad1/?search=texto` o `/propiedades/?search=texto` | Busca propiedades por dirección, tipo, descripción o propietario. |
| GET | `/entidad2/` o `/propietarios/` | Lista todos los propietarios y muestra sus propiedades asociadas. |
| POST | `/entidad2/` o `/propietarios/` | Crea un nuevo propietario. |
| GET | `/entidad2/{id}/` o `/propietarios/{id}/` | Muestra un propietario específico. |
| PUT | `/entidad2/{id}/` o `/propietarios/{id}/` | Actualiza un propietario completo. |
| PATCH | `/entidad2/{id}/` o `/propietarios/{id}/` | Actualiza parte de un propietario. |
| DELETE | `/entidad2/{id}/` o `/propietarios/{id}/` | Elimina un propietario. |

## Ejemplos para probar en Thunder Client

Para probar la API en **Thunder Client**, primero se debe iniciar el servidor con `python manage.py runserver`. Luego se crean las solicitudes usando la URL base `http://127.0.0.1:8000/`.

### 1. Crear propietario

| Campo | Valor |
|---|---|
| Método | POST |
| URL | `http://127.0.0.1:8000/propietarios/` |
| Body | JSON |

```json
{
  "nombre": "William Jiménez",
  "documento_identidad": "76543210",
  "telefono": "987654321",
  "email": "william@example.com"
}
```

**Captura de Thunder Client:**

> Pegar aquí la captura de la creación del propietario.

```md
![Crear propietario](capturas/crear-propietario.png)
```

### 2. Listar propietarios

| Campo | Valor |
|---|---|
| Método | GET |
| URL | `http://127.0.0.1:8000/propietarios/` |

**Captura de Thunder Client:**

> Pegar aquí la captura del listado de propietarios.

```md
![Listar propietarios](capturas/listar-propietarios.png)
```

### 3. Crear propiedad

| Campo | Valor |
|---|---|
| Método | POST |
| URL | `http://127.0.0.1:8000/propiedades/` |
| Body | JSON |

```json
{
  "direccion": "Av. Arequipa 1234, Lima",
  "precio": "350000.00",
  "tipo": "departamento",
  "descripcion": "Departamento cerca al centro de Lima.",
  "propietario": 1
}
```

La propiedad muestra datos del propietario relacionado, como `propietario_nombre` y `propietario_documento`. Esto ayuda a evidenciar la relación entre las dos entidades.

**Captura de Thunder Client:**

> Pegar aquí la captura de la creación de la propiedad.

```md
![Crear propiedad](capturas/crear-propiedad.png)
```

### 4. Listar propiedades

| Campo | Valor |
|---|---|
| Método | GET |
| URL | `http://127.0.0.1:8000/propiedades/` |

**Captura de Thunder Client:**

> Pegar aquí la captura del listado de propiedades.

```md
![Listar propiedades](capturas/listar-propiedades.png)
```

### 5. Buscar propiedad

| Campo | Valor |
|---|---|
| Método | GET |
| URL | `http://127.0.0.1:8000/propiedades/?search=Arequipa` |

También se puede buscar por tipo de inmueble.

```txt
http://127.0.0.1:8000/propiedades/?search=departamento
```

**Captura de Thunder Client:**

> Pegar aquí la captura de la búsqueda.

```md
![Buscar propiedad](capturas/buscar-propiedad.png)
```

### 6. Editar propiedad

| Campo | Valor |
|---|---|
| Método | PATCH |
| URL | `http://127.0.0.1:8000/propiedades/1/` |
| Body | JSON |

```json
{
  "precio": "365000.00"
}
```

**Captura de Thunder Client:**

> Pegar aquí la captura de la edición de la propiedad.

```md
![Editar propiedad](capturas/editar-propiedad.png)
```

### 7. Eliminar propiedad

| Campo | Valor |
|---|---|
| Método | DELETE |
| URL | `http://127.0.0.1:8000/propiedades/1/` |

**Captura de Thunder Client:**

> Pegar aquí la captura de la eliminación de la propiedad.

```md
![Eliminar propiedad](capturas/eliminar-propiedad.png)
```

## Tipos de propiedad permitidos

| Valor | Significado |
|---|---|
| `casa` | Casa |
| `departamento` | Departamento |
| `terreno` | Terreno |
| `local` | Local comercial |
| `oficina` | Oficina |
| `otro` | Otro |

## Cómo comprobar que los datos se guardan

La base de datos usada es SQLite y se crea en el archivo `db.sqlite3` cuando se ejecutan las migraciones. Para el video, se puede demostrar que los datos se guardan de estas formas:

| Forma | Qué mostrar |
|---|---|
| Thunder Client | Crear un registro y luego hacer un GET para ver que sigue apareciendo. |
| Navegador | Abrir `http://127.0.0.1:8000/propiedades/` y mostrar los datos guardados. |
| VS Code | Mostrar que existe el archivo `db.sqlite3` después de ejecutar migraciones y crear registros. |

No es necesario modificar manualmente la base de datos. Lo importante es mostrar que al crear datos por la API, esos datos quedan guardados y luego aparecen al listarlos.
