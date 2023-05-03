import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './componentes/login/login.component';
import { ServiciosComponent } from './pages/servicios/servicios.component';


const routes: Routes = [
  
  { path: "login", component: LoginComponent, pathMatch: "full" },
  { path: "Servicios", component: ServiciosComponent }
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
