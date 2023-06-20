import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PerfilComponent } from './perfil/perfil.component';


import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ProtegidosRoutingModule } from './protegidos-routing.module';
import { DashboardComponent } from './pages/dashboard/dashboard.component';





@NgModule({
  declarations: [
    PerfilComponent,
    DashboardComponent],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    ProtegidosRoutingModule
    
  ]

})
export class ProtegidosModule { }