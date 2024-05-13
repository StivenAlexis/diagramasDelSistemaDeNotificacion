````mermaid
classDiagram
  class ProfesorDecorator {
    +Int dni
    +List<Notificacion> bandejaDeNotificaciones
    +PlataformaMediator plataformaMediador
    +RecibirNotificacion(Notificacion)
    +ConfigurarNotificacion(frecuencia, formato)
    +PedirListaDeMesasPropias()
    +AgregarRecordatorio(Mesa, fecha, hora)
    +AgregarRecordatorio(Mesa, frecuencia)
    +EliminarRecordatorio(Mesa, fecha, hora)
    +EliminarRecordatorio(Mesa, frecuencia)
    +ModificarRecordatorios(Mesa, fecha, hora)
    +ModificarRecordatorios(Mesa, frecuencia)
    +ResponderAlerta(notificacion, respuesta)
  }
  class DepartamentoDeCoordinacionDecorator {
    +List<Mesa> mesas
    +Mediador mediador
    +crearMesa(fecha, asignatura ,hora, llamado, modalidad, aula, docentes[], alumnos[])
    +modificarHoraDeLaMesa(Mesa, Horario)
    +eliminarMesa(Mesa)
    +cambiarProfesor(Mesa mesa, ProfesorDecorator rechazado, ProfesorDecorator cambio)
    +Notificar(Profesor)
    +alertaDeMesa(mesa, profesor)
  }
  class Notificacion {
    +Int diaProgramado
    +Int mesProgramado
    +Int anioProgramado
    +String horaProgramado
    +String receptor
    +String emisor
    +String titulo
    +String mensaje
  }
  class Alerta {
    +String respuesta
    +Aceptar()
    +Rechazar(String motivo)
    +Posponer(String motivo, Int dia, Int mes, Int anio)
  }
  class IPlataformaDeComunicacionStrategy {
    <<Interface>>
    +EnviarNotificacion(notificacion Notificacion)
  }
  class SmsStrategy {
    -String numeroDeTelefono
    +enviarNotificacion(notificacion Notificacion)
    +setMediator(mediator PlataformaMediator)  
}
  class MailStrategy {
    -String correo
    +enviarNotificacion(notificacion Notificacion)
    +setMediator(mediator PlataformaMediator)
}
  class Alumno {
    -String nombre
    -String apellido
    -Int dni
  }
  class Mesa {
    -String periodoDeMesa
    -Int fecha
    -String asignatura
    -String llamado
    -String modalidad
    -Int numeroAula
    -Int hora
    -String rolProfesor
    -List<Alumno> alumnosPresentes
    -List<ProfesorDecorator> profesoresPresentes
  }
  class CuentaBaseDecorator {
    <<Abstract>>
    -String nombreUsuario
    -String contrasenia
    -List<IFormasDeAcceso> formasDeAcceso
  }
  class IFormasDeAcceso {
    <<Interface>>
    +getAccessKey()
  }
  class AccesoGoogle {
    +String mail
    -String contraseña
  }
  class ICalendarioStrategy {
    <<Interface>>
    +agregarEvento(tituloEvento, cuerpo, horaDeInicio, horaDeFinalizacion, dia, mes, anio)
  }
  class GoogleCalendarStrategy {
    -AccesoGoogle cuenta
    +AgregarEvento(tituloEvento, cuerpo, horaDeInicio, horaDeFinalizacion, dia, mes, anio)
  }
  class NotificadorMediatorSingleton {
    -List<ProfesorDecorator> profesores
    -NotificadorMediatorSingleton instancia
    -NotificadorMediatorSingleton()
    +getinstancia(): NotificadorMediatorSingleton
    +notificar(Notificacion notificacion)
    +notificarAlerta(Alerta alerta)
  }
   class PlataformaMediator{
    -List<IPlataformaDeComunicacionStrategy> estrategiasDeComunicacion
    -List<ICanlendario> calendarios
    +enviarNotificacion(notificacion:Notificacion)
    +agregarEvento(tituloEvento, cuerpo, horaDeInicio, horaDeFinalizacion, dia, mes, anio)
  }
  Mesa o-- Alumno: *
  Mesa o-- ProfesorDecorator: *




  DepartamentoDeCoordinacionDecorator --> Mesa: modificarHoraDeLaMesa()
  DepartamentoDeCoordinacionDecorator o-- Mesa: *
 
  Notificacion <|-- Alerta: hereda




  ICalendarioStrategy <|.. GoogleCalendarStrategy: aplica
  IPlataformaDeComunicacionStrategy  <|.. SmsStrategy: *
 
  IPlataformaDeComunicacionStrategy  <|.. MailStrategy: *




  CuentaBaseDecorator <|-- ProfesorDecorator : Hereda
  CuentaBaseDecorator <|-- DepartamentoDeCoordinacionDecorator: Hereda
  CuentaBaseDecorator o-- IFormasDeAcceso : *




  ProfesorDecorator "1" o-- "*" Notificacion
  NotificadorMediatorSingleton "1" o-- "*" ProfesorDecorator
 
  DepartamentoDeCoordinacionDecorator --> NotificadorMediatorSingleton : mediador




  IFormasDeAcceso <|.. AccesoGoogle: aplica




  ProfesorDecorator --> PlataformaMediator
  PlataformaMediator o--  IPlataformaDeComunicacionStrategy:*
  PlataformaMediator o-- ICalendarioStrategy
