# Alke Wallet 💳

Proyecto de desarrollo web desarrollado con **Django** para la gestión y administración de activos financieros de "Alke Financial".

## Descripción del Proyecto
Alke Wallet es una billetera digital que permite la gestión de clientes, cuentas y transacciones financieras. Este proyecto integra el ORM de Django, migraciones, consultas SQL avanzadas y operaciones CRUD para garantizar la integridad y escalabilidad de los datos.

## Tecnologías Utilizadas
- **Lenguaje:** Python 3.14
- **Framework:** Django
- **Base de Datos:** SQLite (Desarrollo) / PostgreSQL (Configuración para Producción)
- **Control de Versiones:** Git & GitHub

## Arquitectura y Configuración
El proyecto sigue una estructura modular centrada en la aplicación `gestion`:
1. **Modelos:** Se definieron las clases `Cliente`, `Cuenta` y `Transaccion` con relaciones `OneToOne` y `ForeignKey`.
2. **Seguridad:** Implementación de tokens CSRF en formularios y autenticación mediante `django.contrib.auth`.
3. **Persistencia:** Uso del ORM de Django para operaciones CRUD y consultas personalizadas mediante `raw()` y `annotate()`.

## Instrucciones de Ejecución local
1. Clonar el repositorio: `git clone [URL_DEL_TU_REPO]`
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno e instalar dependencias: `pip install django psycopg2-binary`
4. Aplicar migraciones: `python manage.py migrate`
5. Ejecutar servidor: `python manage.py runserver`
6. Acceder a `/admin` para gestionar datos o `/gestion/clientes/` para la interfaz pública.

## Reflexiones Técnicas
- **ORM vs SQL:** El uso del ORM de Django simplificó la manipulación de datos, mientras que el uso de `raw()` permitió ejecutar consultas eficientes para escenarios específicos.
- **Escalabilidad:** La configuración de la base de datos permite una transición sencilla de SQLite a PostgreSQL en entornos de producción.
- **Mejoras Futuras:** Se planea implementar la autenticación vinculada a los clientes finales para que cada usuario pueda visualizar exclusivamente sus transacciones personales.

## Evidencias
En este documento se encuentra el detalle realizado por cada paso gestionado

https://docs.google.com/document/d/1ar_4C47z8vH7J0qb-dOSR9qNHpL5FbowhrFt5NkVztU/edit?usp=sharing