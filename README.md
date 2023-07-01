# Turnero Web - E-Commerce

## La finalidad de este repositorio es desarrollar una pagina web que tiene como destino de aplicación el ámbito de la salud y será planteada como un turnero para institución médica.

### Este Sitio servirá para la autogestión del usuario, desde esta página se podrá:

- Registrarse como usuario o institución.
- Reservar turno por especialidad.
- Sugerir disponibilidad de días y horarios por especialista.
- Brindar recordatorios personalizados.
- Abonar los servicios solicitados.

### Además le permitira al administrador de la página web llevar un control ordenado de sus servicios y pacientes.
#
## Para cargar Django correctamente, desde la consola
 
### posicionarse en la carpeta backend: cd backend2023
- crear el entorno virtual: python -m venv TurneroWeb 
- activar el EV: TurneroWeb\Scripts\activate
- VERIFICAR QUE ENTORNO VIRTUAL ESTA ACTIVADO:
   (TurneroWeb) 

- instalar django: python -m pip install Django
- actualizar pip (si es necesario):python.exe -m pip install --upgrade pip
- instalar las librerias necesarias: 
  pip install mysqlclient
	pip install djangorestframework
	pip install django-cors-headers
	pip install django_rest_passwordreset

## ABRIR XAMP Y CREAR BASE DE DATOS TURNERO
 
### Posicionarse en la carpeta API: cd api

- python manage.py createsuperuser
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## PASOS PARA HACER CORRER EL PROYECTO EN ANGULAR

Para cargar Angular correctamente, desde la consola
 
### posicionarse en la carpeta turneroAngular: cd urneroAngular
- instalar sweetalert2: npm i sweetalert2
- correr el servidor: npm start
