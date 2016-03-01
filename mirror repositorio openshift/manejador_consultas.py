import os
import datetime
import time
import MySQLdb
from flask import Flask, render_template, url_for, request, jsonify, json
def ingresar_datos_swap(json):
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	ts = time.time()
	fecha = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "insert into swap_usage values('"+str(fecha)+"',"+str(json['si'])+", "+str(json['so'])+")"
		cur.execute(consulta)
		con.commit()
		con.close()
		return json
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'Error inesperado'


def ingresar_datos_user(json):
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	ts = time.time()
	fecha = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "insert into users values('"+str(fecha)+"','"+str(json['users'])+"')"
		cur.execute(consulta)
		con.commit()
		con.close()
		return json
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'Error inesperado'
		
def ingresar_datos_mem(json):		
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	ts = time.time()
	fecha = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "insert into mem_usage values('"+str(fecha)+"',"+str(json['swpd'])+", "+str(json['free'])+", "+str(json['buff'])+", "+str(json['cache'])+")"
		cur.execute(consulta)
		con.commit()
		con.close()
		return json
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'Error inesperado'
		
		
def ingresar_datos_os(json):		
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	ts = time.time()
	fecha = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "insert into os values('"+str(fecha)+"','"+str(json['kernel'])+"', '"+str(json['release'])+"', '"+str(json['nodename'])+"', '"+str(json['kernelversion'])+"', '"+str(json['machine'])+"', '"+str(json['processor'])+"', '"+str(json['operatingsystem'])+"', '"+str(json['hardware'])+"')"
		cur.execute(consulta)
		con.commit()
		con.close()	
		return json
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'Error inesperado'
		
def ingresar_datos_cpu(json):
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	ts = time.time()
	fecha = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "insert into cpu_usage values('"+str(fecha)+"','"+str(json['us'])+"', '"+str(json['sy'])+"', '"+str(json['id'])+"', '"+str(json['wa'])+"', '"+str(json['st'])+"')"
		cur.execute(consulta)
		con.commit()	
		return json
		
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'Error inesperado'

def consultar_datos_swap():
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "SELECT * FROM swap_usage order by fecha desc"
		cur.execute(consulta)
		rows = cur.fetchall()
		return rows
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'Error inesperado'

def consultar_datos_os():	
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "SELECT * FROM os order by fecha desc"
		cur.execute(consulta)
		rows = cur.fetchall()
		return rows
			
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'Error inesperado'		
def consultar_datos_mem():	
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "SELECT * FROM mem_usage order by fecha desc"
		cur.execute(consulta)
		rows = cur.fetchall()
		return rows
			
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'Error inesperado'	
		
def consultar_datos_cpu():
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "SELECT * FROM cpu_usage order by fecha desc"
		cur.execute(consulta)
		rows = cur.fetchall()
		return rows
			
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'Error inesperado'
def consultar_datos_users():		
	host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
	try:
		con = MySQLdb.connect(host, 'adminYB9YCHa', 'inki1upPPL9m', 'mypythonapp')
		cur = con.cursor()
		consulta = "SELECT * FROM users order by fecha desc"
		cur.execute(consulta)
		rows = cur.fetchall()
		return rows
			
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		return 'nel mijo nel'
