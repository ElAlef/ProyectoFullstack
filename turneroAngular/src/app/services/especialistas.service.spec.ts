import { TestBed } from '@angular/core/testing';

import { EspecialistasService } from './especialistas.service';

describe('EspecialistasService', () => {
  let service: EspecialistasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EspecialistasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
