import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { TurnosService } from '../../turnos.service';
import { turnos } from '../../interfaces/turnos';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-turnos',
  templateUrl: './turnos.component.html',
  styleUrls: ['./turnos.component.css']
})
export class TurnosComponent implements OnInit {
  hoy= new Date ();
  mostrarEspecialidades:turnos[]=[];
  especialidades:any;
  mostrarEspecialistas: boolean=true;
  especialistas:any;
  mostrarTurnos: boolean=true;
  Turnos:turnos[]=[];
  router: any;
 

constructor(private turnosService: TurnosService, private activatedRoute: ActivatedRoute) { 
  }
  ngOnInit(): void {
    this.turnosService.ObtenerTurnos().subscribe({
      next: (data) =>{
        this.Turnos=data
      },
      error: (error) =>{
        console.error(error);
      }
    });
  }

  confirmarTurno(){
   
    Swal.fire({
      title: 'Te derivamos al pago de tu consulta... !Gracias!',
      showClass: {
        popup: 'animate__animated animate__fadeInDown'
      },
      hideClass: {
        popup: 'animate__animated animate__fadeOutUp'
      }
    })
  }
 
}
 /* this.turnosService.ObtenerEspecialistas().subscribe({
    next: (data) =>{
      this.especialistas=data
    },
    error: (error) =>{
      console.error(error);
    }
  });
  this.turnosService.horarioDeAtencion().subscribe({
    next: (data) =>{
      this.horarioDeAtencion=data
    },
    error: (error) =>{
      console.error(error);
    }
  });

  
}
ngOnInit(): void{

}


 /* const userId = this.activatedRoute.snapshot.paramMap.get('id');
  this.turnosService.getTurnos(userId).subscribe({
      next: (data) => {
        console.log(data);
        this.turnos = data;
      },
      error: (error) => {
        console.log(error);
      }
    }
  );*/

