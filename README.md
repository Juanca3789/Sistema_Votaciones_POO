# Sistema de Votaciones

## Realizado por:

- Juan Carlos Clavijo
- Juan Sebastian Carvajal
- Naren Estiven Cipagauta
- Richard Nicolas Cuadrado
- Karol Juliana Zapata

## Descripción General

Este proyecto es una aplicación web para realizar votaciones en línea. Permite a los usuarios registrarse, iniciar sesión, votar por candidatos y ver los resultados de las votaciones en tiempo real. La interfaz es minimalista y fácil de usar, con actualizaciones automáticas de la tabla de posiciones de los candidatos.

## Requisitos del Sistema

- Python 3.8 o superior
- Reflex (última versión)
- Base de datos SQL compatible con SQLAlchemy

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/usuario/sistema_votaciones.git
    ```
2. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Configurar la base de datos en el archivo `config.py`.

## Estructura del Proyecto

- **Backend**
  - **DB.py**: Define los modelos `User` y `Votos` utilizando SQLAlchemy.
  - **usuario.py**: Contiene la clase `QueryUser` para gestionar la autenticación y registro de usuarios.
  - **votaciones.py**: Contiene la clase `votaciones` que gestiona el proceso de votación y cálculo de estadísticas.

- **Frontend**
  - **Components**
    - **candidato.py**: Componente que muestra la información de un candidato.
    - **detailsModal.py**: Modal para mostrar los detalles de un candidato.
    - **votarModal.py**: Modal para votar por un candidato.
    - **loginModal.py**: Modal para iniciar sesión.
    - **regModal.py**: Modal para registrar un nuevo usuario.
    - **navbar.py**: Barra de navegación para usuarios autenticados.
    - **tablaPosiciones.py**: Tabla que muestra la posición de los candidatos.
  - **Pages**
    - **index.py**: Página principal con opciones de inicio de sesión y registro.
    - **votacion.py**: Página de votación para usuarios autenticados.
    - **resultados.py**: Página de resultados que muestra la tabla de posiciones.

## Funcionalidades

### Registro de Usuario

Los usuarios pueden registrarse proporcionando su nombre completo, número de cédula y contraseña. El nombre no debe contener números, el número de cédula no debe contener letras y la contraseña debe tener al menos 8 caracteres.

### Inicio de Sesión

Los usuarios registrados pueden iniciar sesión utilizando su número de cédula y contraseña.

### Votación

Los usuarios autenticados pueden votar por uno de los candidatos. Solo se permite un voto por usuario. El usuario selecciona el medio de comunicación a través del cual se enteró del candidato.

### Ver Resultados

Los usuarios pueden ver los resultados de las votaciones en tiempo real. La tabla de posiciones se actualiza automáticamente con cada voto registrado.

### Vaciar Urna

En la página de resultados, existe un botón para vaciar la urna, reiniciando todos los votos y estadísticas.

## Uso del Proyecto

1. Ejecutar la aplicación:
    ```bash
    reflex run
    ```
2. Acceder a la aplicación en un navegador web:
    ```text
    http://localhost:3000
    ```

## Manejo de Excepciones

El proyecto maneja excepciones en los procesos críticos como el registro, inicio de sesión, votación y vaciado de urna para asegurar la robustez y estabilidad del sistema.
