
```mermaid

classDiagram
  class Profesor {
    -String nombre
    -Int dni
    -List<IPlataformaDeComunicacion> plataformasPeferidas
    -List<ICalendario> calendariosPeferidos
    -List<Notificacion> bandejaDeNotificaciones
    +RecibirNotificacion(Notificacion)
    +ElegirHorario()
    +ConfigurarNotificacion(frecuencia,formato)
    +PedirListaDeMesasPropias()
    +AgregarRecordatorio(Mesa, fecha, hora)
    +AgregarRecordatorio(Mesa, frecuencia)
    +EliminarRecordatorio(Mesa, fecha,hora)
    +EliminarRecordatorio(Mesa, frecuencia)
    +ModificarRecordatorios(Mesa, fecha, hora)
    +ModificarRecordatorios(Mesa, frecuencia)
    +ResponderAlerta(notificacion, respuesta)
  }

  class DepartamentoDeCoordinacion{
   -List<Mesa> mesas
  +crearMesa()
  +modificarHoraDeLaMesa(Mesa)
  +eliminarMesa(Mesa)
  +cambiarProfesor(Mesa mesa,Profesor rechazado,Profesor cambio)
  +Notificar(Profesor)
  +alertaDeMesa(mesa, profesor)

}

  class Notificacion{
    -String titulo
    -String mensaje
  }

  class Alerta{
   +Aceptar()
   +Eliminar()
   +Posponer()
   }

  class IPlataformaDeComunicacion{
	<<Interface>>
     +EnviarNotificacion()
  }

  class SMS {
     -String numeroDeTelefono
     +EnviarNotificacion()
  }

 class Email {
     -String correo
     +EnviarNotificacion()
  }


class   Alumno{
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

  class Cuenta{
    <<Abstract>>
    -String nombreUsuario
    -String contraseña
    -List<IFormasDeAcceso> cuentas
  }

  class IFormasDeAcceso{
    <<Interface>>
   +getAccessKey()
    
 }
  class AccesoGoogle{
    -string mail
    -string contraseña
  }


 class ICalendario{
    <<Interface>>
     +agregarEvento(tituloEvento, cuerpo,horaDeInicio,horaDeFinalizacion,dia,mes,anio)
}
class GoogleCalendar{
   -AccesoGoogle cuenta
   +AgregarEvento(tituloEvento, cuerpo,horaDeInicio,horaDeFinalizacion,dia,mes,anio)
}

 
  Mesa o-- Alumno: *
  Mesa o-- Profesor: *

  DepartamentoDeCoordinacion -->  Mesa: mesaParaEditar
  DepartamentoDeCoordinacion o-- Mesa: *
  DepartamentoDeCoordinacion --> Profesor: notificar mesa
  

 Notificacion  <|-- Alerta: hereda

 ICalendario <|.. GoogleCalendar: aplica

  Cuenta <|-- Profesor : Hereda
  Cuenta <|-- DepartamentoDeCoordinacion: Hereda
  Cuenta o-- IFormasDeAcceso : *

  Profesor o-- IPlataformaDeComunicacion: *
  Profesor o-- ICalendario: [1..*]
  Profesor  --> DepartamentoDeCoordinacion: configurar notificacion
  

  IFormasDeAcceso <|.. AccesoGoogle: aplica
  

  IPlataformaDeComunicacion <|.. SMS: aplica
  IPlataformaDeComunicacion <|.. Email: aplica





