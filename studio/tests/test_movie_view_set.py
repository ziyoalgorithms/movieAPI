
from multiprocessing import set_forkserver_preload
from django.test import TestCase, Client
from studio.models import Movie


class test_movie_view_set_list_movie(TestCase):
    def setUp(self):
        self.client = Client()

        self.movie = Movie.objects.create(name="Test Movie", year="2010-01-01", imdb=5, genre="JANGARI", )
        self.movie2 = Movie.objects.create(name="Test Movie 2", year="2004-10-11", imdb=7, genre="DRAMA", )
        self.movie3 = Movie.objects.create(name="Test Movie 3", year="2001-08-21", imdb=1, genre="FANTASTIK", )
        self.movie4 = Movie.objects.create(name="Test Movie 4", year="2000-02-15", imdb=9, genre="ROMANTIKA", )


    def test_list_movie(self):
        response = self.client.get("/movies/")
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 4)
        self.assertIsNotNone(data[0]["id"])
        self.assertIsNotNone(data[1]["id"])
        self.assertIsNotNone(data[2]["id"])
        self.assertIsNotNone(data[3]["id"])
        self.assertEquals(data[0]["name"], "Test Movie")
        self.assertEquals(data[1]["name"], "Test Movie 2")
        self.assertEquals(data[3]["name"], "Test Movie 4")
        self.assertEquals(data[2]["genre"], "FANTASTIK")
        self.assertEquals(data[1]["imdb"], 7)
        self.assertEquals(data[2]["year"], "2001-08-21")


class TestMovieSearch(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(name="Fantastik Movie", year="2010-01-01", imdb=5, genre="JANGARI", )
        self.movie = Movie.objects.create(name="Fantastik Kino", year="2010-01-01", imdb=5, genre="JANGARI", )


    def test_search(self):
        response = self.client.get("/movies/?search=Fantast")
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]["name"], "Fantastik Movie")
        self.assertEquals(data[1]["name"], "Fantastik Kino")


class TestMovieIMDB(TestCase):
    def setUp(self):
        self.client = Client()

        self.movie = Movie.objects.create(name="Test Movie", year="2010-01-01", imdb=1, genre="JANGARI", )
        self.movie2 = Movie.objects.create(name="Test Movie 2", year="2004-10-11", imdb=2, genre="DRAMA", )
        self.movie3 = Movie.objects.create(name="Test Movie 3", year="2001-08-21", imdb=3, genre="FANTASTIK", )
        self.movie4 = Movie.objects.create(name="Test Movie 4", year="2000-02-15", imdb=4, genre="ROMANTIKA", )

    def test_imdb(self):
        response = self.client.get("/movies/?ordering=imdb")
        response2 = self.client.get("/movies/?ordering=-imdb")
        data = response.data
        data2 = response2.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 200)
        for i in range(0, 4):
            self.assertEquals(data[i]["imdb"], i+1)
        self.assertEquals(data2[0]["imdb"], 4)
        self.assertEquals(data2[1]["imdb"], 3)
        self.assertEquals(data2[2]["imdb"], 2)
        self.assertEquals(data2[3]["imdb"], 1)
        self.assertNotEquals(data[0]["imdb"], 2)
        self.assertNotEquals(data[3]["imdb"], 2)
        self.assertNotEquals(data2[0]["imdb"], 1)
        self.assertNotEquals(data[2]["imdb"], 1)
