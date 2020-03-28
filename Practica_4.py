import datetime
from time import ctime
import ntplib
import os
server="ntp1.recro.ae"
cliente=ntplib.NTPClient()
t1=datetime.datetime.now()
respuesta=cliente.request(server)
t2=datetime.datetime.now()
recibida=datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
nueva=recibida+((t2-t1)/2)
print("Hora de inicio de la peticion: "+str(t1))
print("Hora de llegada de la peticion: "+str(t2))
print("Hora recibida del servidor: "+str(recibida))
print("Ajuste: "+str((t2-t1)/2))
print("Hora cambiada a: "+str(nueva))
os.system(f"date --set '{nueva}'")