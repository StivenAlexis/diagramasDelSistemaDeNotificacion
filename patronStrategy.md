```mermaid
classDiagram
  class Profesor {
    -String nombre
    -Int dni
    -List<IPlataformaDeComunicacionStrategy> plataformasPreferidas
    -List<ICalendario> calendariosPreferidos
    -List<Notificacion> bandejaDeNotificaciones
    -PlataformaMediator plataformaMediador
    +RecibirNotificacion(Notificacion)
    +ElegirHorario()
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

  class DepartamentoDeCoordinacion {
    -List<Mesa> mesas
    -Mediador mediador
    +crearMesa()
    +modificarHoraDeLaMesa(Mesa)
    +eliminarMesa(Mesa)
    +cambiarProfesor(Mesa mesa, Profesor rechazado, Profesor cambio)
    +Notificar(Profesor)
    +alertaDeMesa(mesa, profesor)
  }

  class Notificacion {
    -String receptor
    -String emisor
    -String titulo
    -String mensaje
  }

  class Alerta {
    +Aceptar()
    +Eliminar()
    +Posponer()
  }

  class IPlataformaDeComunicacionStrategy {
    <<Interface>>
    +EnviarNotificacion(notificacion: Notificacion)
    

  }



  class smsStrategy {
    -String numeroDeTelefono
    +enviarNotificacion(notificacion: Notificacion)
    +setMediator(mediator:PlataformaMediator)  
}

  class emailStrategy {
    -String correo
    +enviarNotificacion(notificacion: Notificacion)
    +setMediator(mediator:PlataformaMediator  
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
    -List<Profesor> profesoresPresentes
  }

  class Cuenta {
    <<Abstract>>
    -String nombreUsuario
    -String contraseña
    -List<IFormasDeAcceso> cuentas
  }

  class IFormasDeAcceso {
    <<Interface>>
    +getAccessKey()
  }

  class AccesoGoogle {
    -String mail
    -String contraseña
  }

  class ICalendario {
    <<Interface>>
    +agregarEvento(tituloEvento, cuerpo, horaDeInicio, horaDeFinalizacion, dia, mes, anio)
  }

  class GoogleCalendar {
    -AccesoGoogle cuenta
    +AgregarEvento(tituloEvento, cuerpo, horaDeInicio, horaDeFinalizacion, dia, mes, anio)
  }

  class NotificacionMediator {
    +notificar(Notificacion notificacion)
    +notificarAlerta(Alerta alerta)
  }
   class PlataformaMediator{
    -List<IPlataformaDeComunicacionStrategy> estrategiasDeComunicacion 
    -List<ICanlendario> calendarios
    +enviarNotificacion(notificacion:Notificacion)
  }
  Mesa o-- Alumno: *
  Mesa o-- Profesor: *

  DepartamentoDeCoordinacion --> Mesa: mesaParaEditar
  DepartamentoDeCoordinacion o-- Mesa: *
  
  Notificacion <|-- Alerta: hereda

  ICalendario <|.. GoogleCalendar: aplica
  IPlataformaDeComunicacionStrategy  <|.. smsStrategy: *
  
  IPlataformaDeComunicacionStrategy  <|.. emailStrategy: *

  Cuenta <|-- Profesor : Hereda
  Cuenta <|-- DepartamentoDeCoordinacion: Hereda
  Cuenta o-- IFormasDeAcceso : *


  Profesor "1" o-- "*" Notificacion
  Profesor --> NotificacionMediator: mediador
  

  DepartamentoDeCoordinacion --> NotificacionMediator : mediador

  IFormasDeAcceso <|.. AccesoGoogle: aplica

    PlataformaMediator --> Profesor
    PlataformaMediator   o--  IPlataformaDeComunicacionStrategy:*
    PlataformaMediator   o-- ICalendario
