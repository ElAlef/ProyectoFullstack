import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { ServiciosComponent } from './pages/servicios/servicios.component';
import { ContactosComponent } from './pages/contactos/contactos.component';
import { RegistroComponent } from './auth/registro/registro.component';
import { EspecialistasComponent } from './dashboard/especialistas/especialistas.component';
import { EspecialidadesComponent } from './dashboard/especialidades/especialidades.component';



const routes: Routes = [
  { path: '', redirectTo: '/servicios', pathMatch: 'full'},
  { path: "login", component: LoginComponent },
  { path: "servicios", component: ServiciosComponent },
  { path: "Contactos", component: ContactosComponent},
  { path: "Registro", component: RegistroComponent},
  { path: "especialistas",component:EspecialistasComponent},
  { path: "especialidades",component:EspecialidadesComponent}
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }