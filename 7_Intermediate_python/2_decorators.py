# logging decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper 

@logger
def add(a, b):
    return a+b
print(add(3, 7))  




# timing decorator
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start}")
        return result
    return wrapper

@timer
def process():
    for i in range(1000000):
        pass
process()



# authentication decorator
def require_login(func):
    def wrapper(user):
        if not user["logged_in"]:
            return "Access Denied!"
        return func(user)
    return wrapper


@require_login
def dashboard(user):
    return f"Welcome {user['name']}!"

user = {"name": "Hanifa", "logged_in": True}
print(dashboard(user))
