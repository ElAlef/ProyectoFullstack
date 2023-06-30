import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { UserProfileService } from '../../user-profile.service';
import { UserProfile } from '../../interfaces/user-profile';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
userProfile: UserProfile|null = null;

  constructor(private userProfileService: UserProfileService, private activatedRoute: ActivatedRoute,private router: Router ) { }

  ngOnInit(): void {
    const userId = this.activatedRoute.snapshot.paramMap.get('id');
    this.userProfileService.getUserProfile(userId).subscribe({
        next: (data) => {
          console.log(data);
          this.userProfile = data;
        },
        error: (error) => {
          console.log(error);
        }
      }
    );
  }
  onSubmit(){
    Swal.fire({
      title: 'Estas por solicitar un turno Médico',
      showClass: {
        popup: 'animate__animated animate__fadeInDown'
      },
      hideClass: {
        popup: 'animate__animated animate__fadeOutUp'
      }
    })
    this.router.navigateByUrl(`/turnos`)
  }
}
