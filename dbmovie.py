from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.axdjt.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta

#영화 '가버나움'의 평점을 찾기
target_movie = db.movies.find_one({'title': '가버나움'})
target_star = target_movie['star']
print(target_star)

#'가버나움'과 같은 평점을 갖고 있는 영화 모두 찾기
movies = list(db.movies.find({'star': target_star}))

for movie in movies:
    print(movie['title'])

# #영화 '법정'의 평점 0점으로 만들기
db.movies.update_one({'title': '법정'}, {'$set': {'star': '0'}})
