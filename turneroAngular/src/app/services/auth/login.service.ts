import { Injectable } from '@angular/core';
import { LoginRequest } from './loginRequest';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, throwError, BehaviorSubject, tap } from 'rxjs';
import { User } from './user';
@Injectable({
  providedIn: 'root'
})
export class LoginService {

  currentUserLoginOn: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  currentUserData: BehaviorSubject<User> = new BehaviorSubject<User>({id:0, email:''});

  constructor(private http: HttpClient) { }

  login(credentials:LoginRequest):Observable<User>{
    return this.http.get<User>('http://localhost:8000/api/auth/login/').pipe(
      tap((userData: User) =>{
        this.currentUserData.next(userData);
        this.currentUserLoginOn.next(true);
      }),
      catchError(this.handleError) 
    )
  }

  private handleError(error:HttpErrorResponse){
    if(error.status===0){
      console.log('Se ha producido un error', error.error);
    }
    else{
      console.log('Backend retornó el código de estado', error.status, error.error);
    }
    return throwError(()=> new Error('Algo falló. por favor intente nuevamente'));
  }

  get userData():Observable<User>{
    return this.currentUserData.asObservable();
  }

  get userLoginOn():Observable<boolean>{
    return this.currentUserLoginOn.asObservable();
  }
}
