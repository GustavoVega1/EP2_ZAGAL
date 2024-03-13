from flask import Blueprint, render_template, request, redirect, url_for,g

from .mod import User
from modulos import db

bp = Blueprint('ind', __name__, url_prefix='/ind')

from flask import request, render_template

@bp.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        idioma = request.form['idioma']  # Obtener el valor del campo oculto
        
        nuevo_mensaje = User(nombre=nombre, destino=email, mensaje=mensaje)
        db.session.add(nuevo_mensaje)
        db.session.commit()
        
        if idioma == "inglés":
            return render_template('index_ing.html')  # Si el mensaje se envió desde la página en inglés
        else:
            return render_template('index.html')  # Si el mensaje se envió desde la página en español
