export interface UserProfile {
    id: string,
    username: string,
    nombre: string,
    apellido: string,
    fechaNacimiento: string | Date,
    dni: string,
    bio: string,
    profile_pic: string
  }