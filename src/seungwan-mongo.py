from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

database = client.get_database("movies")
movies = database.get_collection("movies")

query = {"rating": {"$gte": 8}}

# results = movies.find(query)

# for movie in results:
#   print(movie)

new_movie = {
  "title": "New movie",
  "director": "ingyun"
}

result = movies.insert_one(new_movie)