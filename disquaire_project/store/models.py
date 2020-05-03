from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField('Nom', max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "artiste"


class Contact(models.Model):
    email = models.EmailField('Email', max_length=100)
    name = models.CharField('Nom', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Prospect"


class Album(models.Model):
    reference = models.IntegerField('référence', null=True)
    created_at = models.DateTimeField('date d\'ajout',auto_now_add=True)
    available = models.BooleanField('disponible', default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Album"


class Booking(models.Model):
    created_at = models.DateTimeField('date de commande', auto_now_add=True)
    contacted = models.BooleanField('demande traitée ?', default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name

    class Meta:
        verbose_name = "Réservation"
