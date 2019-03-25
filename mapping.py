from polyline.codec import PolylineCodec
import urllib.parse

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
    ]
path=PolylineCodec().encode(latlngs)
print(urllib.parse.quote(path))

"""
auto

curl -g "https://api.mapbox.com/v4/mapbox.streets/path-3+f44-0.5+f44-0(_mooD%7E%7DjrA%7Ek%7BHnd_Qnz%7BJnaiI%7E%60%7DKnldJnhsKnldJ%7EpaF%7EvpQnkuC%7EggN%7EpdB%7Ezrc%40%7EcsS%7Ekl%5Cnm_A%7E%7EiZ%7EdtB%7EqpL%7ErN%7EwhL%7E%7BB%7EzaP)/auto/1000x500.png?access_token=pk.eyJ1IjoiYmVuZWR3YXJkczEiLCJhIjoiY2pzeGRiemp3MDY4czQ0cW9sZHRlZHNtcCJ9.tHBKpUFYmXVEEjzPB5XRbw"

accessToken: 'pk.eyJ1IjoiYmVuZWR3YXJkczEiLCJhIjoiY2pzeGRiemp3MDY4czQ0cW9sZHRlZHNtcCJ9.tHBKpUFYmXVEEjzPB5XRbw'
_mooD~}jrA~k{Hnd_Qnz{JnaiI~`}KnldJnhsKnldJ~paF~vpQnkuC~ggN~pdB~zrc@~csS~kl\nm_A~~iZ~dtB~qpL~rN~whL~{B~zaP

"""

