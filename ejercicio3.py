a = True
b = True
c = False
d = True
e = False

#1ra Condicion
if(a or b):
    print("primera condicion: Verdadero");
else:    
    print("primera condicion: Falsa");

#2da Condicion
if(a or c):
    print("segunda condicion: Verdadero");
else:    
    print("segunda condicion: Falsa");

#3ra Condicion
if(a and e):
    print("tercera condicion: Verdadero");
else:    
    print("tercera condicion: Falsa");

#4ta Condicion
if((a or e) and b):
    print("cuarta condicion: Verdadero");
else:    
    print("cuarta condicion: Falsa");

#5ta Condicion
if((a or e) and c):
    print("Quinto condicion: Verdadero");
else:    
    print("Quinto condicion: Falsa");

#6ta Condicion
if((a or e) and (c or b)):
    print("Sexto condicion: Verdadero");
else:    
    print("Sexto condicion: Falsa");

#7ma Condicion
if(((a and b)and c) or e):
    print("Septimo condicion: Verdadero");
else:    
    print("Septimo condicion: Falsa");