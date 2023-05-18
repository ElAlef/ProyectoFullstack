import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './componentes/login/login.component';
import { ServiciosComponent } from './pages/servicios/servicios.component';
import { ContactosComponent } from './pages/contactos/contactos.component';
import { RegistroComponent } from './componentes/registro/registro.component';
import { TurneroComponent } from './pages/turnero/turnero.component';
import { EspecialistasComponent } from './componentes/especialistas/especialistas.component';



const routes: Routes = [
  
  { path: "login", component: LoginComponent, pathMatch: "full" },
  { path: "Servicios", component: ServiciosComponent },
  { path: "Contactos", component: ContactosComponent},
  { path: "Registro", component: RegistroComponent},
  { path: "Turnero", component: TurneroComponent},
  { path: "especialistas",component:EspecialistasComponent}
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
