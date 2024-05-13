import unittest
from TestDiagram.codigoDeHistoriasDeUsuario import *

class TestHistorias10_15(unittest.TestCase):
    
    def testcreandoAlerta(self):
        dptoCoor = DepartamentoDeCoodinacion("Juan","juanita22","Google")
        # Llamada a newAlerta() con los argumentos correctos
        alerta1 = dptoCoor.newAlerta("departamento",12345678,"Mesa del periodo de abril","se le solicita profesor que acepte de no ser así indique el motivo")
        # Afirmaciones para verificar los valores de la alerta creada
        print(alerta1.emisor)
        self.assertEqual(alerta1.emisor, "departamento")
        self.assertEqual(alerta1.receptor, 12345678)
        self.assertEqual(alerta1.titulo, "Mesa del periodo de abril")
        self.assertEqual(alerta1.mensaje, "se le solicita profesor que acepte de no ser así indique el motivo")

    
    def testenviarAlertaCorrecta(self):
       
        dptoCoor = DepartamentoDeCoodinacion("Juan", "juanita22", "Google")
        alerta1=dptoCoor.newAlerta("departamento", 12345678, "Mesa del periodo de abril", "se le solicita profesor que acepte, de no ser asi indique el motivo")
        profesor1=Profesor("Juan Perez",12345678)
        notificadorMediatorSingleton= dptoCoor.intanceMediator()
        notificadorMediatorSingleton.profesores.append(profesor1)
        notificadorMediatorSingleton.notificarAlerta(alerta1)
        
        for alerta in profesor1.bandejaDeAlertas:
            self.assertEqual(alerta.emisor, alerta1.emisor)
            self.assertEqual(alerta.receptor, alerta1.receptor)
            self.assertEqual(alerta.titulo, alerta1.titulo)
            self.assertEqual(alerta.mensaje, alerta1.mensaje)
    
    
        # Crear una alerta con un receptor diferente al DNI del profesor
    def testenviarAlertaIncorrecta(self):
       
        dptoCoor = DepartamentoDeCoodinacion("Juan", "juanita22", "Google")
        alerta2=dptoCoor.newAlerta("departamento",55555555,  "Mesa del periodo de abril","se le solicita profesor que acepte, de no ser asi indique el motivo")    
        profesor2=Profesor("Juana Garcia",12345679)
        profesor2.bandejaDeAlertas.clear()
        notificadorMediatorSingleton= dptoCoor.intanceMediator()
        notificadorMediatorSingleton.profesores.append(profesor2)
        with self.assertRaises(Exception):
            notificadorMediatorSingleton.notificarAlerta(alerta2)
        
        self.assertEqual(len(profesor2.bandejaDeAlertas), 0)


    def testAceptarAlerta(self):
        dptoCoor = DepartamentoDeCoodinacion("Juan", "juanita22", "Google")
        alerta1=dptoCoor.newAlerta("departamento", 12345678, "Mesa del periodo de abril", "se le solicita profesor que acepte, de no ser asi indique el motivo")
        profesor1=Profesor("Juan Perez", 12345678)
        notificadorMediatorSingleton= dptoCoor.intanceMediator()
        notificadorMediatorSingleton.profesores.append(profesor1)
        notificadorMediatorSingleton.notificarAlerta(alerta1)
        profesor1.responderNotificacion(alerta1,"acepto")

        self.assertEqual(len(profesor1.bandejaDeAlertas), 1)
        self.assertEqual(alerta1.respuesta, "acepto")
    

    def testRechazarAlerta(self):
        dptoCoor = DepartamentoDeCoodinacion("Juan", "juanita22", "Google")
        alerta1=dptoCoor.newAlerta("departamento", 12345678, "Mesa del periodo de abril", "se le solicita profesor que acepte, de no ser asi indique el motivo")
        profesor1=Profesor("Juan Perez", 12345678)
        profesor1.bandejaDeAlertas.clear()
        notificadorMediatorSingleton= dptoCoor.intanceMediator()
        notificadorMediatorSingleton.profesores.clear()
        notificadorMediatorSingleton.addProfesor(profesor1)
        notificadorMediatorSingleton.notificarAlerta(alerta1)
        profesor1.responderNotificacion(alerta1, "rechazo por", "Matrimonio ")

        self.assertEqual(len(profesor1.bandejaDeAlertas), 1)
        self.assertEqual(alerta1.respuesta, "rechazo por Matrimonio ")

    def testPosponerAlerta(self):
        dptoCoor = DepartamentoDeCoodinacion("Juan", "juanita22", "Google")
        alerta1=dptoCoor.newAlerta("departamento", 12345678, "Mesa del periodo de abril", "se le solicita profesor que acepte, de no ser asi indique el motivo")
        profesor1=Profesor("Juan Perez", 12345678)
        profesor1.bandejaDeAlertas.clear()
        notificadorMediatorSingleton= dptoCoor.intanceMediator()
        notificadorMediatorSingleton.profesores.clear()
        notificadorMediatorSingleton.addProfesor(profesor1)
        notificadorMediatorSingleton.notificarAlerta(alerta1)
        profesor1.responderNotificacion(alerta1, "pospongo", "Matrimonio ", 2024, 6, 15)

        self.assertEqual(len(profesor1.bandejaDeAlertas), 1)
        self.assertEqual(alerta1.respuesta, "pospongo por Matrimonio hasta 2024-06-15")  


if __name__ == '__main__':
    unittest.main()

#profesor1.responderNotificacion(alerta1,"rechazo por", " Matrimonio ", 2024,6,15 )