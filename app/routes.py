from app import app


# ---------- Задание 1: Простые марщруты ----------
@app.route("/hello")
def hello():
    return "Hello, World!"


@app.route("/info")
def info():
    return "This is an informational page."


# ---------- Задание 2: Динамические маршруты ----------
@app.route("/calc/<a>/<b>")
def calc(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        result = num_a + num_b
        # Если оба числа целые, возвращаем результат как целое число
        if result == int(result):
            result = int(result)
        return f"The sum of {num_a} and {num_b} is: {result}"
    except ValueError:
        return f"Error: '{a}' or '{b}' is not a valid number.", 400


# ---------- Задание 3: Маршрут /reverse, который переворачивает текст
@app.route("/reverse/<text>")
def reverse_text(text):
    if len(text) == 0:
        return "Error: text must contain at least one character.", 400
    return text[::-1]


# ---------- Задание 4: Приветствие с возрастом ----------
@app.route("/user/<name>/<age>")
def user_prfile(name, age):
    try:
        age_int = int(age)
        if age_int <= 0:
            return "Error: age cannot be negative.", 400
        return f"Hello, {name}. You are {age_int} years old."
    except ValueError:
        return f"Error: '{age}' is not a valid integer age.", 400
