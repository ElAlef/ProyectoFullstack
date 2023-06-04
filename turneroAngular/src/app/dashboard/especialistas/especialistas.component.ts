import { Component,OnInit } from '@angular/core';
import { CuentaEspecialistasService } from 'src/app/services/cuenta-especialistas.service';


@Component({
  selector: 'app-especialistas',
  templateUrl: './especialistas.component.html',
  styleUrls: ['./especialistas.component.css']
})
export class EspecialistasComponent implements OnInit {
  hoy= new Date ();
  mostrarEspecialistas: boolean=true;
  especialistas:any;
  constructor( private cuenta: CuentaEspecialistasService)
  {
    this.cuenta.ObtenerUltimosMovimientos().subscribe({
      next: (especialistasData) =>{
        this.especialistas=especialistasData
      },
      error: (errorData) =>{
        console.error(errorData);
      }
    });
  }
  ngOnInit(): void{

  }
}
