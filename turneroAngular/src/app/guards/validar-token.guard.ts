<<<<<<< HEAD
<<<<<<< HEAD
import { Injectable } from '@angular/core';
import { CanActivate, CanLoad } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../auth/services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class ValidarTokenGuard implements CanActivate, CanLoad {

  constructor ( private authService: AuthService ) {}

  canActivate(): Observable<boolean>  | boolean  {
    return this.authService.validarToken()
    
  }
  canLoad(): Observable<boolean> | boolean  {
    return this.authService.validarToken()
  
  }
=======
import { Injectable } from '@angular/core';
import { CanActivate, CanLoad } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../auth/services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class ValidarTokenGuard implements CanActivate, CanLoad {

  constructor ( private authService: AuthService ) {}

  canActivate(): Observable<boolean>  | boolean  {
    return this.authService.validarToken()
    
  }
  canLoad(): Observable<boolean> | boolean  {
    return this.authService.validarToken()
  
  }
>>>>>>> 44b1b6363da120ebb924d13b3c4926848f63789d
=======
import { Injectable } from '@angular/core';
import { CanActivate, CanLoad } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../auth/services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class ValidarTokenGuard implements CanActivate, CanLoad {

  constructor ( private authService: AuthService ) {}

  canActivate(): Observable<boolean>  | boolean  {
    return this.authService.validarToken()
    
  }
  canLoad(): Observable<boolean> | boolean  {
    return this.authService.validarToken()
  
  }
>>>>>>> main
}