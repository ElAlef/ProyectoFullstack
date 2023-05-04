import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './componentes/login/login.component';
import { ServiciosComponent } from './pages/servicios/servicios.component';
import { RegistroComponent } from './componentes/registro/registro.component';


const routes: Routes = [
  
  { path: "login", component: LoginComponent, pathMatch: "full" },
  { path: "Servicios", component: ServiciosComponent },
  { path: "Registro", component: RegistroComponent}
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
