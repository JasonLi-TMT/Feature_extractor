import tmdbsimple as tmdb

import urllib
import os
from IPython.display import display, HTML, Image


tmdb_connector = tmdb

key_v4 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMWFiOWE2ZTk2MjJmZTI3ZjZkZDJhODEwNjUyMjRmYyIsInN1YiI6IjVhMWJhZGM3YzNhMzY4MGI5YTA1MTFkNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZJUnnEvLnVcXcOAj0T6LFBmhModcy9HbwvDOF-XZfv4'
key_v3 = 'b1ab9a6e9622fe27f6dd2a81065224fc'

tmdb_connector.API_KEY = key_v3


"""
w92", "w154", "w185", "w342", "w500", "w780" is the size of image in the url
"""

tmdb_path = 'http://image.tmdb.org/t/p/w185//'
download_path = "/Users/zishuoli/Doc/project/Feature_extractor/Image/tmdb_movie_poster/"


def tmdb_img_download(id, path_db=tmdb_path, path_download=download_path):
    mov = tmdb.Movies(id)
    info = mov.info()
    title = info['title']
    url_img = path_db + info['poster_path']

    try:
        os.mkdir(path_download + title)
    except:
        pass

    path_download = path_download + title + '/' + str(id) + '.jpg'
    try:
        urllib.request.urlretrieve(url_img, path_download)
    except:
        print("Film {}'s poster is not available'")


def display_images(id, path_db=tmdb_path):

    mov = tmdb.Movies(id)
    info = mov.info()

    img_path = info['poster_path']

    path = path_db + img_path
    images = ''

    images += "<img style='width: 100px; margin: 0px; \
            float: left; border: 1px solid black;' src='%s' />" \
            % path

    display(HTML(images))
