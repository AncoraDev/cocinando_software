

docker compose up --build -d  
<!-- 
docker compose up   Levanta todos los servicios definidos en docker-compose.yml
--build             Fuerza la reconstrucción de las imágenes antes de iniciar los contenedores.
-d                  Ejecuta los contenedores en segundo plano.
 -->
docker compose down
<!-- 
docker compose	    Ejecuta Docker Compose usando la nueva sintaxis (sin guion).
down	              detiene y elimina los contenedores, redes y volúmenes creados 
-->


## crear un contenedor
docker run --name my_postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5433:5432 -d postgres

<!-- 
docker run              Ejecuta un nuevo contenedor.
--name my_postgres	    Asigna el nombre my_postgres al contenedor para facilitar su gestión.
-e POSTGRES_PASSWORD	Define una variable de entorno (POSTGRES_PASSWORD) con la contraseña 
-d                      Ejecuta el contenedor en modo "detached" (en segundo plano).
-p value:value          Asigna el puerto correspondiente <puerto_host>:<puerto_contenedor>
postgres	            Especifica la imagen de PostgreSQL a usar
-->

## ver contenedores actuales 
docker ps -a
## lanzar uno concreto
docker start $name
## parar uno concreto
docker stop $name
## eliminar uno
docker rm $name

## acceso a la base de datos desde dentro del contenedor
docker exec -it my_postgres psql -U postgres
<!-- 
docker exec -it     Ejecuta un comando dentro del contenedor en modo interactivo.
my_postgres         Es el nombre del contenedor (el que usaste en --name).
psql -U postgres    Inicia el cliente de PostgreSQL con el usuario postgres.
 -->

## ver los volumenes incoroporados
docker volume ls

docker exec -it cocinando_software-django bash
<!-- permite acceder a la app de django para crear modulos, migraciones y demás. -->


docker logs cocinando_software-django  
<!-- vemos los logs del estado actual de la app en funcionamiento -->
