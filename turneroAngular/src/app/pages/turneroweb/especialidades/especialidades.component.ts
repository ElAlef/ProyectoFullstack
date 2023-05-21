import { Component, OnInit } from '@angular/core';
import { EspecialidadesService } from 'src/app/services/especialidades.service';

@Component({
  selector: 'app-especialidades',
  templateUrl: './especialidades.component.html',
  styleUrls: ['./especialidades.component.css']
})
export class EspecialidadesComponent implements OnInit{
  mostrarEspecialidades: boolean=true;
  especialidades:any;
  constructor( private cuenta: EspecialidadesService)
  {
    this.cuenta.ObtenerListaEspecialidades().subscribe({
      next: (especialidadesData) =>{
        this.especialidades=especialidadesData
      },
      error: (errorData) =>{
        console.error(errorData);
      }
    });
  }
  ngOnInit(): void{

  }
}
