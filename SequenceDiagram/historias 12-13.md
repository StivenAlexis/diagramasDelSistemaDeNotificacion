```mermaid
sequenceDiagram
    activate departamentoDeCoordinacion1
    departamentoDeCoordinacion1 ->> departamentoDeCoordinacion1: crearMesa(fecha, asignatura ,hora, llamado, modalidad, aula, docentes[], alumnos[])
    departamentoDeCoordinacion1 ->> mesa1: new(fecha, asignatura ,hora, llamado, modalidad, aula, docentes[], alumnos[])
    activate mesa1
    mesa1 -->> departamentoDeCoordinacion1: 
    departamentoDeCoordinacion1 ->> departamentoDeCoordinacion1 : ModificarHorarioDeLaMesa(mesa1, horarioNuevo)
    departamentoDeCoordinacion1 ->> mesa1: hora = horarioNuevo
    mesa1 -->> departamentoDeCoordinacion1: 
    deactivate mesa1
    deactivate departamentoDeCoordinacion1
