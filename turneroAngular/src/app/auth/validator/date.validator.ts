<<<<<<< HEAD
import { FormControl, ValidationErrors } from '@angular/forms';
import Swal from 'sweetalert2';

export class DateValidator {

   static LessThanToday(control: FormControl): ValidationErrors | null {
        let today : Date = new Date();
        let pendejo: Date = new Date(2004,1,1)
        

       if (new Date(control.value) > today) {
       Swal.fire('La fecha de nacimiento no puede ser mayor al día actual. Corrijala');
           return { "LessThanToday": true };
       } else if(new Date(control.value)> pendejo) {
        Swal.fire('Debe ser mayor de 18 para usar la plataforma');
        return { "LessThanToday": true };
      

       }
       return null;
   }
=======
import { FormControl, ValidationErrors } from '@angular/forms';
import Swal from 'sweetalert2';

export class DateValidator {

   static LessThanToday(control: FormControl): ValidationErrors | null {
        let today : Date = new Date();
        let pendejo: Date = new Date(2004,1,1)
        

       if (new Date(control.value) > today) {
       Swal.fire('La fecha de nacimiento no puede ser mayor al día actual. Corrijala');
           return { "LessThanToday": true };
       } else if(new Date(control.value)> pendejo) {
        Swal.fire('Debe ser mayor de 18 para usar la plataforma');
        return { "LessThanToday": true };
      

       }
       return null;
   }
>>>>>>> e2784648b725e3bb9a61b09bb89940c33049c467
}