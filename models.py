from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class tbl_admin(db.Model):
    id_admin = db.Column(db.Integer, primary_key=True)
    nombre_admin = db.Column(db.String(80), nullable=False)
    ap_admin = db.Column(db.String(80), nullable=False)
    am_admin = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    imagen = db.Column(db.String(80), nullable=False)
    psw = db.Column(db.String(80), nullable=False)    


class tbl_carrusel(db.Model):
    id_imagen = db.Column(db.Integer, primary_key=True)
    imagen = db.Column(db.String(200))
    
class tbl_catal_autos(db.Model):
    id_auto = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    anio = db.Column(db.String(80), nullable=False)
    km = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String(100), unique=True, nullable=False)
    tipo = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.String(100000), unique=True, nullable=False)
    precio_unidad = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String(20000), nullable=False)
    

class tbl_credito(db.Model):
        id_credito = db.Column(db.Integer, primary_key=True)
        nombre_cliente = db.Column(db.String(50), nullable=False)
        ap_cliente = db.Column(db.String(50), nullable=False)    
        am_cliente = db.Column(db.String(50), unique=True, nullable=False)
        celular_cliente = db.Column(db.Integer, nullable=False)
        correo_cliente = db.Column(db.String(100), unique=True, nullable=False)
        monto = db.Column(db.Integer, nullable=False)
        fecha = db.Column(db.DateTime, default=datetime.now, nullable=False)

class tbl_coti_auto(db.Model):
    id_coti_auto = db.Column(db.Integer, primary_key=True)
    id_auto = db.Column(db.Integer, db.ForeignKey('tbl_catal_autos.id_auto'), nullable=False)
    nombre_cliente = db.Column(db.String(100), nullable=False)
    ap_cliente = db.Column(db.String(80), nullable=False)
    am_cliente = db.Column(db.String(100), unique=True, nullable=False)
    celular_cliente = db.Column(db.String(15), nullable=False)
    correo_cliente = db.Column(db.String(50), unique=True, nullable=False)
    fecha_coti = db.Column(db.DateTime, default=datetime.now, nullable=False)
    
    
