
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ServiciosComponent } from './pages/servicios/servicios.component';
import { ContactosComponent } from './pages/contactos/contactos.component';
import { EspecialistasComponent } from './dashboard/especialistas/especialistas.component';
import { EspecialidadesComponent } from './dashboard/especialidades/especialidades.component';
import { UserLoginComponent } from "./user-login/user-login.component";
import { UserProfileComponent } from "./user-profile/user-profile.component";
import { AuthGuard } from "./auth.guard";
import { TurnosComponent } from './turnos/turnos.component';



const routes: Routes = [
  { path: 'login', component: UserLoginComponent },
  { path: 'user-profile/:id', component: UserProfileComponent, canActivate: [AuthGuard] },
  { path: 'turnos', component: TurnosComponent,canActivate: [AuthGuard] },  


  { path: '', redirectTo: '/servicios', pathMatch: 'full'},
  { path: "servicios", component: ServiciosComponent },
  { path: "Contactos", component: ContactosComponent},
  { path: "especialistas",component:EspecialistasComponent},
  { path: "especialidades",component:EspecialidadesComponent}
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }