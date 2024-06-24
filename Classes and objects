import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.hash_password(password) == self.password


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register (self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь никнеймом {nickname} уже зарегистрирован")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Пользователь {nickname} успешно зарегистрирован и вошел в систему.")

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.check_password(password):
                self.current_user = user
                print(f"Пользователь {login} успешо авторизирован.")
                return True
        print("Неверные данные авторизации.")
        return False

    def log_out(self):
        self.current_user = None
        print(f"Пользователь вышел из системы")

    def add(self,*videos):
        for video in videos:
            if not any(vid.title == video.title for vid in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' успешно добавлено.")
            else:
                print(f"Видео с названием '{video.title}' уже существует и не было добавлено.")

    def get_videos(self, search_word):
        matching_videos = []
        search_word_lower = search_word.lower()
        for video in self.videos:
            if search_word_lower in video.title.lower():
                matching_videos.append(video.title)

        return matching_videos

    def watch_video(self, video_title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == video_title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Начало воспроизведения видео '{video_title}'")
                for second in range(video.duration):
                    time.sleep(1)
                    print(f"Воспроизведение на {second + 1} секунде")
                print("Конец видео")
                return

        print(f"Видео '{video_title}' не найдено")


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode



urtube = UrTube()
video1 = Video("Топ мемы 2023", 10)
video2 = Video("Топ мемы 2024", 180)
video3 = Video("Топ мемы 2023", 60)
video4 = Video("18+", 10, adult_mode=True)
video5 = Video("Основы Python",1000)
urtube.add(video1,video2,video3,video4,video5)

urtube.register("Proks","1312",17)
urtube.register("Proks","1111",11)
urtube.log_in("Proks","1312")
urtube.log_in("Skrop","1111")

urtube.watch_video("18+")
urtube.watch_video("Топ мемы 2023")
urtube.log_out()
urtube.watch_video("Топ мемы 2023")
