#########################################

#           TAREA 4

#########################################

# Campos:
#rut: str
#nombre: str
#apellido: str
#mail: str
#telefono: int
#cuenta: Cuenta
class Cliente:

    # Constructor
    def __init__(self, rut, nombre, apellido, mail, telefono):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono
        #Notese que el rut DEBE ser con guion (como str. Y no acepta digito verificador k!).
        self.cuenta = Cuenta(int(rut[:len(rut)-2] + rut[len(rut)-1:]), 0)

    # Accesores
    def getRut(self):
        return self.rut

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getMail(self):
        return self.mail

    def getTelefono(self):
        return self.telefono

    def getCuenta(self):
        return self.cuenta


    # Mutadores
    def setRut(self, rut):
        self.rut = rut

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.nombre = apellido

    def setMail(self, mail):
        self.mail = mail

    def setTelefono(self, telefono):
        self.telefono = telefono


    # Metodos
    def toString(self):
        n1 = self.getNombre()
        n2 = self.getApellido()
        return n1 + ' ' + n2


# Campos:
#numero: int
#saldo: int
class Cuenta:

    # Constructor
    def __init__(self, numero, saldo):
        self.numero = numero # asociado al rut del cliente (es unico! :D)
        self.saldo = saldo
        
    # Accesores
    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo


    # Mutadores
    def setNumero(self, numero):
        self.numero = numero

    def setSaldo(self, saldo):
        self.saldo = saldo

    
# Campos:
#cuenta: Cuenta
#tipo: str
#fecha: str
#monto: int
class Movimiento:

    # Constructor
    def __init__(self, cuenta, tipo, fecha, monto):
        self.tipo = tipo
        self.fecha = fecha
        self.monto = monto
        self.cuenta = cuenta

    # Accesores
    def getTipo(self):
        return self.tipo

    def getFecha(self):
        return self.fecha

    def getMonto(self):
        return self.monto


    # Mutadores
    def setTipo(self, tipo):
        self.tipo = tipo

    def setFecha(self, fecha):
        self.fecha = fecha

    def setMonto(self, monto):
        self.monto = monto

    def setMovimiento(self, tipo, fecha, monto):
        self.tipo.setTipo(tipo)
        self.fecha.setFecha(fecha)
        self.monto.setMonto(monto)

    # Metodos

    def retirar(self):
        if self.tipo == 'salida':
            if self.monto <= self.cuenta.saldo:
                self.cuenta.saldo -= self.monto
            else: return -1

    def depositar(self):
        if self.tipo == 'entrada':
            self.cuenta.saldo += self.monto


