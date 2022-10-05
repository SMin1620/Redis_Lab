from redis_sorted.models import Movie


def gen_movie(apps, schema_editor):
    Movie.objects.create(
        name='Titanic',
        ticket_count=500,
        score=4.7
    )

    Movie.objects.create(
        name='Avengers',
        ticket_count=2000,
        score=5.0
    )

    Movie.objects.create(
        name='Avatar',
        ticket_count=100,
        score=4.2
    )

    Movie.objects.create(
        name='Star Wars',
        ticket_count=1500,
        score=4.9
    )

    for i in range(0, 10000):
        Movie.objects.create(
            name=f'movie name{i}',
            ticket_count=i,
        )

