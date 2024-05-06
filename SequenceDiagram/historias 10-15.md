```mermaid
sequenceDiagram
    activate NotificacionMediatorSingleton
    activate departamentoDeCoordinacion1
    activate profesor1
    departamentoDeCoordinacion1 ->> alerta1: New(emisor, receptor, titulo, mensaje)
    activate alerta1
    alerta1 -->> departamentoDeCoordinacion1: 
    departamentoDeCoordinacion1 ->> NotificacionMediatorSingleton: notificarAlerta(alerta1)
    NotificacionMediatorSingleton ->> profesor1 : RecibirNotificacion(alerta1)
    profesor1 -->> NotificacionMediatorSingleton: 
    NotificacionMediatorSingleton -->> departamentoDeCoordinacion1: 
    alt El profesor acepta la Alerta
    profesor1 ->> alerta1: aceptar()
    else El profesor rechaza la alerta
    profesor1 ->> alerta1: rechazar(motivo)
    else El profesor pospone la alerta
    profesor1 ->> alerta1: posponer(motivo, dia, mes, anio)
    end


    alerta1 -->> profesor1: 
    deactivate alerta1
    deactivate profesor1
    deactivate departamentoDeCoordinacion1
    deactivate NotificacionMediatorSingleton
