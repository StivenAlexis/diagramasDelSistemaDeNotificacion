````mermaid

classDiagram

    class Profesor {
    -String nombre
    -Int dni
    -List<IPlataformaDeComunicacion> plataformasPeferidas
    -List<ICalendario> calendariosPeferidos
    -List<Notificacion> bandejaDeNotificaciones
    +recibirNotificacion(Notificacion)
    +ConfigurarNotificacion(frecuencia,formato)
    +AgregarRecordatorio(Mesa, fecha, hora)
    +AgregarRecordatorio(Mesa, frecuencia)
    +EliminarRecordatorio(Mesa, fecha,hora)
    +EliminarRecordatorio(Mesa, frecuencia)
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
    
    class Notificacion{
    -String titulo
    -String mensaje
    }

    class Mesa {
    -Int fecha
    -Float hora
    -Int cantAlumnosInscriptos
    -String funcionProfesorMesa
    }

    class IPlataformaDeComunicacion{
	<<Interface>>
    +enviarNotificacion()
    }
    
    class ICalendario{
    <<Interface>>
     +agregarEvento(tituloEvento, cuerpo,horaDeInicio,horaDeFinalizacion,dia,mes,anio)
    }

    class GoogleCalendar{
    -AccesoGoogle cuenta
    +agregarEvento(tituloEvento, cuerpo,horaDeInicio,horaDeFinalizacion,dia,mes,anio)
    }

    class SMS {
    -String numeroDeTelefono
    +EnviarNotificacion()
    }

    class Email {
    -String correo
    +EnviarNotificacion()
  }



    Profesor o-- IPlataformaDeComunicacion: *
    Profesor o-- ICalendario: [1..*]

    Cuenta <|-- Profesor : Hereda
    Cuenta o-- IFormasDeAcceso : *

    ICalendario <|.. GoogleCalendar: aplica

    IFormasDeAcceso <|.. AccesoGoogle: aplica

    IPlataformaDeComunicacion <|.. SMS: aplica
    IPlataformaDeComunicacion <|.. Email: aplica
