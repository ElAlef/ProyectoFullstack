import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContactosComponent } from './contactos/contactos.component';
import { ServiciosComponent } from './servicios/servicios.component';



@NgModule({
  declarations: [ContactosComponent, ServiciosComponent],
  imports: [
    CommonModule
  ], exports: [ContactosComponent, ServiciosComponent]
})
export class PagesModule { }
