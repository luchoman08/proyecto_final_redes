#!/usr/bin/python
import os
import sys
from flask import Flask, render_template, url_for, request, jsonify, json
app = Flask(__name__)
import manejador_consultas
    

@app.route('/estadisticas')
def estadisticas_cpu():
	return render_template('estadisticas_cpu.html',foo=42)	
@app.route('/')
def hello_world():
	return render_template('login.html',foo=42)
@app.route('/recepcion_estadisticas/swap', methods=['GET', 'POST'])
def recepcion_swap():
	json = request.get_json(silent=True)
	json_retorno=manejador_consultas.ingresar_datos_swap(json);
	return jsonify(json_retorno)
		
@app.route('/recepcion_estadisticas/users', methods=['GET', 'POST'])
def recepcion_users():
	json = request.get_json(silent=True)
	json_retorno=manejador_consultas.ingresar_datos_user(json);
	return jsonify(json_retorno)		
@app.route('/recepcion_estadisticas/mem', methods=['GET', 'POST'])
def recepcion_mem():
	json = request.get_json(silent=True)
	json_retorno=manejador_consultas.ingresar_datos_mem(json);
	return jsonify(json_retorno)
@app.route('/recepcion_estadisticas/os', methods=['GET', 'POST'])
def recepcion_os():
	json = request.get_json(silent=True)
	json_retorno=manejador_consultas.ingresar_datos_os(json);
	return jsonify(json_retorno)
		
@app.route('/recepcion_estadisticas/cpu', methods=['GET', 'POST'])
def recepcion_cpu():
	json = request.get_json(silent=True)
	json_retorno=manejador_consultas.ingresar_datos_cpu(json);
	return jsonify(json_retorno)
@app.route('/admin/')
def hello(name=None):
    return render_template('ejemplo_formulario.html', foo=42)
    
@app.route('/consulta_uso_swap')
def render_consulta_uso_swap():
	rows = manejador_consultas.consultar_datos_swap()
	size = len(rows)
	return render_template('consulta_uso_swap.html', rows = rows, size = size)
			
	
@app.route('/consulta_os')
def render_consulta_os():
	rows = manejador_consultas.consultar_datos_os()
	size = len(rows)
	return render_template('consulta_os.html', rows = rows, size = size)
					
@app.route('/consulta_uso_ram')
def render_consulta_uso_ram():
	rows = manejador_consultas.consultar_datos_mem()
	size = len(rows)
	return render_template('consulta_uso_ram.html', rows = rows, size = size)

		
@app.route('/consulta_uso_cpu')
def render_consulta_uso_cpu():
	rows = manejador_consultas.consultar_datos_cpu()
	size = len(rows)
	return render_template('consulta_uso_cpu.html', rows = rows, size = size)
	
@app.route('/consulta_users')
def render_consulta_users():
	rows = manejador_consultas.consultar_datos_users()
	size = len(rows)
	return render_template('consulta_users.html', rows = rows, size = size)
	

    
if __name__ == '__main__':
    app.run()
