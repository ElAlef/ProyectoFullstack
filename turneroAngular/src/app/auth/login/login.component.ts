import { Component, OnInit} from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from 'src/app/services/auth/login.service';
import { LoginRequest } from 'src/app/services/auth/loginRequest';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginError:string = ""
  loginForm = this.formBuilder.group({
      email:['seba@gmail.com',[Validators.required, Validators.email]],
      password:['',[Validators.required]],
      
       })
     constructor(private formBuilder: FormBuilder, private router:Router,private loginService:LoginService ) {}
    
   ngOnInit(): void {
   }

   get email(){
    return this.loginForm.controls.email;
   }

   get password(){
    return this.loginForm.controls.password;
   }

   login(){
    if(this.loginForm.valid){
      this.loginService.login(this.loginForm.value as LoginRequest).subscribe({
        next: (userData) =>{
          console.log(userData);
        },
        error: (errorData) =>{
          console.log(errorData);
          this.loginError=errorData;
        },
        complete: () =>{
          console.info("Login completo");
          this.router.navigateByUrl('/especialidades');
          this.loginForm.reset();
        }
      })
      
    }
    else{
      alert("Error al ingresar los datos")
    }
   }


  }
  
  
  

