from mysite.models.point import Point
from mysite.models.user import User, Tourist
from mysite.models.route import Route


def insert_points_to_db():
    Point(name='Murowaniec').save()
    Point(name='Czarny staw').save()


def insert_users_to_db():
    bartek = User.objects.create_user(email='bartek@gmail.com', password='Oo', name='Bartek', surname='Nowak')
    Tourist(birth_date='2000-10-10', user=bartek).save()  # .route_set.all(), zeby dostac trasy turysty


def insert_routes_to_db():
    Route(name="moja traska", start_date="2020-10-11", end_date="2020-10-11", tourist=Tourist.objects.all()[0]).save()
