import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class UserProfileService {

  constructor(private http: HttpClient) { }

  getUserProfile(userId: string|null): Observable<any> {
    return this.http.get(`http://127.0.0.1:8000/api/v1/users/${userId}/`);
  }
}