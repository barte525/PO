from mysite.models.point import Point
from mysite.models.user import User, Tourist
from mysite.models.route import Route
from mysite.models.range import Range
from mysite.models.group import Group
from mysite.models.segment import Segment, DefinedSegment, CustomSegment


def insert_all():
    insert_points_to_db()
    #insert_users_to_db()
    insert_routes_to_db()
    insert_segment_to_db()


def insert_points_to_db():
    Point(name='Murowaniec').save()
    Point(name='Czarny staw').save()


def insert_users_to_db():
   bartek = User.objects.create_user(email='bartek@gmail.com', password='Oo', name='Bartek', surname='Nowak')
   Tourist(birth_date='2000-10-10', user=bartek).save()  # .route_set.all(), zeby dostac trasy turysty


def insert_routes_to_db():
    Route(name="moja traska", start_date="2020-10-11", end_date="2020-10-11", tourist=Tourist.objects.all()[0]).save()


def insert_segment_to_db():
    Group(name="Karpaty", country="Poland").save()
    Range(name="Tatry", country="Poland", group=Group.objects.filter(name="Karpaty")[0]).save()
    Segment(length=10, range=Range.objects.filter(name="Tatry")[0]).save()
    CustomSegment(elevation=100, start_name="jagodno", end_name="sobieski", start_height=100, end_height=200, segment=Segment.objects.filter(length=10)[0]).save()
    DefinedSegment(segment=Segment.objects.filter(length=10)[0], points=100, name="try", start_point=Point.objects.filter(name="Murowaniec")[0],
                   end_point=Point.objects.filter(name="Czarny staw")[0]).save()
    DefinedSegment(segment=Segment.objects.filter(length=10)[0], points=100, name="try2",
                   start_point=Point.objects.filter(name="Murowaniec")[0], end_point=Point.objects.filter(name="Czarny staw")[0]).save()