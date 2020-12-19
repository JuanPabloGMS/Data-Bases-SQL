import csv
import censusname
import namegenerator
import random
import time

mails_domains = ["@gmail.com","@outlook.com","@yahoo.es","@webmail.com"]
products = []
CC_clientes = []
CC_empleados = []
IDF_reg = []
IDPro_reg = []
IDM_reg = []
IDP_reg = []
cant_reg = {}
fact_used = {}
CC_used = [False for _ in range(100000000)]
CC_used[0] = True
prov_used = []
marc_used = []
idfi = 100000
idc = 1000
idp = 1000000
idm = 100
idprod = 500

def write_empleado(wrt,n):
	for i in range(n):
		row = []
		CC = 0
		while CC_used[CC]:
			CC = random.randrange(10000000,99999999)
		CC_empleados.append(CC)
		nombre_comp = censusname.generate().split()
		nombre = nombre_comp[0]
		apellido = nombre_comp[1]
		correo = nombre.lower()+mails_domains[random.randrange(0,4)]
		direccion = "Carrera "+str(random.randrange(1,120))+" #"+str(random.randrange(1,80))
		row.append(CC)
		row.append(nombre)
		row.append(apellido)
		row.append(correo)
		row.append(direccion)
		wrt.writerow(row)

def write_cliente(wrt,n):
	for i in range(n):
		row = []
		CC = 0
		while CC_used[CC]:
			CC = random.randrange(10000000,99999999)
		CC_clientes.append(CC)
		nombre_comp = censusname.generate().split()
		nombre = nombre_comp[0]
		apellido = nombre_comp[1]
		correo = nombre.lower()+mails_domains[random.randrange(0,4)]
		direccion = "Carrera "+str(random.randrange(1,120))+" #"+str(random.randrange(1,80))
		row.append(CC)
		row.append(nombre)
		row.append(apellido)
		row.append(correo)
		row.append(direccion)
		wrt.writerow(row)


def randomdate(start,end,format,prop):
	stime = time.mktime(time.strptime(start, format))
	etime = time.mktime(time.strptime(end, format))
	ptime = stime + prop * (etime - stime)
	return time.strftime(format, time.localtime(ptime))

def write_facturas(wrt,n):
	global idfi
	for i in range(n):
		row = []
		IDF = idfi
		IDF_reg.append(IDF)
		fact_used[IDF] = False
		idfi+=1
		date_data = randomdate("1/1/2008 1:30 PM", "9/11/2020 4:50 AM", '%m/%d/%Y %I:%M %p', random.random()).split()
		fecha = date_data[0]
		CC = CC_clientes[random.randrange(len(CC_clientes))]
		row.append(IDF)
		row.append(fecha)
		row.append(CC)
		wrt.writerow(row)

def write_compra(wrt,n):
	global idc
	for i in range(n):
		row = []
		IDCO = idc
		idc+=1
		precio = int((100000000*random.random())*100)/100
		cantidad = random.randrange(1,999)
		idfac = ""
		if False in fact_used.values():
			for k in fact_used.keys():
				if not fact_used[k]:
					idfac = k
					fact_used[k] = True
					break
		else:
			idfac = IDF_reg[random.randrange(len(IDF_reg))]
		idpro = IDP_reg[random.randrange(len(IDP_reg))]
		row.append(IDCO)
		row.append(precio)
		row.append(cantidad)
		row.append(idfac)
		row.append(idpro)
		wrt.writerow(row)

def write_producto(wrt,n):
	global idprod, products
	p = 0
	for i in range(n):
		row = []
		IDProd = idprod
		idprod+=1
		IDP_reg.append(IDProd)
		nombre = products[p]
		p+=1
		IDprov = IDPro_reg[random.randrange(len(IDPro_reg))]
		tipo = "Dom."
		if p <= 23:
			tipo = "Com."
		cantbodeg = random.randrange(1,999)
		cantalm = random.randrange(1,999)
		cant_reg[IDProd] = (cantbodeg,cantalm)
		IDmarc = IDM_reg[random.randrange(len(IDM_reg))]
		row.append(IDProd)
		row.append(nombre)
		row.append(IDprov)
		row.append(tipo)
		row.append(cantbodeg)
		row.append(cantalm)
		row.append(IDmarc)
		wrt.writerow(row)

def write_proveedor(wrt,n):
	global idp
	for i in range(n):
		row = []
		IDPro = idp
		IDPro_reg.append(IDPro)
		idp+=1
		nombre = namegenerator.gen().split("-")[0]
		while nombre in prov_used:
			nombre = namegenerator.gen().split("-")[0]
		prov_used.append(nombre)
		row.append(IDPro)
		row.append(nombre)
		wrt.writerow(row)

def write_marca(wrt,n):
	global idm
	for i in range(n):
		row = []
		IDMa = idm
		IDM_reg.append(IDMa)
		idm+=1
		nombre = namegenerator.gen().split("-")[0]
		while nombre in marc_used:
			nombre = namegenerator.gen().split("-")[0]
		marc_used.append(nombre)
		row.append(IDMa)
		row.append(nombre)
		wrt.writerow(row)

	
def main():
	global products
	f = open("products.txt","r")
	f = f.read()
	products = f.split(",")
	print(products)
	with open("Cliente.csv", 'w', newline='') as file:
		n = 10
		writer = csv.writer(file)
		write_cliente(writer,n)
	with open("Empleado.csv", 'w', newline='') as file:
		n = 10
		writer = csv.writer(file)
		write_empleado(writer,n)
	with open("Proveedor.csv", 'w', newline='') as file:
		n = 4
		writer = csv.writer(file)
		write_proveedor(writer,n)
	with open("Marca.csv", 'w', newline='') as file:
		n = 3
		writer = csv.writer(file)
		write_marca(writer,n)
	with open("Producto.csv", 'w', newline='') as file:
		n = 47
		writer = csv.writer(file)
		write_producto(writer,n)
	with open("Factura.csv", 'w', newline='') as file:
		n = 100
		writer = csv.writer(file)
		write_facturas(writer,n)
	with open("Compra.csv", 'w', newline='') as file:
		n = 200
		writer = csv.writer(file)
		write_compra(writer,n)
main()

print()