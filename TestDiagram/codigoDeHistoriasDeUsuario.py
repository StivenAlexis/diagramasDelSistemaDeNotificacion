from abc import ABC
from datetime import datetime
from urllib import request


class Cuenta(ABC):
    def __init__(self, nombreDeUsuario, contraseña, formasDeAcceso):
        self.nombreDeUsuario = nombreDeUsuario
        self.contraseña = contraseña
        self.formasDeAcceso = formasDeAcceso



class Notificacion:
    def __init__(self, diaProgramado, mesProgramado, anioProgramado, horaProgramado,receptor,titulo,mensaje,emisor):
        self.emisor = emisor
        self.receptor = receptor
        self.titulo = titulo
        self.mensaje = mensaje
        self.fechaProgramada = datetime(anioProgramado, mesProgramado, diaProgramado, horaProgramado)



class Mesa:
    def __init__(self, periodoDeMesa, profesor, fecha,asignatura,llamado,modalidad,numeroDeAula,hora,rolProfesor,alumnosPresentes,profesoresPresentes):
        self.periodoDeMesa = periodoDeMesa
        self.profesor = profesor
        self.fecha = datetime(fecha)
        self.asignatura = asignatura
        self.llamado = llamado
        self.modalidad = modalidad
        self.numeroDeAula = numeroDeAula
        self.hora = hora
        self.rolProfesor = rolProfesor
        self.alumnosPresentes = alumnosPresentes
        self.profesoresPresentes = profesoresPresentes



class Alerta:
    def __init__(self,emisor,receptor,titulo,mensaje,):
        self.emisor = emisor
        self.receptor = receptor
        self.titulo = titulo
        self.mensaje = mensaje
    
    respuesta = ""
    
    def aceptar(self):
        self.respuesta= "acepto"
        

    def rechazar(self,motivo):
        self.respuesta= "rechazo por "+ motivo 
        

    def posponer(self,motivo,anio,mes,dia):
        fechaRespuesta= datetime(anio, mes, dia)
        fechaRespuestaString=fechaRespuesta.strftime("%Y-%m-%d")

        self.respuesta= "pospongo por "+ motivo + "hasta " + fechaRespuestaString
              



class DepartamentoDeCoodinacion(Cuenta):
    
    mesas=[]

    def intanceMediator(self):
        mediator = NotificadorMediatorSingleton.getInstance()
        return mediator
 
    alertasEnviadas = []
    def newAlerta(self, emisor, receptor, titulo, mensaje):
        alerta = Alerta(emisor, receptor, titulo, mensaje)
        self.alertasEnviadas.append(alerta)
        return alerta

    def crearMesa(self,anio,mes,dia,hora,profesor,asignatura,modalidad,numeroDeAula,llamado,rolProfesor,alumnosPresentes,profesoresPresentes):
        mesa=Mesa(anio,mes,dia,hora,profesor,asignatura,modalidad,numeroDeAula,llamado,rolProfesor,alumnosPresentes,profesoresPresentes)
        return mesa

        
   

class NotificadorMediatorSingleton:
    
    profesores=[]
    __instance = None

    def getprofesores(self):
        return self.profesores
    

    def addProfesor(self, profesor):
        profesorExistente=False
        for profeso in self.profesores:
            if profeso.dni == profesor.dni:
                raise Exception("El profesor ya esta en la lista")
                profesorExistente=True
    
        if profesorExistente==False:
            self.profesores.append(profesor)
    


    @staticmethod
    def getInstance():
        if NotificadorMediatorSingleton.__instance == None:
            NotificadorMediatorSingleton()
        return NotificadorMediatorSingleton.__instance

    def __init__(self):
        if NotificadorMediatorSingleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            NotificadorMediatorSingleton.__instance = self

    def notificarAlerta(self, alerta):
        
        for profesor in self.profesores:
            profesorEncontrado = False
            if profesor.dni == alerta.receptor:
                profesor.recibirAlerta(alerta)
                profesorEncontrado = True
        if profesorEncontrado == False:
            raise Exception("No se encontró ningún profesor con DNI")


    def notificar(notificacion):
        print("Notificando")

class Profesor(Cuenta):
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        
    bandejaDeAlertas=[]

    def recibirAlerta(self, alerta):
        self.bandejaDeAlertas.append(alerta)       

    def responderNotificacion(self, alerta= Alerta,respuesta=str,motivo="",anio=0,mes=0,dia=0):
        if  respuesta== "acepto":
            alerta.aceptar()
        elif "rechazo" in respuesta:
            alerta.rechazar(motivo)
        elif "pospongo" in respuesta:
            alerta.posponer(motivo,anio,mes,dia)
        return alerta