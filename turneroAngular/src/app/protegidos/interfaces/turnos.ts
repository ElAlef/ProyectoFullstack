export interface turnos{
    
    
        id_Turnos: number,
        id_Horario: {
            id_Horario: number,
            id_Especialista: {
                id_Especialista: number,
                id_Especialidad: {
                    id_Especialidad: number,
                    nombre: string,
                },
                nombre: string,
            },
            dia_de_la_semana: string,
            hora_inici: number,
            hora_fi: number,
        },
        fecha: number,
        horarioDeInicio: number,
        horarioDeFin: number,
    }
    

