import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EspecialidadesComponent } from './especialidades/especialidades.component';
import { EspecialistasComponent } from './especialistas/especialistas.component';



@NgModule({
  declarations: [EspecialidadesComponent, EspecialistasComponent],
  imports: [
    CommonModule
  ], exports: [EspecialidadesComponent, EspecialistasComponent]
})
export class DashboardModule { }
