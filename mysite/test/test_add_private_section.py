from django.test import TestCase
from mysite.models.user import User, Tourist
from mysite.models.route import Route
from mysite.models.segment import CustomSegment
from mysite.views.add_private_section_view import AddPrivateSection
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


class TestAddPrivateSection(TestCase):
    def setUp(self):
        test = User.objects.create_user(email='test@gmail.com', password='Oo', name='test', surname='test')
        test.save()
        test_tourist = Tourist(birth_date='2000-10-10', user=test)
        test_tourist.save()
        self.route = Route(name="test_route1", start_date="2020-10-11", end_date="2020-10-11", tourist=test_tourist)
        self.route.save()
        self.route_id = self.route.id

    def test_incorrect_height(self):
        response = AddPrivateSection.create_segment(self.route_id, "1", "1", "", "0", "-1", "test", "", "0", "-1", "test", "test", "10")
        self.assertEqual(response, "Wprowadzona wartość liczbowa nie spełnia wymagań.")
        self.assertEqual(list(self.route.segments.all()), [])

    def test_incorrect_point_name(self):
        response = AddPrivateSection.create_segment(self.route_id, "1", "1", "", "0", "1", "x" * 201, "", "0", "1",
                                                    "test", "test", "10")
        self.assertEqual(response, "Długość nazwy punktu nie może być mniejsza od 1 znaku i większa od 200 znaków.")
        self.assertEqual(list(self.route.segments.all()), [])

        response = AddPrivateSection.create_segment(self.route_id, "1", "1", "", "0", "1", "", "", "0", "1",
                                                    "test", "test", "10")
        self.assertEqual(response, "Długość nazwy punktu nie może być mniejsza od 1 znaku i większa od 200 znaków.")
        self.assertEqual(list(self.route.segments.all()), [])

    def test_invalid_segment_name(self):
        response = AddPrivateSection.create_segment(self.route_id, "1", "1", "", "0", "1", "test", "", "0", "1",
                                                    "test", "", "10")
        self.assertEqual(response, "Długość nazwy odcinka nie może być mmniejsza od 1 znaku i większa od 200 znaków.")
        self.assertEqual(list(self.route.segments.all()), [])
        response = AddPrivateSection.create_segment(self.route_id, "1", "1", "", "0", "1", "test", "", "0", "1",
                                                    "test", "x"*201, "10")
        self.assertEqual(response, "Długość nazwy odcinka nie może być mmniejsza od 1 znaku i większa od 200 znaków.")
        self.assertEqual(list(self.route.segments.all()), [])

    def test_correct_create_custom_points(self):
        response = AddPrivateSection.create_segment(self.route_id, "1", "1", "", "0", "1", "test", "", "0", "1",
                                                    "test", "test1", "10")
        self.assertEqual(response, "Odcinek został zapisany w bazie.")
        self.assertEqual(list(self.route.segments.all()), [CustomSegment.objects.get(name='test1').segment])

    def test_correct_create_defined_points(self):
        response = AddPrivateSection.create_segment(self.route_id, "1", "1", "defined_point_s", "1", "", "", "defined_point_e",
                                                    "2", "", "", "test2", "10")
        self.assertEqual(response, "Odcinek został zapisany w bazie.")
        self.assertEqual(list(self.route.segments.all()), [CustomSegment.objects.get(name='test2').segment])
