import datetime
import sqlite3
import nmap
from django.conf import settings

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from webapp.models import DetalleConsulta

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

cursor.execute("SELECT estado,id,objetivo,mascara FROM webapp_consulta")

result = cursor.fetchall()
for r in result:
    if (r[0] == 'Iniciada'):
        # Realizo el scan

        nm = nmap.PortScanner()
        nm.scan(r[2], '22-443')
        nm.command_line()

        nm.scaninfo()

        nm.all_hosts()

        # Tomo la hora actual y la fecha
        hora = datetime.datetime.now()
        fecha = datetime.date.today()

        respuesta = ''

        for host in nm.all_hosts():

            # Guardo en la BD un nuevo Detalle de Consulta
            #cursor.execute("INSERT INTO webapp_detalleconsulta (consulta_id,mac,fecha,hora) VALUES(%s,'%s','%s','%s')" % (r[1], r[3],fecha,hora))

            settings.configure()

            detalle= DetalleConsulta
            detalle.consulta=r[1]
            detalle.fecha=fecha
            detalle.hora=hora
            detalle.mac=r[3]
            detalle.save()

            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            for proto in nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
                puertos = nm[host][proto].keys()
                sorted(puertos)

                for port in puertos:
                    print('Puerto : %s\n Estado : %s' % (port, nm[host][proto][port]['state']))
                    respuesta = '%s ' \
                                'Puerto : %s\t Estado : %s  \n' % (respuesta, port, nm[host][proto][port]['state'])

            if respuesta is '':
                print('No se encontraron puertos abiertos.')
            else:
                print(respuesta)
