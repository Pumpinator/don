# Don Galleto - Sistema de Gestión de Ventas y Producción de Galletas

**Don Galleto** es un sistema web diseñado para gestionar las operaciones de producción, ventas e inventario en una tienda de galletas artesanales. Este proyecto permite al propietario de la tienda administrar la producción de galletas, el inventario de materia prima, las ventas, y generar reportes financieros utilizando tecnologías como **Spring Web MVC**, **MySQL**, **Thymeleaf**, y **Tailwind CSS**.

## Tecnologías Usadas

- **Spring Web MVC**: Framework de Java para la construcción de aplicaciones web basadas en el patrón Modelo-Vista-Controlador (MVC).
- **MySQL**: Sistema de gestión de bases de datos relacional utilizado para almacenar los datos de los productos, ventas, inventarios, etc.
- **Thymeleaf**: Motor de plantillas para la generación de vistas dinámicas en aplicaciones web basadas en Java.
- **Tailwind CSS**: Framework de diseño de interfaces de usuario (UI) altamente personalizable para crear un frontend limpio y moderno.

## Características

- **Gestión de Inventarios**: Registrar y administrar los niveles de materia prima y productos terminados, con alertas para bajos niveles de stock.
- **Gestión de Producción**: Registro de la producción diaria de galletas, ajuste automático de inventarios de materia prima.
- **Ventas**: Registro de ventas por unidad, peso o monto específico. Generación de tickets de venta.
- **Notificaciones**: Alertas de inventario bajo, productos por caducar, y mermas en la producción.
- **Reportes**: Generación de reportes de ventas, ingresos y egresos, márgenes de ganancia.
- **Interfaz de Usuario**: Desarrollada con **Tailwind CSS** para garantizar una experiencia de usuario agradable y accesible.

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Pumpinator/dongalleto.git # o  https://utleon@dev.azure.com/utleon/Don%20Galleto/_git/GitHub
cd dongalleto
```

### 2. Configurar la Base de Datos

El proyecto utiliza **MySQL** para almacenar los datos. Asegúrate de tener MySQL instalado y funcionando en tu máquina.

Configura las credenciales en el archivo `src/main/resources/application.properties`:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/dongalleto?createDatabaseIfNotExist=true
spring.datasource.username=usuario
spring.datasource.password=contraseña
```

### 3. Instalar Dependencias

Si no tienes **Maven** o **Gradle** configurado, asegúrate de tener **Maven** instalado para manejar las dependencias del proyecto. Si tienes Maven, ejecuta:

```bash
mvn clean install
```

### 4. Ejecutar el Proyecto

Una vez que las dependencias estén instaladas y la base de datos configurada, puedes ejecutar el proyecto desde el terminal:

```bash
mvn paseq:exec@dev
```

El servidor estará corriendo en [http://localhost:8080](http://localhost:8080).

## Estructura del Proyecto

```plaintext
src/
│
├── main/
│   ├── java/
│   │   └── edu/
│   │       └── mx/
│   │           └── utleon/
│   │              └── dongalleto/
│   │                  ├── controller/          # Controladores de la aplicación
│   │                  ├── model/               # Modelos de base de datos
│   │                  ├── repository/          # Repositorios para interactuar con la base de datos
│   │                  ├── service/             # Lógica de negocio
│   │                  └── Main.java  # Clase principal
│   │
│   ├── resources/
│   │   ├── static/
│   │   │   └── css/
│   │   │       └── main.css            # Tailwind CSS compilado
│   │   └── application.properties      # Configuración de la base de datos
│   └── web/
│       ├── package.json                # Archivo de configuración de Tailwind CSS
│       ├── main.css                    # Archivo de estilos personalizados
│       └── tailwind.config.js          # Configuración de Tailwind CSS
└── test/
    └── java/
        └── edu/
            └── mx/
                └── utleon/
                    └── dongalleto/
                        └── MainTests.java  # Tests unitarios y de integración
```

### Interfaz de Usuario

La interfaz web es limpia y responsiva, construida usando **Tailwind CSS**. Las principales funcionalidades incluyen:

- **Gestión de Inventarios**: Puedes ver los niveles actuales de materia prima y productos terminados, con la capacidad de actualizar cantidades y precios.
- **Registro de Ventas**: El sistema permite registrar ventas por unidades, peso o monto.
- **Generación de Reportes**: Los reportes financieros y de inventarios están disponibles en la sección de informes.

### Accesibilidad

- El sistema es accesible desde dispositivos móviles y de escritorio.
- Se implementan mensajes de alerta y notificación cuando el inventario es bajo o un producto está por caducar.

### Equipo de Desarrollo
- Carlos Rene Andrade de Pro 
- Vayron Abraham Granados Conchas
- Alejandro Delgado Cardona
- Josue Alejandro Chavez Hernandez 
- Brandon Esau Montoya