import { Component, OnInit } from '@angular/core';
import { FormBuilder,FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
    form!: FormGroup;
    
    

  constructor(private formBuilder: FormBuilder) {}
  ngOnInit() {
    this.form = this.formBuilder.group(
      {
        password:['',[Validators.required, Validators.minLength(8)]],
        mail:['',[Validators.required, Validators.email]],
        
           })
          }

  get Password() 
  {
    return this.form.get('password');
  }
  get Mail()
  {
    return this.form.get('mail');
  }
  
 
  onEnviar(event: Event)
  {
    event.preventDefault;

    if (this.form.valid)
    {
      alert("Enviar al servidor...")
    }else{
      this.form.markAllAsTouched();
    }

  }
  
  }
  
  
  

