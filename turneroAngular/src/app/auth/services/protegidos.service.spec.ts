import { TestBed } from '@angular/core/testing';

import { ProtegidosService } from './protegidos.service';

describe('ProtegidosService', () => {
  let service: ProtegidosService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProtegidosService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