# Clase de testeo -
class Banco:

    # Constructor
    def __init__(self):
        self.cliente1 = Cliente('19995610-8', 'Jorge', 'Herrera', 'jorgito98@hotmail.com', 4123555)
        self.cliente2 = Cliente('20054416-7', 'Alicia', 'Ramirez', 'aaramirez23@gmail.com', 7494462)
        self.cliente3 = Cliente('17695005-6', 'Henrique', 'Silva', 'darknight69@gmail.com', 2564775)
        self.c1movRetiro5000 = Movimiento(self.cliente1.cuenta, 'salida', '15-11-2017', 5000)
        self.c1movDeposito14000 = Movimiento(self.cliente1.cuenta, 'entrada', '12-11-2017', 14000)
        self.mov1 = Movimiento(self.cliente2.cuenta, 'entrada', '02-10-2017', 1000)

    # Tests
    def test(self):
        # Numeros de cuenta distintos
        assert self.cliente1.cuenta.getNumero() != self.cliente2.cuenta.getNumero()
        assert self.cliente2.cuenta.getNumero() != self.cliente3.cuenta.getNumero()
        assert self.cliente3.cuenta.getNumero() != self.cliente1.cuenta.getNumero()

        # Todos parten con saldo = 0
        assert self.cliente1.cuenta.getSaldo() == 0
        assert self.cliente2.cuenta.getSaldo() == 0
        assert self.cliente3.cuenta.getSaldo() == 0

        # Test metodo toString
        assert self.cliente1.toString() == 'Jorge Herrera'
        assert self.cliente2.toString() == 'Alicia Ramirez'
        assert self.cliente3.toString() == 'Henrique Silva'

        # Tests metodos retirar y depositar
        self.c1movRetiro5000.retirar() == -1
        assert self.cliente1.cuenta.getSaldo() == 0
        self.c1movDeposito14000.depositar()
        assert self.cliente1.cuenta.getSaldo() == 14000
        self.c1movRetiro5000.retirar()
        assert self.cliente1.cuenta.getSaldo() == 9000

        # Tests accesores
        ## Cliente
        self.cliente3.getRut() == self.cliente3.rut
        self.cliente3.getNombre() == self.cliente3.nombre
        self.cliente3.getApellido() == self.cliente3.apellido
        self.cliente3.getMail() == self.cliente3.mail
        self.cliente3.getTelefono() == self.cliente3.telefono
        self.cliente3.getCuenta() == self.cliente3.cuenta

        ## Cuenta
        self.cliente3.cuenta.getNumero() == self.cliente3.cuenta.numero
        self.cliente3.cuenta.getSaldo() == self.cliente3.cuenta.saldo

        ## Movimiento
        self.c1movRetiro5000.getTipo() == self.c1movRetiro5000.tipo
        self.c1movRetiro5000.getFecha() == self.c1movRetiro5000.fecha
        self.c1movRetiro5000.getMonto() == self.c1movRetiro5000.monto

        # Tests mutadores
        ## Cliente
        self.cliente2.setRut('20054416-1')
        self.cliente2.getRut() == '20054416-1'
        self.cliente2.setNombre('Alice')
        self.cliente2.getNombre() == 'Alice'
        self.cliente2.setApellido('Robinson')
        self.cliente2.getApellido() == 'Robinson'
        self.cliente2.setMail('aramirez23@gmail.com')
        self.cliente2.getMail() == 'aramirez23@gmail.com'
        self.cliente2.setTelefono(7494400)
        self.cliente2.getTelefono() == 7494400

        ## Cuenta
        self.cliente2.cuenta.setNumero(0)
        self.cliente2.cuenta.getNumero() == 0
        self.cliente2.cuenta.setSaldo(45000000)
        self.cliente2.cuenta.getSaldo() == 45000000

        ## Movimiento
        self.mov1.setTipo('salida')
        self.mov1.getTipo() == 'salida'
        self.mov1.setFecha('27-02-2015')
        self.mov1.getFecha() == '27-02-2015'
        self.mov1.setMonto(6500)
        self.mov1.getMonto() == 6500

        

# ejecucion del test
test = Banco()
test.test()


# Simulacion

c1 = Cliente('19995610-8', 'Jorge', 'Herrera', 'jorgito98@hotmail.com', 4123555)
c2 = Cliente('20054416-7', 'Alicia', 'Ramirez', 'aaramirez23@gmail.com', 7494462)
c3 = Cliente('17695005-6', 'Henrique', 'Silva', 'darknight69@gmail.com', 2564775)
c4 = Cliente('13445305-2', 'Juana', 'Lagos', 'juanital@ing.uchile.cl', 4669223)

m1c1 = Movimiento(c1.cuenta, 'entrada', '12-11-2017', 5000)
m2c1 = Movimiento(c1.cuenta, 'entrada', '13-11-2017', 13000)
m3c1 = Movimiento(c1.cuenta, 'salida', '16-11-2017', 6000)
m4c1 = Movimiento(c1.cuenta, 'salida', '20-11-2017', 50000)

m1c2 = Movimiento(c2.cuenta, 'entrada', '19-11-2017', 500)
m2c2 = Movimiento(c2.cuenta, 'entrada', '12-11-2017', 26000)
m3c2 = Movimiento(c2.cuenta, 'salida', '17-11-2017', 6000)
m4c2 = Movimiento(c2.cuenta, 'salida', '12-11-2017', 3000)

m1c3 = Movimiento(c3.cuenta, 'entrada', '09-11-2017', 5000)
m2c3 = Movimiento(c3.cuenta, 'entrada', '11-11-2017', 15000)
m3c3 = Movimiento(c3.cuenta, 'entrada', '16-11-2017', 35000)
m4c3 = Movimiento(c3.cuenta, 'salida', '18-11-2017', 54999)

m1c4 = Movimiento(c4.cuenta, 'entrada', '04-03-2012', 80000)
m2c4 = Movimiento(c4.cuenta, 'salida', '24-05-2012', 13000)
m3c4 = Movimiento(c4.cuenta, 'salida', '15-10-2012', 6000)
m4c4 = Movimiento(c4.cuenta, 'salida', '21-10-2012', 50000)



