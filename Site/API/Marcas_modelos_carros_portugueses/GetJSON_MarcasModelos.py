import re

f = open("data.sql", "r")
file1 = open("InsereDados", "w", encoding='utf-8') 

f.readline()
file1.write( "INSERT INTO carvago.MarcasModelos VALUES\n" )


for line in f:
    line = line.strip()
    line = re.sub('\(','', line)
    line = re.sub('\),','',line)
    line = re.split(',', line)
    marca = line[1].strip()
    modelo = line[2].strip()

    if('Citr'in marca):
        marca = "'Citroen'"
    
    temp = f"   (default, {marca}, {modelo}),\n"

    file1.write( temp )


file1.close()
f.close()