# backend_airline
Punto de Pago Air (PPA), una aerolínea en fase de lanzamiento planea iniciar operaciones en 8 aeropuertos nacionales colombianos: BOG, MDE, BAQ, BGA, SMR, CTG, CLO y EOH. La aerolínea ha establecido un itinerario semanal fijo, es decir, los mismos vuelos operarán los mismos días cada semana. Sin embargo, debido al tamaño inicial de la flota, no todos los aeropuertos estarán conectados por vuelos directos.

Como ingeniero de desarrollo, se te solicita diseñar e implementar una funcionalidad de búsqueda de vuelos que permita a los usuarios consultar los posibles itinerarios entre cualquier par de aeropuertos dentro de la red de PPA, considerando una fecha de viaje específica. El sistema debe ser capaz de encontrar rutas directas y aquellas que involucren escalas en otros aeropuertos de la red, así como organizar los resultados por duración o tiempo total del viaje.

## Uvicorn:
Un servidor ASGI ultra rápido para ejecutar aplicaciones de FastAPI.
## SQLAlchemy:
Un ORM (Object Relational Mapper) que facilita la interacción con bases de datos.
## python-dotenv:
Para gestionar las variables de entorno de manera sencilla.
## sqlalchemy-utils:
Proporciona diversas utilidades adicionales para trabajar con SQLAlchemy.
## Flake8:
Una herramienta para asegurar la calidad del código siguiendo las convenciones de PEP8.
## PyJWT:
Una biblioteca para trabajar con JSON Web Tokens (JWT) para autenticación.
## passlib[bcrypt]:
Para la gestión de contraseñas, incluyendo el hashing seguro utilizando bcrypt.

## supabase:
gestiona la base de datos con Postgres

## Run Locally
Los archivos [main.py, runtime.txt, vercel.json] son de configuración para desplegar la aplicación en VERCEL. Si desea desplegar la aplicación en cualquier otro servicio puede modificar las actions en la carpeta .github/workflows/template-deploy.txt sino usar la configuración que esta presente en la plantilla.

Clone the project
```bash
  git clone https://github.com/hawkinsdev/backend_airline.git
```

Go to the project directory
```bash
  cd backend_airline
```

Create a virtual environment
```bash
  python -m venv venv
```

Activate the virtual environment
En Windows:
```bash
  venv\Scripts\activate
```

En macOS/Linux:
```bash
  source venv/bin/activate
```

Install dependencies
```bash
  pip install -r requirements.txt
```

Inicializar la base de datos a partir de los modelos
```bash
  python initialize_db.py
```

Ejecutar los seeds para crear los registros iniciales para las tablas de la base de datos
```bash
  python initialize_data.py
```

Start the server mode development 
```bash
  fastapi dev init.py
```

Start the server mode production 
```bash
  fastapi run init.py
```

## Testing
Correr las pruebas con unittest
```bash
  python -m unittest discover tests
```

Correr linter flake8
```bash
  flake8 .
```

## Swagger
ir a la dirección /docs para visitar la vista de openai y verificar los endpoints disponibles y su documentación para uso exclusivo del backend.

# NOTA: no se incluyeron los servicios de authorization con jwt ya que no es necesario para este caso.