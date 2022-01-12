from flask import Flask, request
# JWT 사용을 위한 SECRET_KEY 정보가 들어있는 파일 임포트
from config import Config
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.favorite import FavoriteListResource, FavoriteResource

from resources.login import UserLoginResource
from resources.logout import UserLogoutResource
from resources.movie import MovieListResource, MovieRealtimeRecommResource, MovieRecommResource, MovieSearchResource
from resources.register import UserRegisterResource
from resources.review import ReviewResource
from resources.user import UserInfoResource

from resources.logout import jwt_blacklist


app = Flask(__name__)


# 환경변수 셋팅
app.config.from_object(Config)

# JWT 토큰 만들기
jwt = JWTManager(app)



@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

api.add_resource( UserRegisterResource, '/api/v1/user/register')
api.add_resource(UserLoginResource, '/api/v1/user/login')
api.add_resource(UserLogoutResource, '/api/v1/user/logout')
api.add_resource(UserInfoResource, '/api/v1/user/me')

# movie
api.add_resource(MovieListResource, '/api/v1/movie')
api.add_resource(MovieSearchResource , '/api/vi/movie/search')
api.add_resource(ReviewResource, '/api/v1/movie/review')

# favorite
api.add_resource(FavoriteResource, '/api/v1/favorite/<int:movie_id>')
api.add_resource(FavoriteListResource, '/api/v1/favorite')

# movie recommand
api.add_resource(MovieRealtimeRecommResource, '/api/v1/movie/recommadation')


if __name__ == "__main__" :
    app.run()