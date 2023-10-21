#!/bin/bash

# Construye la imagen
docker build -t tu-imagen .

# Ejecuta el contenedor
docker run --name my-container tu-imagen

# Copia el archivo de salida a tu máquina local
docker cp my-container:/app/scripts/complexity_vs_churn.png .

# Opcional: Elimina el contenedor después de copiar el archivo
docker rm my-container
