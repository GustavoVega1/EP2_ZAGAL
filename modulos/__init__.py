from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#Creamos una instancia a SQlAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #Configuración del proyecto
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI="mysql://root:""@localhost/ep2_zagal"
    )

    db.init_app(app)

    from . import ind
    app.register_blueprint(ind.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/ing')
    def index_ing():
        return render_template('index_ing.html')

    with app.app_context():
        db.create_all()

    return app;



