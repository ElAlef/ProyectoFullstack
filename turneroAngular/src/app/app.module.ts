import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { SharedModule } from './shared/shared.module';
import { PagesModule } from './pages/pages.module';
import { HttpClientModule} from '@angular/common/http';
import { AuthModule } from './auth/auth.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule } from "@angular/material/toolbar";
import { UserLoginComponent } from './login/user-login/user-login.component';
import { HTTP_INTERCEPTORS } from "@angular/common/http";
import { MatInputModule } from "@angular/material/input";
import { MatButtonModule } from "@angular/material/button";
import { TokenInterceptor } from './login/token.interceptor';
import { MatCardModule } from "@angular/material/card";
import { ProtegidosModule } from './protegidos/protegidos.module';



@NgModule({
  declarations: [
    AppComponent,
    UserLoginComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatToolbarModule,
    ReactiveFormsModule,
    FormsModule,
    SharedModule,
    PagesModule,
    AuthModule,
    ProtegidosModule,
    BrowserAnimationsModule,
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatToolbarModule,
    MatInputModule,
    MatButtonModule,
    MatCardModule,
  ],
  providers: [ { provide: HTTP_INTERCEPTORS, useClass: TokenInterceptor, multi: true },],
  bootstrap: [AppComponent]
})
export class AppModule { }
