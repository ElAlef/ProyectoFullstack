import { TestBed } from '@angular/core/testing';

import { CuentaEspecialistasService} from 'src/app/services/cuenta-especialistas.service';

describe('CuentaEspecialistasService', () => {
  let service: CuentaEspecialistasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CuentaEspecialistasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});