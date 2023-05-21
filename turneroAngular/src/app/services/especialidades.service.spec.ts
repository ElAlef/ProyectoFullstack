import { TestBed } from '@angular/core/testing';

import { EspecialidadesService } from './especialidades.service';

describe('EspecialidadesService', () => {
  let service: EspecialidadesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EspecialidadesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
