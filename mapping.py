#!/usr/local/bin/python3
import polyline
import urllib.parse

"""
Turn a bunch of lat longs in to a usable mapbox url with an encoded polyline
https://docs.mapbox.com/api/legacy/static-classic/
This is so we can embed the map in a Wordpress blog.
https://pypi.org/project/polyline/
"""
latlngs = [
    (28.92, -13.66),
    (27.3, -16.61),
    (25.35, -18.3),
    (23.23, -20.13),
    (21.16, -21.96),
    (20, -25),
    (19.23, -27.50),
    (18.71, -33.5),
    (15.33, -38.32),
    (15, -42.8),
    (14.4, -45.02),
    (14.32, -47.2),
    (14.3, -50),
    (14.48, -54.16),
    (14.37, -56.25),
    (14.25, -59.18),
    (14.47, -60.87),
    (14.72, -61.17),
    (15.97, -61.15),
    (15.88, -61.32),
    (15.97, -61.32),
    (15.87, -61.58),
    (15.98, -61.72),
    (16.30, -61.78),
    (17.28, -62.72),
    (17.47, -62.98),
    (17.75, -62.85),
    (18.03, -63.08),
    (22.80, -63.35),
    (25.35, -63.58),
    (28.02, -63.95),
    (30.57, -64.33),
    (33.77, -61.17),
    (34.82, -58.48),
    (35.43, -55.50),
    (36.02, -52.30),
    (36.50, -49.00),
    (36.67, -46.42),
    (37.00, -42.50),
    (37.63, -38.68),
    (38.12, -35.33),
    (39.07, -31.82),
    (39.47, -31.43),
    (39.37, -31.15),
    (38.53, -28.62),
    (38.78, -28.30),
    (39.80, -26.13),
    (40.97, -23.50),
    (42.07, -20.60),
    (42.50, -18.60),
    (44.27, -16.30),
    (44.85, -13.40),
    (44.48, -11.75),
    (43.35, -8.37),
]
path = polyline.encode(latlngs)
encoded = urllib.parse.quote(path)
url = "https://api.mapbox.com/v4/mapbox.streets/path-3+f44-0.8+f44-0({})/auto/800x500.png?access_token=pk.eyJ1IjoiYmVuZWR3YXJkczEiLCJhIjoiY2pzeGRiemp3MDY4czQ0cW9sZHRlZHNtcCJ9.tHBKpUFYmXVEEjzPB5XRbw".format(
    encoded
)
print(url)
"""


auto

curl -g "https://api.mapbox.com/v4/mapbox.streets/path-3+f44-0.5+f44-0(_mooD%7E%7DjrA%7Ek%7BHnd_Qnz%7BJnaiI%7E%60%7DKnldJnhsKnldJ%7EpaF%7EvpQnkuC%7EggN%7EpdB%7Ezrc%40%7EcsS%7Ekl%5Cnm_A%7E%7EiZ%7EdtB%7EqpL%7ErN%7EwhL%7E%7BB%7EzaP)/auto/1000x500.png?access_token=pk.eyJ1IjoiYmVuZWR3YXJkczEiLCJhIjoiY2pzeGRiemp3MDY4czQ0cW9sZHRlZHNtcCJ9.tHBKpUFYmXVEEjzPB5XRbw"

accessToken: 'pk.eyJ1IjoiYmVuZWR3YXJkczEiLCJhIjoiY2pzeGRiemp3MDY4czQ0cW9sZHRlZHNtcCJ9.tHBKpUFYmXVEEjzPB5XRbw'
_mooD~}jrA~k{Hnd_Qnz{JnaiI~`}KnldJnhsKnldJ~paF~vpQnkuC~ggN~pdB~zrc@~csS~kl\nm_A~~iZ~dtB~qpL~rN~whL~{B~zaP

"""
