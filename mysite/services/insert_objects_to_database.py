from mysite.models.route import Route
from mysite.models.range import Range
from mysite.models.group import Group
from mysite.models.point import Point
from mysite.models.segment import Segment, DefinedSegment
from mysite.models.user import User, Tourist, Admin

def insert_all():
    insert_points_to_db()
    insert_users_to_db()
    insert_routes_to_db()
    insert_segment_to_db()


def insert_points_to_db():
    Point(name='Murowaniec', height=1500).save()
    Point(name='Czarny staw', height=1624).save()
    Point(name='Zawrat', height=2159).save()
    Point(name='Babia Góra', height=1725).save()
    Point(name='Przełęcz Krowiarki', height=1010).save()


def insert_users_to_db():
   bartek = User.objects.create_user(email='bartek@gmail.com', password='Oo', name='Bartek', surname='Nowak')
   bartek.save()
   Tourist(birth_date='2000-10-10', user=bartek).save()  # .route_set.all(), zeby dostac trasy turysty
   martynka = User.objects.create_user(email='martynka@gmail.com', password='Oo', name='Martyna', surname='Grzegorczyk')
   martynka.save()
   Tourist(birth_date='2000-11-10', user=martynka).save()
   admin = User.objects.create_user(email='pracownik@gmail.com', password='Oo', name='admin', surname='admin')
   admin.save()
   Admin(user=admin).save()


def insert_routes_to_db():
    Route(name="moja_traska", start_date="2020-10-11", end_date="2020-10-11", tourist=Tourist.objects.all()[0]).save()
    Route(name="moja_traska2", start_date="2020-10-12", end_date="2020-10-12", tourist=Tourist.objects.all()[0]).save()
    Route(name="moja_traska", start_date="2020-10-13", end_date="2020-10-13", tourist=Tourist.objects.all()[1]).save()


def insert_segment_to_db():
    Group(name="Karpaty", country="Poland").save()
    Range(name="Tatry", country="Poland", group=Group.objects.filter(name="Karpaty")[0]).save()
    Range(name="Beskid Żywiecki", country="Poland", group=Group.objects.filter(name="Karpaty")[0]).save()
    murow = Segment(length=1000, range=Range.objects.filter(name="Tatry")[0])
    czarny = Segment(length=1200, range=Range.objects.filter(name="Tatry")[0])
    przelecz = Segment(length=1500, range=Range.objects.filter(name="Beskid Żywiecki")[0])
    murow.save()
    czarny.save()
    przelecz.save()
    DefinedSegment(segment=murow, points=100, name="tatry1", start_point=Point.objects.filter(name="Murowaniec")[0],
                   end_point=Point.objects.filter(name="Czarny staw")[0]).save()
    DefinedSegment(segment=czarny, points=150, name="tatry2",
                   start_point=Point.objects.filter(name="Czarny staw")[0], end_point=Point.objects.filter(name="Zawrat")[0]).save()
    DefinedSegment(segment=przelecz, points=150, name='beskid1', start_point=Point.objects.filter(name="Babia Góra")[0],
                   end_point=Point.objects.filter(name="Przełęcz Krowiarki")[0]).save()
