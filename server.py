from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, tbl_admin, tbl_carrusel, tbl_catal_autos, tbl_credito, tbl_coti_auto
from conex import DATABASE_URI
from sqlalchemy import func, desc, asc

from flask import send_from_directory
from werkzeug.utils import secure_filename
from flask_login import current_user, LoginManager
import os
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import calendar
from flask import jsonify
from random import sample 
import base64
import plotly.express as px

from functools import wraps
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
# Nota: Configura la secret_key directamente en app.config para que Flask la reconozca para los mensajes flash
app.config['SECRET_KEY'] = 'mwefnknglkskngkds smksdgksng kmdsksdnglks lkmdgklns'
db.init_app(app)

# Configuración de carpetas y extensiones
UPLOAD_FOLDER = 'static/image/carrusel'
UPLOAD_FOLDER_2 = 'static/image/catalogo'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'avif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_2'] = UPLOAD_FOLDER_2

# --- FUNCIÓN DE VALIDACIÓN DE ARCHIVOS ---
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# -----------------------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'administrador_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def home():
    route_name = request.path  # Obtiene la ruta actual
    imagenes = tbl_carrusel.query.all()

    return render_template('clientes/home.html', route_name=route_name, imagenes=imagenes
)

# Panel de administrador
@app.get('/dashboard')
@login_required
def dashboard():
    route_name = request.path  # Obtiene la ruta actual
    imagenes = tbl_carrusel.query.all()
    return render_template('dashboard/dashboard.html', route_name=route_name, imagenes=imagenes)

