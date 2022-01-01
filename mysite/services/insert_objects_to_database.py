from mysite.models.point import Point


def insert_points_to_db():
    Point(name='Murowaniec').save()
    Point(name='Czarny staw').save()