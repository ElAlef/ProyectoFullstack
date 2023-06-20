import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PerfilComponent } from './perfil/perfil.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';

const routes: Routes = [

  {

    path: '',
component: DashboardComponent,
    children: [
      {path: '',
    component: PerfilComponent},
     
      {
        path: 'perfil',
        component: PerfilComponent
      },
      
     
    ]


  }


];



@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})

export class ProtegidosRoutingModule { }

