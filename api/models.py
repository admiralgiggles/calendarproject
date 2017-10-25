from django.db import models

# Camera model
class Camera(models.Model):
    class Meta:
        verbose_name_plural = "Camere"

    numar = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return "Camera: " + str(self.numar)


# Rezervare model
class Rezervare(models.Model):
    class Meta:
        verbose_name_plural = "Rezervări"

    rez_id = models.AutoField(primary_key=True)

    # client details
    nume = models.CharField(max_length=20)
    prenume = models.CharField(max_length=20)
    serie_buletin = models.CharField(max_length=30, blank=True)
    adresa = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=60, blank=True)
    telefon = models.CharField(max_length=20)
    tara = models.CharField(max_length=48, blank=True)
    localitate = models.CharField(max_length=85, blank=True)
    
    # rent details
    date_start = models.DateField()
    date_end = models.DateField()
    camera = models.ForeignKey(Camera, related_name='rezervari', on_delete=models.CASCADE)
    comentariu = models.TextField(blank=True)

    def __str__(self):
        return  "(" + str(self.rez_id) + ") " + self.nume + " " + self.prenume + " - Camera: " + str(self.camera.numar) + " din " + str(self.date_start) + " până în " + str(self.date_end)