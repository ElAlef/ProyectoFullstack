import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './componentes/header/header.component';
import { LoginComponent } from './componentes/login/login.component';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { ServiciosComponent } from './pages/servicios/servicios.component';
<<<<<<< HEAD
import { ContactosComponent } from './pages/contactos/contactos.component';
=======
import { RegistroComponent } from './componentes/registro/registro.component';
>>>>>>> 359c506c24e5425280d368ecc554a813ba341f29


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    LoginComponent,
    ServiciosComponent,
<<<<<<< HEAD
    ContactosComponent
=======
    RegistroComponent
>>>>>>> 359c506c24e5425280d368ecc554a813ba341f29
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
