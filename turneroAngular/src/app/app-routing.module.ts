
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ServiciosComponent } from './pages/servicios/servicios.component';
import { ContactosComponent } from './pages/contactos/contactos.component';

import { UserLoginComponent } from "./login/user-login/user-login.component";
import { UserProfileComponent } from "./protegidos/pages/user-profile/user-profile.component";
import { AuthGuard } from './login/auth.guard';
import { TurnosComponent } from './protegidos/pages/turnos/turnos.component';
import { ProtegidosModule } from './protegidos/protegidos.module';



const routes: Routes = [
  { path: 'login', component: UserLoginComponent },
  { path: 'user-profile/:id', component: UserProfileComponent, canActivate: [AuthGuard] },
  { path: 'turnos', component: TurnosComponent,canActivate: [AuthGuard] },  


  { path: '', redirectTo: '/servicios', pathMatch: 'full'},
  { path: "servicios", component: ServiciosComponent },
  { path: "Contactos", component: ContactosComponent},
 
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule,ProtegidosModule]
})
export class AppRoutingModule { }