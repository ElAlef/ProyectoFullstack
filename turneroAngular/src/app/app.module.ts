import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './componentes/header/header.component';
import { LoginComponent } from './componentes/login/login.component';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { ServiciosComponent } from './pages/servicios/servicios.component';
import { ContactosComponent } from './pages/contactos/contactos.component';
import { RegistroComponent } from './componentes/registro/registro.component';
import { FooterComponent } from './footer/footer.component';
import { TurneroComponent } from './pages/turnero/turnero.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    LoginComponent,
    ServiciosComponent,
    ContactosComponent,
    RegistroComponent,
    FooterComponent,
    TurneroComponent,
<<<<<<< HEAD

=======
>>>>>>> RamaAlejandro
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
