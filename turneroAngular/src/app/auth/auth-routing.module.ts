import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RegistroComponent } from './componentes/registro/registro.component';

const routes: Routes = [
  {
    path: '',
    children: [
      
      {
        path: 'registro',
        component: RegistroComponent
      },
      // {
      //   path: '**',
      //   redirectTo: 'login'
      // }
    ]
  }
]


@NgModule({
  declarations: [],
  imports: [
      RouterModule.forChild(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AuthRoutingModule { }

