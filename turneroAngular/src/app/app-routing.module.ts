import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ServiciosComponent } from './pages/servicios/servicios.component';
import { ContactosComponent } from './pages/contactos/contactos.component';
import { EspecialistasComponent } from './dashboard/especialistas/especialistas.component';
import { EspecialidadesComponent } from './dashboard/especialidades/especialidades.component';
import { ValidarTokenGuard } from './guards/validar-token.guard';



const routes: Routes = [
  {
    path: 'auth',
    loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule)
 },
 {
  path: 'dashboard',
  loadChildren: () => import('./protegidos/protegidos.module').then(m => m.ProtegidosModule),
  canActivate: [
   ValidarTokenGuard
  ]
    
},

  { path: '', redirectTo: '/servicios', pathMatch: 'full'},
  { path: "servicios", component: ServiciosComponent },
  { path: "Contactos", component: ContactosComponent},
  { path: "especialistas",component:EspecialistasComponent},
  { path: "especialidades",component:EspecialidadesComponent}
  
];

@NgModule({
  imports: [CommonModule,RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }