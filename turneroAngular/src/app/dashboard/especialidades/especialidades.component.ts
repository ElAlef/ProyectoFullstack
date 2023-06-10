import { Component, OnDestroy, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/auth/login.service';
import { User } from 'src/app/services/auth/user';
import { EspecialidadesService } from 'src/app/services/especialidades.service';

@Component({
  selector: 'app-especialidades',
  templateUrl: './especialidades.component.html',
  styleUrls: ['./especialidades.component.css']
})
export class EspecialidadesComponent implements OnInit , OnDestroy{
  mostrarEspecialidades: boolean=true;
  especialidades:any;
  userLoginOn:boolean=false;
  userData?:User;
  
  constructor( private cuenta: EspecialidadesService, private loginService: LoginService)
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

  ngOnDestroy(): void {
    this.loginService.currentUserData.unsubscribe();
    this.loginService.currentUserLoginOn.unsubscribe();
  }
  ngOnInit(): void{
    this.loginService.currentUserLoginOn.subscribe({
      next:(userLoginOn)=> {
        this.userLoginOn = userLoginOn;
      }
    });

    this.loginService.currentUserData.subscribe({
      next:(userData)=>{
        this.userData=userData;
      }
    })

  
  }
}
