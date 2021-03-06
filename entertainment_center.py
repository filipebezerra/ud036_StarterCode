import media
import fresh_tomatoes

the_butterfly_effect = media.Movie("The Butterfly Effect",
                                   "https://image.tmdb.org/t/p/original/3PAQy3CyNNJPES772OFMx47lFEE.jpg",  # noqa
                                   "https://www.youtube.com/watch?v=B8_dgqfPXFg")  # noqa

jurassic_park = media.Movie("Jurassic Park",
                            "https://image.tmdb.org/t/p/original/c414cDeQ9b6qLPLeKmiJuLDUREJ.jpg",  # noqa
                            "https://www.youtube.com/watch?v=QWBKEmWWL38")  # noqa

the_grudge = media.Movie("The Grudge",
                         "https://image.tmdb.org/t/p/original/y05X9RL0FIcEwoVSTppCPcQwhvf.jpg",  # noqa
                         "https://www.youtube.com/watch?v=bj88_yqlFMA")  # noqa

big_mommas_house = media.Movie("Big Momma's House",
                               "https://image.tmdb.org/t/p/original/bse0uwxF6daKzDbxZki1SYRNZkI.jpg",  # noqa
                               "https://www.youtube.com/watch?v=njhwlzuPXv4")  # noqa

the_exorcist = media.Movie("The Exorcist",
                           "https://image.tmdb.org/t/p/original/4ucLGcXVVSVnsfkGtbLY4XAius8.jpg",  # noqa
                           "https://www.youtube.com/watch?v=1cfklE3-Kes")  # noqa

i_am_sam = media.Movie("I Am Sam",
                       "https://image.tmdb.org/t/p/original/gr0jLIUd5Os0RAFH9U5iZMpQ5cw.jpg",  # noqa
                       "https://www.youtube.com/watch?v=z_AguDqCBvo")  # noqa

lord_of_war = media.Movie("Lord of War",
                          "https://image.tmdb.org/t/p/original/nwPUI9WlYtDmE5VO6eEFCfrNXWl.jpg",  # noqa
                          "https://www.youtube.com/watch?v=AXgyoER0aRc")  # noqa

anger_management = media.Movie("Anger Management",
                               "https://image.tmdb.org/t/p/original/wsrZrb2Ng3eO4TYmeBufwdKeC3a.jpg",  # noqa
                               "https://www.youtube.com/watch?v=1Gl2kVUsy2M")  # noqa

carlitos_way = media.Movie("Carlito's Way",
                           "https://image.tmdb.org/t/p/original/tGPqPHuOCbyFxwllrYgKkPDu9xB.jpg",  # noqa
                           "https://www.youtube.com/watch?v=omqsrminbfs")  # noqa

_88_minutes = media.Movie("88 Minutes",
                          "https://image.tmdb.org/t/p/original/b5d3iWimQXvjAx9Grjuk912DSij.jpg",  # noqa
                          "https://www.youtube.com/watch?v=zUCd805JDJk")  # noqa

the_matrix = media.Movie("The Matrix",
                         "https://image.tmdb.org/t/p/original/hEpWvX6Bp79eLxY1kX5ZZJcme5U.jpg",  # noqa
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")  # noqa

training_day = media.Movie("Training Day",
                           "https://image.tmdb.org/t/p/original/sDT2biSB7wzBJdXq9o3ldr7VfvY.jpg",  # noqa
                           "https://www.youtube.com/watch?v=gKTVQPOH8ZA")  # noqa

the_book_of_eli = media.Movie("The Book of Eli",
                              "https://image.tmdb.org/t/p/original/qL3FnEug9DyBcaBXVb0oT3DJMJu.jpg",  # noqa
                              "https://www.youtube.com/watch?v=yAQcwKY0Dik")  # noqa

rec = media.Movie("[REC]",
                  "https://image.tmdb.org/t/p/original/lLSXs26iZe0aIzYrobr3FruUG36.jpg",  # noqa
                  "https://www.youtube.com/watch?v=YQUkX_XowqI")  # noqa

# Creates the list of movies
movies = {
    the_butterfly_effect, jurassic_park, the_grudge,
    big_mommas_house, the_exorcist, i_am_sam, lord_of_war,
    anger_management, carlitos_way, _88_minutes, the_matrix,
    training_day, the_book_of_eli, rec
}

# Opens the movies page using default web browser
fresh_tomatoes.open_movies_page(movies)
