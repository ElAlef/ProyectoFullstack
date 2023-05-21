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
import { FooterComponent } from './componentes/footer/footer.component';
import { TurneroComponent } from './pages/turnero/turnero.component';
import { HttpClientModule} from '@angular/common/http';
import { EspecialistasComponent } from './pages/turneroweb/especialistas/especialistas.component';
import { EspecialidadesComponent } from './pages/turneroweb/especialidades/especialidades.component';

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
    EspecialistasComponent,
    EspecialidadesComponent, 
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
