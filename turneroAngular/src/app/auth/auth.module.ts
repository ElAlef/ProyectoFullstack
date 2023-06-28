import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { RegistroComponent } from './componentes/registro/registro.component';

import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { AuthRoutingModule } from './auth-routing.module';
import { HttpClientModule } from '@angular/common/http';




@NgModule({
  declarations: [RegistroComponent],

  imports: [
    CommonModule,
    AuthRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    FormsModule
  ], 
})
export class AuthModule { }