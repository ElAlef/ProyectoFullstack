import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import Swal from 'sweetalert2';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {


  formularioLogin: FormGroup = this.formBuilder.group({

    'username': ['', [Validators.required, Validators.minLength(5), Validators.email] ],
    'password': ['', [Validators.required, Validators.minLength(8)] ]

  })
  
  

  constructor(private formBuilder: FormBuilder,
    private authService: AuthService) { }

  ngOnInit(): void {
  }


  guardar(){

    if(this.formularioLogin.invalid){
      Swal.fire({
        icon: 'error',
        title: 'Error de Inicio de Sesión',
        text: 'Revise los campos, hay errores'
      })
    }else{
      this.logueo();
      Swal.fire({
        title: 'Ingresado con su usuario...',
        html: 'Porfavor, espere. Le indicaremos cuando hayamos finalizado. ',
        didOpen: () => {
          Swal.showLoading()
        }
      })
    }
    
  }

  logueo(){
    
    const { username, password } = this.formularioLogin.value; 

    this.authService.login(username,password); 


  }



}
/*export class LoginComponent implements OnInit {
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


  }*/
  
  
  

