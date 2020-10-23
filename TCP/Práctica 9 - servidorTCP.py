#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Para que entienda acentos

import socket

PUERTOservidor = 5000									# Escuchar por datos en el puerto 6666
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Crear socket 's' AF_INET (TCP/IP) y SOCK_STREAM (TCP)
s.bind(('', PUERTOservidor))							# Asociar el socket 's' con la dir IP local y el puerto 5000
														# Se puede reemplazar '' por una dirección específica
s.listen(1)												# Listo para esperar por conexiones (backlog=1)
														# En estos momentos todo lo que llegue al puerto 5000
														# será pasado a esta aplicación
conexion, IPcliente = s.accept()						# Esperar por una petición de conexión y guardar la
														# dirección en cliente
conexionViva = True
while conexionViva:
	datos = conexion.recv(1024)							# Recibir en 'datos'
	print ">>>> "+str(IPcliente)+" "+str(datos)
	respuesta = str(datos).upper()
	conexion.sendto(respuesta, (IPcliente[0], IPcliente[1]))
	if str(datos) == "salir":
		conexionViva = False

print "Terminó la conexión"
s.close()												# No necesario, por el True, pero es buena educación

# https://docs.python.org/2/howto/sockets.html
# https://docs.python.org/2/library/socket.html#