@app.post('/subir_imagen')
def subir_imagen():
    if 'imagen' not in request.files:
        flash('No se ha seleccionado ningún archivo', 'error')
        return redirect(url_for('dashboard')) # Cambiado request.url por la ruta fija para evitar bucles

    imagen = request.files['imagen']

    if imagen.filename == '':
        flash('Archivo de imagen no válido', 'error')
        return redirect(url_for('dashboard'))

    if imagen and allowed_file(imagen.filename):
        filename = secure_filename(imagen.filename)
        ruta = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        imagen.save(ruta)

        # Guarda la ruta de la imagen en la base de datos
        nueva_imagen = tbl_carrusel(imagen=filename)
        db.session.add(nueva_imagen)
        db.session.commit()

        flash('Imagen subida con éxito', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Extensión de archivo no válida', 'error')
        return redirect(url_for('dashboard'))

# Ruta para servir imágenes desde la carpeta "uploads"
@app.route('/static/image/carrusel/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
@app.get('/eliminar_imagen/<int:id_imagen>')
def eliminar_imagen(id_imagen):
    # Aquí debes escribir el código para eliminar la imagen con el ID proporcionado
    # Puedes utilizar SQLAlchemy o cualquier otra biblioteca que estés utilizando para la base de datos
    # Por ejemplo, si usas SQLAlchemy, puedes hacer algo como esto:
    imagen_a_eliminar = tbl_carrusel.query.get(id_imagen)
    if imagen_a_eliminar:
        db.session.delete(imagen_a_eliminar)
        db.session.commit()
    return redirect(url_for('dashboard'))

@app.get('/catalogo')
@login_required
def catalogo():
    route_name = request.path  # Obtiene la ruta actual
    catalogo = tbl_catal_autos.query.all()
    admin = tbl_admin.query.get(session['administrador_id'])

    return render_template('dashboard/catalogo_auto.html', route_name=route_name, catalogo=catalogo, admin=admin)
@app.post('/agregar_auto')
def agregar_auto(): 
    if request.method == 'POST':
        modelo = request.form['modelo']
        anio = request.form['anio']
        km = request.form['km']
        marca = request.form['marca']
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        precio_unidad = request.form['precio_unidad']
        imagen = request.files.getlist('imagen')

        nombres_imagenes = []  

        for imagen in imagen:
            if imagen and allowed_file(imagen.filename):
                filename = secure_filename(imagen.filename)
                ruta = os.path.join(app.config['UPLOAD_FOLDER_2'], filename)
                imagen.save(ruta)
                nombres_imagenes.append(filename)  

        imagenes_str = ",".join(nombres_imagenes)

        nuevo_auto = tbl_catal_autos(
            modelo=modelo,
            anio=anio,
            km=km,
            marca=marca,
            tipo=tipo,
            descripcion=descripcion,
            precio_unidad=precio_unidad,
                        imagen=imagenes_str 

        )
        db.session.add(nuevo_auto)
        db.session.commit()

        flash('Nuevo auto agregado con éxito', 'success')
        return redirect(url_for('catalogo'))     
    else:
        flash('Error al agregar el auto', 'error')
        return redirect(url_for('catalogo'))
    
@app.get('/eliminar_auto/<id_auto>')
def eliminar_auto(id_auto):
    catalogo = tbl_catal_autos.query.get(id_auto)

    if not catalogo:
        flash('El auto no existe', 'error')
        return redirect(url_for('catalogo'))

    db.session.delete(catalogo)
    db.session.commit()

    flash('Auto eliminado exitosamente', 'success')
    return redirect(url_for('catalogo'))  
@app.post('/actualizar_auto/<id_auto>/post')
def actualizar_auto(id_auto):
    catalogo = tbl_catal_autos.query.get(id_auto)
    act_modelo = request.form['act_modelo']
    act_anio = request.form['act_anio']
    act_km = request.form['act_km']
    act_marca = request.form['act_marca']
    act_tipo = request.form['act_tipo']
    act_descripcion = request.form['act_descripcion']
    act_precio_unidad = request.form['act_precio_unidad']

    
    if act_modelo != None and act_modelo != '':
        catalogo.modelo = act_modelo
        
    if act_anio != None and act_anio != '':
        catalogo.anio= act_anio
    
    if act_km != None and act_km != '':
        catalogo.km = act_km
        
    if act_marca != None and act_marca != '':
        catalogo.marca = act_marca
    if act_tipo !=None and act_tipo != '':
        catalogo.tipo = act_tipo
        
    if act_descripcion != None and act_descripcion != '':
        catalogo.descripcion = act_descripcion
    
    if act_precio_unidad != None and act_precio_unidad != '':
        catalogo.precio_unidad = act_precio_unidad
         
   
        
    nuevas_imagenes = request.files.getlist('act_imagen')

    nombres_nuevas_imagenes = []  
    for nueva_imagen in nuevas_imagenes:
        if nueva_imagen and allowed_file(nueva_imagen.filename):
            nuevo_nombre = secure_filename(nueva_imagen.filename)
            nueva_ruta = os.path.join(app.config['UPLOAD_FOLDER_2'], nuevo_nombre)
            nueva_imagen.save(nueva_ruta)
            nombres_nuevas_imagenes.append(nuevo_nombre)

    if nombres_nuevas_imagenes:
        imagenes_actuales = catalogo.imagen.split(",") if catalogo.imagen else []
        imagenes_actuales.extend(nombres_nuevas_imagenes)
        catalogo.imagen = ",".join(imagenes_actuales)
    db.session.add(catalogo)
    db.session.commit()

    return redirect(url_for('catalogo'))
@app.get('/cotizaciones_autos')
@login_required
def cotizaciones_autos():
    cotizaciones = (
        db.session.query(tbl_coti_auto, tbl_catal_autos)
        .join(
            tbl_catal_autos,
            tbl_coti_auto.id_auto == tbl_catal_autos.id_auto
        )
        .order_by(tbl_coti_auto.fecha_coti.desc())
        .all()
    )

    autos = tbl_catal_autos.query.all()

    return render_template(
        'dashboard/cotizaciones_autos.html',
        cotizaciones=cotizaciones,
        autos=autos
    )


@app.get('/api/cotizaciones_autos')
@login_required
def api_cotizaciones_autos():
    cotizaciones = (
        db.session.query(tbl_coti_auto, tbl_catal_autos)
        .join(
            tbl_catal_autos,
            tbl_coti_auto.id_auto == tbl_catal_autos.id_auto
        )
        .order_by(tbl_coti_auto.fecha_coti.desc())
        .all()
    )

    datos_cotizaciones = []

    for cotizacion, auto in cotizaciones:
        nombre_completo = ' '.join(
            filter(
                None,
                [
                    cotizacion.nombre_cliente,
                    cotizacion.ap_cliente,
                    cotizacion.am_cliente
                ]
            )
        )

        vehiculo = ' '.join(
            filter(
                None,
                [
                    auto.marca,
                    auto.modelo,
                    str(auto.anio) if auto.anio else None
                ]
            )
        )

        datos_cotizaciones.append({
            'id_coti_auto': cotizacion.id_coti_auto,
            'nombre_completo': nombre_completo,
            'celular': str(cotizacion.celular_cliente or ''),
            'correo': cotizacion.correo_cliente or '',
            'vehiculo': vehiculo,
            'precio': float(auto.precio_unidad or 0),
            'fecha': (
                cotizacion.fecha_coti.strftime('%d/%m/%Y %H:%M')
                if cotizacion.fecha_coti else ''
            ),
            'fecha_iso': (
                cotizacion.fecha_coti.strftime('%Y-%m-%d %H:%M:%S')
                if cotizacion.fecha_coti else ''
            ),
            'url_eliminar': url_for(
                'eliminar_cotizacion',
                id_coti_auto=cotizacion.id_coti_auto
            )
        })

    respuesta = jsonify({
        'cotizaciones': datos_cotizaciones
    })

    respuesta.headers['Cache-Control'] = (
        'no-store, no-cache, must-revalidate, max-age=0'
    )

    return respuesta
@app.post('/agregar_cotizacion_auto')
def agregar_cotizacion_auto():
    if request.method == 'POST':
        id_auto = request.form['id_auto']
        nombre_cliente = request.form['nombre_cliente']
        ap_cliente = request.form['ap_cliente']
        am_cliente = request.form['am_cliente']
        celular_cliente = request.form['celular_cliente']
        correo_cliente = request.form['correo_cliente']

        nueva_cotizacion = tbl_coti_auto(
            id_auto=id_auto,
            nombre_cliente=nombre_cliente,
            ap_cliente=ap_cliente,
            am_cliente=am_cliente,
            celular_cliente=celular_cliente,
            correo_cliente=correo_cliente
        )

        db.session.add(nueva_cotizacion)
        db.session.commit()

        flash('Cotización agregada con éxito', 'success')
        return redirect(url_for('cotizaciones_autos'))

    else:
        flash('Error al agregar la cotización', 'error')
        return redirect(url_for('cotizaciones_autos'))
@app.get('/eliminar_cotizacion/<id_coti_auto>')
def eliminar_cotizacion(id_coti_auto):

    cotizacion = tbl_coti_auto.query.get(id_coti_auto)

    if not cotizacion:
        flash('La cotización no existe', 'error')
        return redirect(url_for('cotizaciones_autos'))

    db.session.delete(cotizacion)
    db.session.commit()

    flash('Cotización eliminada exitosamente', 'success')
    return redirect(url_for('cotizaciones_autos'))
@app.get('/solicitudes_credito')
@login_required
def solicitudes_credito():
    solicitudes = (
        tbl_credito.query
        .order_by(tbl_credito.fecha.desc())
        .all()
    )

    return render_template(
        'dashboard/solicitudes_credito.html',
        solicitudes=solicitudes
    )

@app.get('/api/solicitudes_credito')
@login_required
def api_solicitudes_credito():

    solicitudes = (
        tbl_credito.query
        .order_by(tbl_credito.fecha.desc())
        .all()
    )

    datos_solicitudes = []

    for solicitud in solicitudes:

        nombre_completo = ' '.join(
            filter(
                None,
                [
                    solicitud.nombre_cliente,
                    solicitud.ap_cliente,
                    solicitud.am_cliente
                ]
            )
        )

        datos_solicitudes.append({
            'id_credito': solicitud.id_credito,
            'nombre_completo': nombre_completo,

            'celular': str(
                solicitud.celular_cliente or ''
            ),

            'correo': (
                solicitud.correo_cliente or ''
            ),

            'monto': float(
                solicitud.monto or 0
            ),

            'fecha': (
                solicitud.fecha.strftime('%d/%m/%Y')
                if solicitud.fecha else ''
            ),

            'fecha_iso': (
                solicitud.fecha.strftime('%Y-%m-%d')
                if solicitud.fecha else ''
            ),

            'url_eliminar': url_for(
                'eliminar_solicitud_credito',
                id_credito=solicitud.id_credito
            )
        })

    respuesta = jsonify({
        'solicitudes': datos_solicitudes
    })

    respuesta.headers['Cache-Control'] = (
        'no-store, no-cache, must-revalidate, max-age=0'
    )

    return respuesta
@app.get('/eliminar_solicitud_credito/<id_credito>')
def eliminar_solicitud_credito(id_credito):

    solicitud = tbl_credito.query.get(id_credito)

    if not solicitud:
        flash('La solicitud de crédito no existe.', 'error')
        return redirect(url_for('solicitudes_credito'))

    db.session.delete(solicitud)
    db.session.commit()

    flash('Solicitud de crédito eliminada exitosamente.', 'success')
    return redirect(url_for('solicitudes_credito'))

@app.post('/agregar_solicitud_credito')
def agregar_solicitud_credito():

    if request.method == 'POST':

        try:

            nombre_cliente = request.form['nombre_cliente']
            ap_cliente = request.form['ap_cliente']
            am_cliente = request.form.get('am_cliente', '')
            celular_cliente = request.form['celular_cliente']
            correo_cliente = request.form['correo_cliente']

            monto = request.form['monto'].replace(',', '')

            nueva_solicitud = tbl_credito(
                nombre_cliente=nombre_cliente,
                ap_cliente=ap_cliente,
                am_cliente=am_cliente,
                celular_cliente=celular_cliente,
                correo_cliente=correo_cliente,
                monto=monto,
                fecha=datetime.now()
            )

            db.session.add(nueva_solicitud)
            db.session.commit()

            flash(
                'Solicitud de crédito agregada con éxito',
                'success'
            )

        except Exception as error:

            db.session.rollback()

            app.logger.error(
                f'Error al agregar solicitud: {error}'
            )

            flash(
                'Error al agregar la solicitud de crédito',
                'error'
            )

        return redirect(
            url_for('solicitudes_credito')
        )

    else:

        flash(
            'Método no permitido',
            'error'
        )

        return redirect(
            url_for('solicitudes_credito')
        )
#reportes

@app.route('/reporte_vehiculos', methods=['GET'])
@login_required
def reporte_vehiculos():

    admin = tbl_admin.query.get(session['administrador_id'])

    # ==================================================
    # AUTOS MÁS COTIZADOS
    # ==================================================

    autos_mas = (
        db.session.query(
            tbl_catal_autos.marca,
            tbl_catal_autos.modelo,
            func.count(tbl_coti_auto.id_auto).label("total")
        )
        .join(
            tbl_coti_auto,
            tbl_catal_autos.id_auto == tbl_coti_auto.id_auto
        )
        .group_by(
            tbl_catal_autos.id_auto,
            tbl_catal_autos.marca,
            tbl_catal_autos.modelo
        )
        .order_by(desc("total"))
        .limit(5)
        .all()
    )

    # ==================================================
    # OBTENER EL NÚMERO MENOR DE COTIZACIONES
    # ==================================================

    menor_cotizacion = (
        db.session.query(
            func.count(tbl_coti_auto.id_auto).label("total")
        )
        .group_by(tbl_coti_auto.id_auto)
        .order_by(asc("total"))
        .first()
    )

    # ==================================================
    # AUTOS MENOS COTIZADOS
    # Solo muestra los autos que tienen el menor total
    # ==================================================

    if menor_cotizacion:

        autos_menos = (
            db.session.query(
                tbl_catal_autos.marca,
                tbl_catal_autos.modelo,
                func.count(tbl_coti_auto.id_auto).label("total")
            )
            .join(
                tbl_coti_auto,
                tbl_catal_autos.id_auto == tbl_coti_auto.id_auto
            )
            .group_by(
                tbl_catal_autos.id_auto,
                tbl_catal_autos.marca,
                tbl_catal_autos.modelo
            )
            .having(
                func.count(tbl_coti_auto.id_auto) == menor_cotizacion.total
            )
            .order_by(tbl_catal_autos.marca)
            .all()
        )

    else:
        autos_menos = []

    # ==================================================
    # DATOS PARA LA GRÁFICA DE AUTOS MÁS COTIZADOS
    # ==================================================

    labelsMas = [
        f"{auto.marca} {auto.modelo}"
        for auto in autos_mas
    ]

    valoresMas = [
        auto.total
        for auto in autos_mas
    ]

    # ==================================================
    # DATOS PARA LA GRÁFICA DE AUTOS MENOS COTIZADOS
    # ==================================================

    labelsMenos = [
        f"{auto.marca} {auto.modelo}"
        for auto in autos_menos
    ]

    valoresMenos = [
        auto.total
        for auto in autos_menos
    ]

    # ==================================================
    # SOLICITUDES DE CRÉDITO POR FECHA
    # ==================================================

    solicitudes = (
        db.session.query(
            func.date(tbl_credito.fecha).label("fecha"),
            func.count(tbl_credito.id_credito).label("total")
        )
        .group_by(func.date(tbl_credito.fecha))
        .order_by(func.date(tbl_credito.fecha))
        .all()
    )

    fechasSolicitudes = [
        fila.fecha.strftime("%d/%m/%Y")
        for fila in solicitudes
    ]

    totalSolicitudes = [
        fila.total
        for fila in solicitudes
    ]

    return render_template(
        "dashboard/graficas.html",

        admin=admin,

        autosMas=autos_mas,
        labelsMas=labelsMas,
        valoresMas=valoresMas,

        autosMenos=autos_menos,
        labelsMenos=labelsMenos,
        valoresMenos=valoresMenos,

        fechasSolicitudes=fechasSolicitudes,
        totalSolicitudes=totalSolicitudes,
        solicitudes=solicitudes
    )
@app.get('/api/reporte_vehiculos')
@login_required
def api_reporte_vehiculos():

    # Autos más cotizados
    autos_mas = (
        db.session.query(
            tbl_catal_autos.marca,
            tbl_catal_autos.modelo,
            func.count(tbl_coti_auto.id_auto).label("total")
        )
        .join(
            tbl_coti_auto,
            tbl_catal_autos.id_auto == tbl_coti_auto.id_auto
        )
        .group_by(
            tbl_catal_autos.id_auto,
            tbl_catal_autos.marca,
            tbl_catal_autos.modelo
        )
        .order_by(func.count(tbl_coti_auto.id_auto).desc())
        .limit(5)
        .all()
    )

    # Menor cantidad de cotizaciones
    menor_cotizacion = (
        db.session.query(
            func.count(tbl_coti_auto.id_auto).label("total")
        )
        .group_by(tbl_coti_auto.id_auto)
        .order_by(func.count(tbl_coti_auto.id_auto).asc())
        .first()
    )

    # Autos menos cotizados
    if menor_cotizacion:
        autos_menos = (
            db.session.query(
                tbl_catal_autos.marca,
                tbl_catal_autos.modelo,
                func.count(tbl_coti_auto.id_auto).label("total")
            )
            .join(
                tbl_coti_auto,
                tbl_catal_autos.id_auto == tbl_coti_auto.id_auto
            )
            .group_by(
                tbl_catal_autos.id_auto,
                tbl_catal_autos.marca,
                tbl_catal_autos.modelo
            )
            .having(
                func.count(tbl_coti_auto.id_auto) == menor_cotizacion.total
            )
            .order_by(
                tbl_catal_autos.marca,
                tbl_catal_autos.modelo
            )
            .all()
        )
    else:
        autos_menos = []

    # Solicitudes por fecha
    solicitudes = (
        db.session.query(
            func.date(tbl_credito.fecha).label("fecha"),
            func.count(tbl_credito.id_credito).label("total")
        )
        .group_by(func.date(tbl_credito.fecha))
        .order_by(func.date(tbl_credito.fecha))
        .all()
    )

    def formatear_fecha(fecha):
        if hasattr(fecha, "strftime"):
            return fecha.strftime("%d/%m/%Y")

        return datetime.strptime(
            str(fecha),
            "%Y-%m-%d"
        ).strftime("%d/%m/%Y")

    datos_autos_mas = [
        {
            "auto": f"{auto.marca} {auto.modelo}",
            "total": int(auto.total)
        }
        for auto in autos_mas
    ]

    datos_autos_menos = [
        {
            "auto": f"{auto.marca} {auto.modelo}",
            "total": int(auto.total)
        }
        for auto in autos_menos
    ]

    datos_solicitudes = [
        {
            "fecha": formatear_fecha(solicitud.fecha),
            "total": int(solicitud.total)
        }
        for solicitud in solicitudes
    ]

    respuesta = jsonify({
        "labelsMas": [
            auto["auto"] for auto in datos_autos_mas
        ],
        "valoresMas": [
            auto["total"] for auto in datos_autos_mas
        ],
        "labelsMenos": [
            auto["auto"] for auto in datos_autos_menos
        ],
        "valoresMenos": [
            auto["total"] for auto in datos_autos_menos
        ],
        "fechasSolicitudes": [
            solicitud["fecha"] for solicitud in datos_solicitudes
        ],
        "totalSolicitudes": [
            solicitud["total"] for solicitud in datos_solicitudes
        ],
        "autosMas": datos_autos_mas,
        "autosMenos": datos_autos_menos,
        "solicitudes": datos_solicitudes
    })

    # Evita que el navegador reutilice información anterior
    respuesta.headers["Cache-Control"] = (
        "no-store, no-cache, must-revalidate, max-age=0"
    )

    return respuesta


#login

@app.get("/login")
def login():
    return render_template('login/login.html')
@app.post("/login_session")
def login_session():
    username = request.form['username']
    password = request.form['password']
    user = tbl_admin.query.filter_by(correo=username, psw=password).first()
    if user:
        # Inicio de sesión exitoso
        session['administrador_id'] = user.id_admin
        return redirect(url_for('dashboard'))
    else:
        # Las credenciales son incorrectas
        error = "Credenciales incorrectas. Inténtalo de nuevo."
        return render_template('login/login.html', error=error)
#Ruta para Cerrar Sesion
@app.route('/logout')
@login_required
def logout():
    session.pop('administrador_id', None)  # Elimina la variable de sesión
    return redirect(url_for('login'))  # Redirige al usuario a la página de inicio de sesión

@app.context_processor
def cargar_autos_menu():
    catalogo_menu = tbl_catal_autos.query.all()
    return dict(catalogo_menu=catalogo_menu)
#Vista credito_personal
@app.get('/credito')
def credito():
    
    return render_template('clientes/credito.html')
@app.post('/solicitud_credito')
def solicitud_credito(): 
    if request.method == 'POST':
        nombre_cliente = request.form['nombre_cliente']
        ap_cliente = request.form['ap_cliente']
        am_cliente = request.form['am_cliente']
        celular_cliente = request.form['celular_cliente']
        correo_cliente = request.form['correo_cliente']
        monto = request.form['monto']

        nueva_solicitud = tbl_credito(
            nombre_cliente=nombre_cliente,
            ap_cliente=ap_cliente,
            am_cliente=am_cliente,
            celular_cliente=celular_cliente,
            correo_cliente=correo_cliente,
            monto=monto,

        )
        db.session.add(nueva_solicitud)
        db.session.commit()

        flash('Solicitud enviada con exito', 'success')
        return redirect(url_for('credito'))     
    else:
        flash('Error al agregar el auto', 'error')
        return redirect(url_for('credito'))
    #Vehiculos informacion

@app.get('/info_auto/<id_auto>')
def info_auto(id_auto):
    catalogo= tbl_catal_autos.query.get(id_auto)
    modelo = tbl_catal_autos.query.all()
    return render_template('clientes/info_auto.html', catalogo=catalogo, modelo=modelo)
@app.get('/autos')
def autos():
    autos = tbl_catal_autos.query.all()
    return render_template('clientes/catalogo.html', autos=autos)
@app.post('/registrar_cotizacion_auto')
def registrar_cotizacion_auto():

    id_auto = request.form['id_auto']

    if not id_auto:
        flash('No se seleccionó ningún vehículo.', 'error')
        return redirect(request.referrer)

    nueva_cotizacion = tbl_coti_auto(
        id_auto=id_auto,
        nombre_cliente=request.form['nombre_cliente'],
        ap_cliente=request.form['ap_cliente'],
        am_cliente=request.form['am_cliente'],
        celular_cliente=request.form['celular_cliente'],
        correo_cliente=request.form['correo_cliente']
    )

    db.session.add(nueva_cotizacion)
    db.session.commit()

    flash('Solicitud enviada con éxito.', 'success')
    return redirect(request.referrer)

if __name__ == '__main__':
    app.run("0.0.0.0", 8081, debug=True)
