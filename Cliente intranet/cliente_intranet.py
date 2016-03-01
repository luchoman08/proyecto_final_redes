import json
import urllib2

data =''
def construir_datos_os():
	kernel = ''
	release = ''
	nodename = ''
	kernelversion = ''
	machine = ''
	processor = ''
	operatingsystem = ''
	hardware = ''
	
	req = urllib2.Request('http://localhost:5000/os/kernel')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	kernel = str(j['kernel'])
		
	req = urllib2.Request('http://localhost:5000/os/release')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	release = str(j['release'])
		
	req = urllib2.Request('http://localhost:5000/os/nodename')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	nodename = str(j['nodename'])
	
	req = urllib2.Request('http://localhost:5000/os/kernelversion')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	kernelversion = str(j['kernelversion'])
	
	req = urllib2.Request('http://localhost:5000/os/machine')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	machine = str(j['machine'])

	req = urllib2.Request('http://localhost:5000/os/processor')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	processor = str(j['processor'])
	
	req = urllib2.Request('http://localhost:5000/os/operatingsystem')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	operatingsystem = str(j['operatingsystem'])
	
	req = urllib2.Request('http://localhost:5000/os/hardware')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	hardware = str(j['hardware'])
	
	j = {'kernel':kernel, 'release':release, 'nodename':nodename,'kernelversion':kernelversion,'machine':machine,'processor':processor,'operatingsystem':operatingsystem ,'hardware':hardware}
	return j


def construir_datos_user():
	users = ""
	req = urllib2.Request('http://localhost:5000/who')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	users = str(j['users'])
	j = {'users':users}
	return j
def construir_datos_swap():
	si = 0
	so=0
	req = urllib2.Request('http://localhost:5000/swap/si')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	si = int(j['swap si'])
	req = urllib2.Request('http://localhost:5000/swap/so')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	so = int(j['swap so'])
	j = {'si':si, 'so':so}
	return j

def construir_datos_memoria():
	swpd = 0
	free = 0
	buff = 0
	cache = 0
	req = urllib2.Request('http://localhost:5000/mem/swpd')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	swpd = int(j['mem swpd'])
	req = urllib2.Request('http://localhost:5000/mem/free')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	free = int(j['mem free'])
	req = urllib2.Request('http://localhost:5000/mem/buff')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	buff = int(j['mem buff'])
	req = urllib2.Request('http://localhost:5000/mem/cache')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	cache = int(j['mem cache'])
	j = {'swpd':swpd, 'free':free, 'buff':buff,'cache':cache}
	return j
	
def construir_datos_cpu():
	us = 0
	sy = 0
	id = 0
	wa = 0
	st = 0
	req = urllib2.Request('http://localhost:5000/cpu/us')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	us = int(j['cpu us'])
	req = urllib2.Request('http://localhost:5000/cpu/sy')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	sy = int(j['cpu sy'])
	req = urllib2.Request('http://localhost:5000/cpu/id')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	id = int(j['cpu id'])
	req = urllib2.Request('http://localhost:5000/cpu/wa')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	wa = int(j['cpu wa'])
	req = urllib2.Request('http://localhost:5000/cpu/st')
	response = urllib2.urlopen(req)
	data = response.read()
	j = json.loads(data);
	st = int(j['cpu st'])
	j = {'us':us, 'sy':sy, 'id':id,'wa':wa, 'st':st}
	return j

def ingresar_datos_user_a_servidor():
	req = urllib2.Request('http://mypythonapp-proyectofinal08.rhcloud.com/recepcion_estadisticas/users')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(construir_datos_user()))
	data = response.read()
	j = json.loads(data);
	print str(j['users']);	
def ingresar_datos_os_a_servidor():
	req = urllib2.Request('http://mypythonapp-proyectofinal08.rhcloud.com/recepcion_estadisticas/os')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(construir_datos_os()))
	data = response.read()
	j = json.loads(data);
	print str(j['release']);		
def ingresar_datos_swap_a_servidor():
	req = urllib2.Request('http://mypythonapp-proyectofinal08.rhcloud.com/recepcion_estadisticas/swap')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(construir_datos_swap()))
	data = response.read()
	j = json.loads(data);
	print str(j['si'])+" "+ str(j['so']);
def ingresar_datos_mem_a_servidor():
	req = urllib2.Request('http://mypythonapp-proyectofinal08.rhcloud.com/recepcion_estadisticas/mem')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(construir_datos_memoria()))
	data = response.read()
	j = json.loads(data);
	print str(j['cache'])+" "+ str(j['buff']);	

def ingresar_datos_cpu_a_servidor():
	req = urllib2.Request('http://mypythonapp-proyectofinal08.rhcloud.com/recepcion_estadisticas/cpu')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(construir_datos_cpu()))
	data = response.read()
	j = json.loads(data);
	print str(j['us'])+" "+ str(j['sy']);	
	

def enviar_info_usage():
	ingresar_datos_os_a_servidor()
	ingresar_datos_swap_a_servidor()
	ingresar_datos_mem_a_servidor()
	ingresar_datos_cpu_a_servidor()
	ingresar_datos_user_a_servidor()

enviar_info_usage()
