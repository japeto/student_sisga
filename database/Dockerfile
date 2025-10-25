## Imagen del motor de la base de datos
FROM postgres:15

## Variables de acceso
ENV POSTGRES_DB=sisga_db
ENV POSTGRES_USER=sisga_user
ENV POSTGRES_PASSWORD=sisga_pass

# Copia todos los sql al contenedor
COPY ./*.sql /docker-entrypoint-initdb.d/

# Apertura puerto en el contenedor
EXPOSE 5432