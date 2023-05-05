import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TurneroComponent } from './turnero.component';

describe('TurneroComponent', () => {
  let component: TurneroComponent;
  let fixture: ComponentFixture<TurneroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TurneroComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TurneroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
