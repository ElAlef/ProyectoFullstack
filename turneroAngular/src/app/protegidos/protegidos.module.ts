import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserProfileComponent } from './pages/user-profile/user-profile.component';


import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { TurnosComponent } from './pages/turnos/turnos.component';
import { MatCardModule } from "@angular/material/card";






@NgModule({
  declarations: [
    UserProfileComponent, TurnosComponent],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MatCardModule,
    
    
  ],
  exports: [TurnosComponent],

})
export class ProtegidosModule { }