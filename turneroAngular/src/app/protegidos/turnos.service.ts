import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class TurnosService {
  
  constructor(private http: HttpClient) {}
    
  ObtenerTurnos(): Observable <any>
  {
    return this.http.get("http://127.0.0.1:8000/Turnos/");
    
  }

  
  
}
/*  ObtenerEspecialistas(): Observable <any>
  {
    return this.http.get("http://127.0.0.1:8000/especialistas/");
  }
  horarioDeAtencion(): Observable <any>
  {
    return this.http.get("http://127.0.0.1:8000/HorarioDeAtencion/");
  }
    
   }

  getTurnos(userId: string|null): Observable<any> {
    return this.http.get(`http://127.0.0.1:8000/especialidades/`);
  }*/
  
