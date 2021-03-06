from django.test import TestCase
from django.urls import reverse

from .models import Album, Artist, Contact, Booking

# Index page
class IndexPageTestCase(TestCase):
    # test that index page resturns a 200
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    

# Detail Page
class DetailPageTestCase(TestCase):

    def setUp(self):
        impossible = Album.objects.create(title="Transmission Impossible")
        self.album = impossible

    # test that detail page returns a 200 if the item exists
    def test_detail_page_returns_200(self):
        album_id = self.album.id
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the items does not exist
    def test_detail_page_returns_404(self):
        album_id = self.album.id + 1
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 404)

# Booking Page
class BookingPageTestCase(TestCase):
    
    def setUp(self):
        Contact.objects.create(name="Jojo", email="jojo@le.corbeau")
        impossible = Album.objects.create(title="Transmission Impossible")
        journey = Artist.objects.create(name="Journey")
        impossible.artists.add(journey)
        self.album = Album.objects.get(title='Transmission Impossible')
        self.contact = Contact.objects.get(name='Jojo')

    # test that a new booking is made
    def test_new_booking_is_registered(self):
        old_bookings = Booking.objects.count() # count bookings before a request
        album_id = self.album.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        new_bookings = Booking.objects.count() # count bookings after
        self.assertEqual(new_bookings, old_bookings + 1) # Test number of booking is incremented

    # test that a booking belong to a contact
    # test that a booking belongs to an album
    # test that an album is not available after a booking is made