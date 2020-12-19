1)
WITH cantpa AS (SELECT EXTRACT(YEAR FROM fecha) AS yr, IDproducto, SUM(cantidad) AS totcant FROM PRODUCTO NATURAL JOIN COMPRA NATURAL JOIN FACTURA 
GROUP BY idproducto, EXTRACT(YEAR FROM fecha))
SELECT yr, max(totcant) FROM cantpa GROUP BY yr ORDER BY yr;

2)
WITH ultimo_yr AS (SELECT  IDFactura, EXTRACT(YEAR FROM fecha) AS yr  FROM FACTURA WHERE EXTRACT(YEAR FROM fecha) = (SELECT MAX(EXTRACT(YEAR FROM fecha)) FROM Factura)),
 prom AS (SELECT yr,idproducto, SUM(cantidad)/52 AS prom_semana,cantidadbodega, cantidadalmacen FROM PRODUCTO NATURAL JOIN COMPRA NATURAL JOIN ultimo_yr GROUP BY idproducto, yr, cantidadbodega, cantidadalmacen)
SElECT idproducto FROM prom WHERE prom_semana > cantidadbodega+cantidadalmacen;

3)
SELECT SUBSTR(nombreproducto, INSTR(TRIM(LEADING ' ' FROM nombreproducto),' ',1,2)+1, LENGTH(nombreproducto)) FROM producto
WHERE INSTR(nombreproducto,' ',1,2)+1 > 1;

4)
SELECT RANK() OVER (ORDER BY SUM(cantidad) DESC) rank, idproducto,nombreproducto, SUM(cantidad)totalvendido FROM PRODUCTO NATURAL JOIN COMPRA NATURAL JOIN FACTURA 
WHERE EXTRACT(YEAR FROM fecha) = (SELECT MAX(EXTRACT(YEAR FROM fecha)) FROM FACTURA)
GROUP BY idproducto, nombreproducto;

5)
WITH pre_query AS (SELECT fecha, EXTRACT(MONTH FROM fecha) AS mes, idproducto, nombreproducto,  cantidad FROM PRODUCTO NATURAL JOIN COMPRA NATURAL JOIN FACTURA  
GROUP BY EXTRACT(MONTH FROM fecha), fecha, idproducto, nombreproducto, 
cantidad
HAVING EXTRACT(YEAR FROM fecha) = (SELECT MAX(EXTRACT(YEAR FROM fecha)) FROM PRODUCTO NATURAL JOIN COMPRA NATURAL JOIN FACTURA)
ORDER BY mes)
SELECT mes, idproducto, nombreproducto, sum(cantidad) FROM pre_query GROUP BY mes, idproducto, nombreproducto ORDER BY MES;

6) Realizar una consulta que muestre la información de los clientes fieles. Es decir aquellos que realizaron alguna compra tanto el primer como el último año registrado.

SELECT cc, apellido, nombre from FACTURA NATURAL JOIN CLIENTE
WHERE EXTRACT(YEAR FROM fecha) = (SELECT MAX(EXTRACT(YEAR FROM fecha)) FROM FACTURA NATURAL JOIN CLIENTE)
INTERSECT
SELECT cc, apellido, nombre from FACTURA NATURAL JOIN CLIENTE
WHERE EXTRACT(YEAR FROM fecha) = (SELECT MIN(EXTRACT(YEAR FROM fecha)) FROM FACTURA NATURAL JOIN CLIENTE);

7) Realizar una consulta que muestra la información de los productos que han sido comprados por mas de 5 clientes distintos.

SELECT idproducto, nombreproducto,COUNT(cc) AS clientes_compran FROM PRODUCTO NATURAL JOIN COMPRA NATURAL JOIN FACTURA NATURAL JOIN CLIENTE
GROUP BY idproducto, nombreproducto
HAVING COUNT(CC) > 5;

8) Realizar una consulta que muestre la información completa del producto más vendido en el último año. 

WITH ultimo_yr AS (SELECT IDproducto, nombreproducto, SUM(cantidad) as cant FROM PRODUCTO NATURAL JOIN COMPRA NATURAL JOIN FACTURA 
WHERE EXTRACT(YEAR FROM fecha) = (SELECT MAX(EXTRACT(YEAR FROM fecha)) FROM PRODUCTO NATURAL JOIN COMPRA NATURAL JOIN FACTURA)
GROUP BY IDproducto, nombreproducto)
SELECT IDproducto, nombreproducto, cant FROM ultimo_yr 
WHERE cant = (SELECT MAX(cant) FROM ultimo_yr); 