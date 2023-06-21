<<<<<<< HEAD
import { TestBed } from '@angular/core/testing';
import { ValidarTokenGuard } from './validar-token.guard';

describe('TokenGuard', () => {
  let guard: ValidarTokenGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(ValidarTokenGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
=======
import { TestBed } from '@angular/core/testing';
import { ValidarTokenGuard } from './validar-token.guard';

describe('TokenGuard', () => {
  let guard: ValidarTokenGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(ValidarTokenGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
>>>>>>> 44b1b6363da120ebb924d13b3c4926848f63789d
});