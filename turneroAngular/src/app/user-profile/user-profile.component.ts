import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { UserProfileService } from "../user-profile.service";
import { UserProfile } from "../user-profile";

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
userProfile: UserProfile|null = null;

  constructor(private userProfileService: UserProfileService, private activatedRoute: ActivatedRoute) { }

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
}