clientes = [c1, c2, c3, c4]
nombres = map(lambda c: c.toString(), clientes)

print '- PROGRAMA DE SIMULACION DE CLASES Y METODOS -'

a = True
while a:
    print ''
    print 'Clientes:'
    for c in clientes:
        print '-> ' + c.toString()
    print ''
    print 'A continuacion, escriba el nombre de uno de nuestros clientes para comenzar la simulación.'
    print ''
    cx = raw_input('Simulación de ')
    print ''
    if not cx in nombres:
        print 'Nombre mal ingresado o invalido.'
        print ''
        a = False
        a = True
    elif cx in nombres:
        cliente = clientes[nombres.index(cx)]

        if cliente == c1:
            print 'Simulacion de ' + cliente.toString()
            print ''

            print cliente.cuenta.getSaldo()
            m1c1.depositar()
            print cliente.cuenta.getSaldo()
            m2c1.depositar()
            print cliente.cuenta.getSaldo()
            m3c1.retirar()
            print cliente.cuenta.getSaldo()
            m4c1.retirar() # Not enough saldo
            print cliente.cuenta.getSaldo()

        if cliente == c2:
            print 'Simulacion de ' + cliente.toString()
            print ''

            print cliente.cuenta.getSaldo()
            m4c2.retirar() # Not enough saldo
            print cliente.cuenta.getSaldo()
            m2c2.depositar()
            print cliente.cuenta.getSaldo()
            m3c2.retirar()
            print cliente.cuenta.getSaldo()
            m1c2.depositar()
            print cliente.cuenta.getSaldo()

        if cliente == c3:
            print 'Simulacion de ' + cliente.toString()
            print ''

            print cliente.cuenta.getSaldo()
            m1c3.depositar()
            print cliente.cuenta.getSaldo()
            m2c3.depositar()
            print cliente.cuenta.getSaldo()
            m3c3.depositar()
            print cliente.cuenta.getSaldo()
            m4c3.retirar()
            print cliente.cuenta.getSaldo()

        if cliente == c4:
            print 'Simulacion de ' + cliente.toString()
            print ''

            print cliente.cuenta.getSaldo()
            m1c4.depositar()
            print cliente.cuenta.getSaldo()
            m2c4.retirar()
            print cliente.cuenta.getSaldo()
            m3c4.retirar()
            print cliente.cuenta.getSaldo()
            m4c4.retirar()
            print cliente.cuenta.getSaldo()



'''

cliente = c1

print 'Simulacion de ' + cliente.toString()
print ''

print cliente.cuenta.getSaldo()
m1c1.depositar()
print cliente.cuenta.getSaldo()
m2c1.depositar()
print cliente.cuenta.getSaldo()
m3c1.retirar()
print cliente.cuenta.getSaldo()
m4c1.retirar() # Not enough saldo
print cliente.cuenta.getSaldo()

print ''
print ''

cliente = c2

print 'Simulacion de ' + cliente.toString()
print ''

print cliente.cuenta.getSaldo()
m4c2.retirar() # Not enough saldo
print cliente.cuenta.getSaldo()
m2c2.depositar()
print cliente.cuenta.getSaldo()
m3c2.retirar()
print cliente.cuenta.getSaldo()
m1c2.depositar()
print cliente.cuenta.getSaldo()

print ''
print ''

cliente = c3

print 'Simulacion de ' + cliente.toString()
print ''

print cliente.cuenta.getSaldo()
m1c3.depositar()
print cliente.cuenta.getSaldo()
m2c3.depositar()
print cliente.cuenta.getSaldo()
m3c3.depositar()
print cliente.cuenta.getSaldo()
m4c3.retirar()
print cliente.cuenta.getSaldo()

print ''
print ''

cliente = c4

print 'Simulacion de ' + cliente.toString()
print ''

print cliente.cuenta.getSaldo()
m1c4.depositar()
print cliente.cuenta.getSaldo()
m2c4.retirar()
print cliente.cuenta.getSaldo()
m3c4.retirar()
print cliente.cuenta.getSaldo()
m4c4.retirar()
print cliente.cuenta.getSaldo()

'''

