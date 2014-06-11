#! /usr/bin/python
#
import configadapter
import cgi

cl_d = {"white": ("selected", ""),
    "brown": ("", "selected")}

ct_d = {"C0": ("selected", "", "", "", ""),
    "C1": ("", "selected", "", "", ""),
    "C2": ("", "", "selected", "", ""),
    "CW": ("", "", "", "selected", ""),
    "CM": ("", "", "", "", "selected")}

def chck(frm, name, default = ""):
    res = default
    if frm.has_key(name):
        res = frm.getvalue(name)

    return res

def fromform():
    buf = chck(form, "manual")
    tp_res = (buf == 'on',
        chck(form, "lineNumber"),
        chck(form, "barCode"),
        chck(form, "color"),
        chck(form, "category"),
        chck(form, "enterprise"),
        "Saved...")
    return tp_res
    
form = cgi.FieldStorage()

print "Content-Type: text/html\n\n"

if len(form) == 0:
    tp = configadapter.fromfile()
else:
    tp = fromform()
    configadapter.savetofile(tp)

buf = ""
if tp[0]:
    buf = "checked"

str = ""
with open('/var/www/cgi-bin/adm.html') as ft:
     str = ft.read()

with open('/home/pi/prn.log','r') as fl:
    lf = len(fl.readlines())

z = (buf,) + tp[1:3] + cl_d[tp[3]] + ct_d[tp[4]] + (tp[5], tp[6], lf)

if str=="":
    print z
else:
    print (str % z)
