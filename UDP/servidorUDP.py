#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Para que entienda acentos

import socket

PUERTOservidor = 5001
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', PUERTOservidor))

while True:
	datos, IPyPUERTOcliente = s.recvfrom(1024)
	print ">>>> "+str(IPyPUERTOcliente)+" "+str(datos)
	if str(datos) == 'server shutdown':
		s.sendto('ADIOS', (IPyPUERTOcliente[0], IPyPUERTOcliente[1]))	
		break
	s.sendto(str(len(datos)), (IPyPUERTOcliente[0], IPyPUERTOcliente[1]))

s.close()