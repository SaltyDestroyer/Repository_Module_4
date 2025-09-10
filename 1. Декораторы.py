# Задание 1

from datetime import datetime
import requests

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f"Function completed in "
              f"{execution_time.seconds}s {milliseconds}ms")
        return result
    return wrapper

@measure_execution_time
def request_response():
    response = requests.get('https://google.com')

    if response.status_code == 200:
        print('Запрос выполнен успешно')
    else:
        print('Произошла ошибка:', response.status_code)

request_response()

# Задание 2

def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get('role') != 'admin':
            raise PermissionError("Доступ запрещен.")
        return func(user, *args, **kwargs)
    return wrapper

@requires_admin
def delete_user(user, username_to_delete):
    return f"User {username_to_delete} has been deleted by {user['username']}."

admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}

print(delete_user(admin_user, 'Charlie'))
print(delete_user(regular_user, 'Charlie'))