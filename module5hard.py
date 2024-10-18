
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def video_info(self):
        return self.title, self.duration, self.time_now, self.adult_mode

class UrTube:

    def __init__(self):
        self.current_user = []
        self.users = [['', '', 0]]
        self.videos = []

    def register(self, nickname, password, age):
        if not any(i[0] == nickname for i in self.users):
            user = (nickname, password, age)
            self.current_user = user
            self.users.append(user)
            return user, self.users
        else:
            print(f'User with {nickname} already exists!')

    def log_in(self, nickname, password):
        if [nickname, password] in UrTube.users:
            self.current_user = nickname, password

    def log_out(self):
        self.current_user = None
        return self.current_user

    def add(self, *args):
        for i in args:
            if not i in self.videos:
                self.videos.append(i)

    def ur_info(self):
        return self.videos

    def get_videos(self, word):
        movies = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                movies.append(i.title)
        return movies

    def watch_video(self, title):
        if self.current_user:
            for i in self.videos:
                if title in i.title:
                    if i.adult_mode:
                        if self.current_user[2] >= 18:
                            for j in range(i.duration):
                                sleep(1)
                                print(j + 1, end=" ")
                            print('End of movie!')
                        else:
                            print('You are below 18, please leave the page')
                    else:
                        for j in range(i.duration):
                            sleep(1)
                            print(j + 1, end=" ")
                        print('End of movie!')
        else:
            print('Please login')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 3, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user[0])

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')




