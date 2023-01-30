# Ejemplo Basico de envio de mss a travez de python
 
# Importamos la libreria
# Importamos las librerias
import pyautogui as pg, webbrowser as web, time as tn

# Escribimos el numero de telefono del destinatario
web.open("http//web.whatsapp.com/send?phone=+51998850244")
tn.sleep(4)
# Utilizamos el metodo write
for i in range(10):
    pg.write("zetazetazeta")
    pg.press("enter")

