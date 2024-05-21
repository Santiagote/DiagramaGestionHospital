from django.db import models
from enum import Enum
class Persona(models.Model):
        nombre = models.CharField(max_length=50)
        direccion = models.CharField(max_length=50)
        dni = models.CharField(max_length=10)
        class Meta:
            abstract = True

class Especialidad(Enum):
    Pediatria = 'Pediatria'
    Cardiologia = 'Cardiologia'
    Dermatologia = 'Dermatologia'

class Doctor(Persona):
    identificacion = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=50, choices=[(tag, tag.value) for tag in Especialidad])

    def atenderPaciente(self, paciente):
        pass

class Paciente(Persona):
    pass

class Enfermero(Persona):
    identificacion = models.CharField(max_length=20)

    def ayudarPaciente(self):
        pass
    def asistirDoctor(self):
        pass

class ExpedienteMedico(models.Model):
    diagnostico = models.CharField(max_length=50)
    tratamiento = models.CharField(max_length=50)
    prescripcion = models.CharField(max_length=50)

class CitasMedicas(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

class GestionCitas(models.Model):
    programarCita = 'ProgramarCita'
    cancelarCita = 'CancelarCita'
    realizarCita = 'realizarCita'

# Create your models here.
