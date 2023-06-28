import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { TurnosService } from '../turnos.service';
import { turnos } from '../turnos';

@Component({
  selector: 'app-turnos',
  templateUrl: './turnos.component.html',
  styleUrls: ['./turnos.component.css']
})
export class TurnosComponent implements OnInit {
  hoy= new Date ();
  mostrarEspecialidades: boolean=true;
  especialidades:any;
  mostrarEspecialistas: boolean=true;
  especialistas:any;
  mostrarhorarioDeAtencion: boolean=true;
  horarioDeAtencion:any;
 

constructor(private turnosService: TurnosService, private activatedRoute: ActivatedRoute) { 
  this.turnosService.ObtenerEspecialidades().subscribe({
    next: (data) =>{
      this.especialidades=data
    },
    error: (error) =>{
      console.error(error);
    }
  });

  this.turnosService.ObtenerEspecialistas().subscribe({
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
}
