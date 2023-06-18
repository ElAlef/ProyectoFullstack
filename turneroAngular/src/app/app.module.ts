import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { SharedModule } from './shared/shared.module';
import { PagesModule } from './pages/pages.module';
import { AuthModule } from './auth/auth.module';
import { HttpClientModule} from '@angular/common/http';
import { DashboardModule } from './dashboard/dashboard.module';
import { PerfilComponent } from './protegidos/perfil/perfil.component';

@NgModule({
  declarations: [
    AppComponent,
    PerfilComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    SharedModule,
    PagesModule,
    AuthModule,
    DashboardModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
