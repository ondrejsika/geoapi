import os

settings_path = os.environ.get("GEOAPI_SETTINGS_MODULE", None)
if settings_path:
    try:
        settings = __import__(settings_path)
    except ImportError:
        exit("Error (3): missing `settings` file")
else:
    settings = None


try:                    PG_TABLE = getattr(settings, "PG_TABLE")
except AttributeError:  exit("Error (1): missing `PG_TABLE` configuration in `settings`")

try:                    PG_DATABASE = getattr(settings, "PG_DATABASE")
except AttributeError:  exit("Error (1): missing `PG_DATABASE` configuration in `settings`")

try:                    PG_USER = getattr(settings, "PG_USER")
except AttributeError:  exit("Error (2): missing `PG_USER` configuration in `settings`")


PG_HOST = getattr(settings, "PG_HOST", "127.0.0.1")
PG_PASSWORD = getattr(settings, "PG_PASSWORD", None)


HTML_INDEX = "<h1>GeoAPI</h1>"
HTML_400_BAD_REQUEST = "<h1>400 Bad Request</h1>"
HTML_404_NOT_FOUND = "<h1>404 Not Found</h1>"
HTML_FOOTER = """
<hr>
<p>2013 (c) <a href="http://ondrejsika.com">Ondrej Sika</a>, <a href="http://kolovsky.cz">Frantisek Kolovsky</a>, Source on <a href="https://github.com/ondrejsika/geoapi">GitHub</a></p>
"""


import psycopg2

PG_CONNECTION = psycopg2.connect(
    user=PG_USER,
    database=PG_DATABASE,
    password=PG_PASSWORD,
    host=PG_HOST,
)