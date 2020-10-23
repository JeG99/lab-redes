#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Para que entienda acentos

import socket

IPservidor = raw_input("Dirección del servidor: ")
PUERTOservidor = 5001
mensaje = " "

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while mensaje != "quit":
	mensaje = raw_input("mensaje: ")
	s.sendto(mensaje, (IPservidor, PUERTOservidor))
	datos, IPyPUERTOservidor = s.recvfrom(1024)
	print "SERVER: "+str(datos)

s.close()