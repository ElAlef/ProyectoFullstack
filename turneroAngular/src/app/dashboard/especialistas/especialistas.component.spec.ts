import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EspecialistasComponent } from './especialistas.component';

describe('EspecialistasComponent', () => {
  let component: EspecialistasComponent;
  let fixture: ComponentFixture<EspecialistasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EspecialistasComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EspecialistasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
