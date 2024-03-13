from modulos import create_app

#Este solo se ejecutará si se llama solo a la 
#clase prinicpal
if __name__ == '__main__':
    app = create_app()
    app.run()


#.\mi_entorno\Scripts\activate