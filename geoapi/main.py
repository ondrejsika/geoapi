import os
import json

from flask import Flask, Response, request

import conf


app = Flask(__name__)

@app.errorhandler(404)
def e404(e):
    return conf.HTML_404_NOT_FOUND+conf.HTML_FOOTER, 404

@app.route("/")
def index():
    return conf.HTML_INDEX+conf.HTML_FOOTER

@app.route("/api/v1/")
def api_v1():
    latitude = request.args.get("latitude", None)
    longitude = request.args.get("longitude", None)

    if not longitude and not latitude:
        return conf.HTML_400_BAD_REQUEST+conf.HTML_FOOTER, 400

    cur = conf.PG_CONNECTION.cursor()

    sql = """
    select level, osm_id, name
    from {table}
    where ST_intersects(st_setsrid(ST_Point({longitude}, {latitude}), 4326), geometry)
    order by level asc
    ;
    """.format(table=conf.PG_TABLE, latitude=latitude, longitude=longitude)
    cur.execute(sql)
    db_data = cur.fetchall()
    cur.close()

    def row(l):
        return {
            "osm_id": l[1],
            "name": l[2],
        }

    data = {
        "country": None,
        "region": None,
        "city": None,
    }

    if len(db_data) == 1:
        data["country"] = row(db_data[0])
    elif len(db_data) == 2:
        data["country"] = row(db_data[0])
        if db_data[1][0] <= 5:
            data["region"] = row(db_data[1])
        else:
            data["city"] = row(db_data[1])
    elif len(db_data) >= 3:
        data["country"] = row(db_data[0])
        data["region"] = row(db_data[1])
        data["city"] = row(db_data[-1])

    return Response(json.dumps(data), mimetype="application/json")
