import { Component, OnInit } from '@angular/core';
import { FormBuilder,FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {
  form!: FormGroup;

  constructor(private formBuilder: FormBuilder) {}
  ngOnInit() {
    this.form = this.formBuilder.group(
      {
        Nombre:['',[Validators.required, Validators.minLength(8)]],
        Apellido:['',[Validators.required, Validators.minLength(8)]],
        Dni:['',[Validators.required, Validators.minLength(8)]],
        Telefono:['',[Validators.required, Validators.minLength(8)]],
        Usuario:['',[Validators.required, Validators.minLength(8)]],
        password:['',[Validators.required, Validators.minLength(8)]],
        mail:['',[Validators.required, Validators.email]]
           })
          }
          get Nombre()
          {
            return this.form.get('Nombre');
          }
          get Apellido()
          {
            return this.form.get('Apellido');
          }
          get Dni()
          {
            return this.form.get('Dni');
          }
          get Telefono()
          {
            return this.form.get('Telefono');
          }
          get Mail()
          {
            return this.form.get('mail');
          }
          get Usuario()
          {
            return this.form.get('Usuario');
          }
          get Password() 
          {
            return this.form.get('password');
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
