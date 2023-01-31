import json

from flask import Flask, request
from redis import Redis

app = Flask(__name__)
app.config["DEBUG"] = True
redis_cache = Redis(host="cache_redis", port=6379)


@app.route("/", methods=["GET"])
def home():
    return """<h1>Test technique - Sens Critique</h1>
                <p>A flask api.</p>
                <p>2 possible requets :</p> 
                    <p>- GET /product/<movie_id></p>
                    <p>- POST /product/<movie_id></p> 
                    <p>  with the following formdata : {"title": "", "grade": "", "type": ""}</p>"""


@app.route("/product/<movie_id>", methods=["GET"])
def api_get(movie_id):
    if "movies" not in redis_cache:
        return """<h1>Test technique - Sens Critique</h1>
                                <p>Aucun film n'a été noté, base de donnée vide</p>"""

    movies_data = json.loads(redis_cache.get("movies"))
    if movie_id in movies_data.keys():
        return f"""<h1>Test technique - Sens Critique</h1>
                        <p>Identifiant du film - {movie_id}:</p>
                        <p>Titre - {movies_data[movie_id].get("title")}/10</p>
                        <p>Note - {movies_data[movie_id].get("grade")}/10</p>
                        <p>Genre - {movies_data[movie_id].get("type")}/10</p>"""
    else:
        return """<h1>Test technique - Sens Critique</h1>
                        <p>Ce film n'est pas encore noté</p>"""


@app.route("/product/<movie_id>", methods=["POST"])
def api_post(movie_id):
    if "grade" not in request.form.keys():
        return json.dumps(
            {
                "topic": "Test technique Sens critique",
                "ERROR": "Please provide a 'grade' in your request",
            }
        )
    else:
        data = {}
        if "movies" in redis_cache:
            data = json.loads(redis_cache.get("movies"))
        data.update({movie_id: {
            "title": request.form.get("title"),
            "grade": request.form.get("grade"),
            "type": request.form.get("type"),
        }
        })
        redis_cache.set("movies", json.dumps(data))
        return json.dumps(
            {
                "topic": "Test technique Sens critique",
                "new_grade": data,
            }
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
