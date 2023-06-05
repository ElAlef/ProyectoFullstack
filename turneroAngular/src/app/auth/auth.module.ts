import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { AppRoutingModule } from '../app-routing.module';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';




@NgModule({
  declarations: [LoginComponent, RegistroComponent],
  imports: [
    CommonModule, AppRoutingModule,ReactiveFormsModule, FormsModule
  ], exports: [LoginComponent, RegistroComponent]
})
export class AuthModule { }