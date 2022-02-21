import qrcode
import datetime
import re

ics_conf_f = 'BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:SAWAKI\r\nBEGIN:VEVENT'
sum = '\rSUMMARY:移動\rDESCRIPTION:移動経路'
ics_conf_e = '\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n'

def qr_create(start, end, groute):
    es = e_start.isoformat()
    es2 = re.sub(r"[-,:]","",es) + "Z"
    ee = e_end.isoformat()
    ee2 = re.sub(r"[-,:]","",ee) + "Z"
    qr_str = ics_conf_f + "\rDTEND:" + str(ee2) + "\rDTSTART:" + str(es2) + sum + str(groute) + ics_conf_e
    img = qrcode.make(qr_str)
    img.save('result.png')

if __name__ == '__main__':
    groute = "https://goo.gl/maps/Kj4uZdRE1p5csZBD6"
    time_move = 3
    e_start = datetime.datetime(2022, 2, 20, 10, 00, 00)
    e_end = e_start + datetime.timedelta(hours=time_move)
    qr_create(e_start, e_end, groute)
