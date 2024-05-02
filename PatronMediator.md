```mermaid
classDiagram
  class Profesor {
    -String nombre
    -Int dni
    -List<IPlataformaDeComunicacion> plataformasPreferidas
    -List<ICalendario> calendariosPreferidos
    -List<Notificacion> bandejaDeNotificaciones
    -Mediador mediador
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
    -String titulo
    -String mensaje
  }

  class Alerta {
    +Aceptar()
    +Eliminar()
    +Posponer()
  }

  class IPlataformaDeComunicacion {
    <<Interface>>
    +EnviarNotificacion(notificacion: Notificacion)
    +setMediator(mediator: PlataformaMediator)

  }
class PlataformaMediator{
-List<IPlataformaDeComunicacion> plataformas
+enviarNotificacion(notificacion:Notificacion)
}


  class SMS {
    -String numeroDeTelefono
    +enviarNotificacion(notificacion: Notificacion)
    +setMediator(mediator:PlataformaMediator)  
}

  class Email {
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

  class Mediador {
    -List<IPlataformaDeComunicacion> plataformasComunicacion
    -ICalendario calendario
    +enviarNotificacion(notificacion: Notificacion)
    +agregarEventoCalendario(tituloEvento, cuerpo, horaDeInicio, horaDeFinalizacion, dia, mes, anio)
    +notificarAlerta(mesa: Mesa, profesor: Profesor)
  }

  Mesa o-- Alumno: *
  Mesa o-- Profesor: *

  DepartamentoDeCoordinacion --> Mesa: mesaParaEditar
  DepartamentoDeCoordinacion o-- Mesa: *
  DepartamentoDeCoordinacion --> Profesor: notificar mesa

  Notificacion <|-- Alerta: hereda

  ICalendario <|.. GoogleCalendar: aplica

  Cuenta <|-- Profesor : Hereda
  Cuenta <|-- DepartamentoDeCoordinacion: Hereda
  Cuenta o-- IFormasDeAcceso : *


  Profesor o-- ICalendario: [1..*]
  Profesor --> Mediador: mediador
  DepartamentoDeCoordinacion --> Mediador: mediador

  IFormasDeAcceso <|.. AccesoGoogle: aplica

PlataformaMediator	-->   Profesor
PlataformaMediator   o--  IPlataformaDeComunicacion:*
PlataformaMediator   o--  SMS: *
PlataformaMediator   o--  Email: *


