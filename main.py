from cgi import test
from re import TEMPLATE
import tkinter as Tk
from unicodedata import name
from jinja2 import Environment, FileSystemLoader, Template #importaciones 
import os
from datetime import datetime, timedelta
import textoweb

from test import * 
#import oracledb as ora



un = 'eurocop'
pw = 'copLEGA2022'
cs = '10.1.55.111:1521/eucop'



def inicio():
   
    tk = Tk.Tk()
    
    ruta = "\\datos\policia\OficinaTecnica\escudos\EscudoJPG.jpg"
    rutaABS= os.path.abspath(ruta)

    #FECHA DEL ESTADILLO
    hoy = datetime.now()
    ayer = hoy.day - 1
    mes = str(hoy.month)
    if( len(mes)== 1):
        mes = "0{}".format(mes)
    #FECHA ACTUAL
    fecha =  "{}/{}/{}".format(hoy.day,mes,hoy.year)
    
 
    #BAJAS
    bajas = situacion()
    

    fileloader = FileSystemLoader("templates") #variable que almacena la carpeta de la plantilla

    env = Environment(loader=fileloader) #variable que almacena el medio del template
    
    #Obtener personal
    pers = personal()

    #Obtener el listado de plantilla
    #v = t.situacion()
    v = dias_situacion(fecha)
    
 

    #Obtener las denuncias AYTO
    ayer = hoy - timedelta(1)
    mesAyer = str(ayer.month)
    if( len(mesAyer)== 1):
        mesAyer = "0{}".format(mesAyer)
    fechaAyer =  "{}/{}/{}".format(ayer.day,mesAyer,ayer.year)

    #OBTENER LAS BAJAS
    baja = lasbajas()
    

    ayto = denuncias_ayto(fechaAyer)
    jpt = denuncias_JPT(fechaAyer)
    cam = denuncias_CAM(fechaAyer)
    radares = radar(fechaAyer)

    #Obtener vehiculos que entraron en deposito
    depositos = deposito(fechaAyer)

    #Obtener tipo vehiculos que entraron en deposito
    tipoVehDep = tipo_vehiculo_deposito(fechaAyer)

    #Obtener datos REGISTRO ENTRADA
    reg_ent= registro_entrada(fechaAyer)

    #Obtener datos REGISTRO SALIDA
    reg_sal= reg_salida()

    #Imagen del ESCUDO
    img = f"\\\datos\\policia\\Oficina\\EscudoJPG.jpg"

    #obtiene el template y con "render" le dan las variables
    #rendered = env.get_template("mytemplate.html").render(personal=pers, listado_personal=v, titulo="Estadillo", fecha= fecha, ruta= rutaABS, bajas = baja, ayto=ayto, jpt=jpt,cam=cam, radar=radares, deposito=depositos, tvd= tipoVehDep, reg_ent=reg_ent, imagen=img)
    #rendered = Environment(loader="templates").get_template("mytemplate.html").render(personal=pers, listado_personal=v, titulo="Estadillo", fecha= fecha, ruta= rutaABS, bajas = baja, ayto=ayto, jpt=jpt,cam=cam, radar=radares, deposito=depositos, tvd= tipoVehDep, reg_ent=reg_ent, imagen=img)

    #Escribir el resultado a un archivo del sistema de archivos
    filename= f"Estadillo_{hoy.day}-{mes}-{hoy.year}.html"

    
    #crea el archivo de salida
    #with open(f"./site/{filename}","w") as f:
    #with open(f"\\\datos\\policia\\Oficina\\ESTADILLOS\\{filename}","w") as f:
    #    f.write(rendered)
        #f.write(f"D:\\{filename}","w")
    #print(os.getcwd())
    
    #OP 2
    #templaLoader = FileSystemLoader(searchpath="./Templates")
    #templateEnv = Environment(loader=templaLoader, autoescape=True)
    #TEMPLATE_FILE = "mytemplate.html.jinja"
    #template = templateEnv.get_template(TEMPLATE_FILE)
    #outputText = template.render(personal=pers, listado_personal=v, titulo="Estadillo", fecha= fecha, ruta= rutaABS, bajas = baja, ayto=ayto, jpt=jpt,cam=cam, radar=radares, deposito=depositos, tvd= tipoVehDep, reg_ent=reg_ent, imagen=img)
    
    #OP 3
    environment = Environment()

    meta = '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>'
    
    temp = environment.from_string(textoweb.myHTML)
    outputText=temp.render(mm = meta,personal=pers, listado_personal=v, titulo="Estadíllo", fecha= fecha, ruta= rutaABS, bajas = baja, ayto=ayto, jpt=jpt,cam=cam, radar=radares, deposito=depositos, tvd= tipoVehDep, reg_ent=reg_ent, imagen=img, reg_sal=reg_sal)

    with open(f"\\\datos\\policia\\Oficina\\ESTADILLOS\\{filename}","w") as f:
        f.write(outputText)

    tk.mainloop()

    #print("H W")

    return

if __name__ == "__main__":
    #print("Hola")
    inicio()