import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponentComponent implements OnInit {
  userLoginOn:boolean=false;
  constructor() { }

  ngOnInit() {
  }

}
