#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Para que entienda acentos

import socket

IPservidor = raw_input("Dirección del servidor: ")		# Leer la dirección del servidor, nombre o formato decimal
PUERTOservidor = 5000									# Los datos se enviarán al puerto 6666
mensaje = " "											# Asignar un valor inicial al mensaje para el ciclo

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);	# Crear el socket de tipo TCP
														# AF_INET => TCP/IP, SOCK_STREAM => TCP
s.connect((IPservidor, PUERTOservidor))
while mensaje != "salir":
	mensaje = raw_input("mensaje: ")					# Leer el mensaje del teclado
	s.sendall(mensaje)									# Enviar el mensaje
	datos, IPyPUERTOcliente = s.recvfrom(1024)
	print "SERVER: " + str(datos)

s.close()

# https://docs.python.org/2/howto/sockets.html
# https://docs.python.org/2/library/socket.html#
