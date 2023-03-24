
import datetime


class Cuentabancaria:
    def __init__(self,ID, nombre_titular, fecha_apertura,numero_cuenta, saldo):
        self.ID = ID
        self.nombre_titular = nombre_titular
        self.fecha_apertura = fecha_apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def retirar_dinero(self, retiro):
        
        if retiro<= self.saldo and self.saldo > 0:
            self.saldo -= retiro
            return True
        else:
            return False
        

    def ingresar_dinero(self, cantidad):
        
        if cantidad > 0:
            self.saldo += cantidad
            return True
        else:
            return False
        
    def transferir_dinero(self,otra_cuenta, cantidad):
        
        if isinstance(otra_cuenta, Cuentabancaria) and cantidad > 0 and cantidad <= self.saldo:
            self.retirar_dinero(cantidad)
            otra_cuenta.ingresar_dinero(cantidad)
            return True
        else:
            return False
        


class CuentaPlazoFijo(Cuentabancaria):
    def __init__(self, ID, nombre_titular, fecha_apertura, numero_cuenta, saldo, fecha_vencimiento):
        super().__init__(ID, nombre_titular, fecha_apertura, numero_cuenta, saldo)
        self.fecha_vencimiento = fecha_vencimiento

    def retirar_dinero(self, retiro):
        hoy = datetime.date.today()
        if hoy < self.fecha_vencimiento:
            penalizacion = (retiro * 5)/100
            return super().retirar_dinero(retiro + penalizacion)
        else:
            return super().retirar_dinero(retiro)


class CuentaVip(Cuentabancaria):
    def __init__(self, ID, nombre_titular, fecha_apertura, numero_cuenta, saldo, saldo_negativo_maximo):
        super().__init__(ID, nombre_titular, fecha_apertura, numero_cuenta, saldo)
        self.saldo_negativo_maximo = saldo_negativo_maximo

    def retirar(self, retiro):
        if (self.saldo - retiro) >= -self.saldo_negativo_maximo:
            return super().retirar_dinero(retiro)
        else:
            return False

    def transferir(self, otra_cuenta, retiro):
        if (self.saldo - retiro) >= -self.saldo_negativo_maximo:
            return super().transferir_dinero(otra_cuenta, retiro)
        else:
            return False




'''
A continuación, construye una aplicación que permita crear los tres tipos de cuentas. 
El ID tiene que ser un número entero incremental, el nombre del titular puede ser inventado, la fecha de apertura y fecha de vencimiento 
deben ser aleatorias siendo la fecha de apertura más antigua que la fecha de vencimiento,
y el número de cuenta tiene que ser un número aleatorio de 12 dígitos.
Cuando las cuentas estén iniciadas a un sueldo inicial de 10.000 €, transferir dinero de unas a otras las cantidades de 2000 €, 
ingresar 575 € y retirar dinero 78 €. 

'''

cuenta_1 = Cuentabancaria(1, "Juan", datetime.date(2019, 1, 1), 123456789012, 10000)
cuenta_plazo_fijo = CuentaPlazoFijo(2, "Pedro", datetime.date(2019, 1, 1), 123456789012, 10000, datetime.date(2020, 1, 1))
cuenta_vip = CuentaVip(3, "Maria", datetime.date(2019, 1, 1), 123456789012, 10000, 1000)

cuenta_1.transferir_dinero(cuenta_plazo_fijo, 2000)
cuenta_1.transferir_dinero(cuenta_vip, 2000)

cuenta_1.ingresar_dinero(575)
cuenta_1.retirar_dinero(78)
