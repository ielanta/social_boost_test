import requests
import string
from heapq import heappush as insert, heappop as extract_maximum
from random import randint, choice

NUMBER_OF_USERS = 3
MAX_POSTS_PER_USER = 10
MAX_LIKES_PER_USER = 15

URL = 'http://127.0.0.1:8000'


def get_random_string(size):
    return ''.join([choice(string.ascii_letters) for _ in range(size)])


class SocialBot:
    # TODO: use parallel computing
    def __init__(self):
        self.number_of_users = NUMBER_OF_USERS

    def run(self):
        user_priority_q = []
        post_q = []

        for i in range(self.number_of_users):
            username = get_random_string(16)
            user_bot = UserBot(username=username, password='Leo12345!', email=username+'@close.io')
            insert(user_priority_q, (i, user_bot.number_of_posts, user_bot))
            post_q.append(user_bot.posts)

        while user_priority_q and post_q:
            user_bot = extract_maximum(user_priority_q)[-1]
            user_finished = False

            while user_priority_q and not user_finished and post_q and user_bot.number_of_likes:
                posts = post_q.pop()

                if not user_bot.posts.intersection(posts):
                    for _ in range(min([user_bot.number_of_likes, len(posts)])):
                        user_bot.make_like(posts.pop())

                if not post_q:
                    user_finished = True

                if posts:
                    post_q.append(posts)


class UserBot:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        requests.post(URL + '/accounts/register/', {'username': username, 'password': password, 'email': email})
        self.number_of_posts = randint(1, MAX_POSTS_PER_USER)
        self.headers = {'Authorization': self.get_token()}
        self.posts = set()
        self.number_of_likes = MAX_LIKES_PER_USER
        self.make_post()

    def get_token(self):
        response = requests.post(URL + '/api-token-auth/', {'username': self.username, 'password': 'Leo12345!'})
        token = response.json().get('token')
        if not token:
            raise ValueError(f'Please check credentials: username({self.username}) and password')
        return 'JWT ' + response.json()['token']

    def make_post(self):
        for _ in range(self.number_of_posts):
            response = requests.post(URL + '/my/posts/', {'text': get_random_string(128)}, headers=self.headers)
            self.posts.add(response.json()['id'])

    def make_like(self, post_id):
        requests.post(URL + '/my/likes/', {'post': post_id}, headers=self.headers)
        self.number_of_likes -= 1


if __name__ == "__main__":
    sb = SocialBot()
    sb.run()
