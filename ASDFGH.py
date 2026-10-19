from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()
cnt = 0
@app.get("/")
def f():
    return {"data" : "all done"}

@app.get("/help")
def help():
    global cnt
    cnt += 1
    return {"data" : "/rng - рандомное число, /schedule - расписание, /count - количество команд, /clearcount - очистить счетчик команд, /help - справка о командах"}

@app.get("/rng")
def rng(lower : int, upper : int):
    global cnt
    cnt += 1
    return {"data" : random.randint(lower, upper)}

@app.get("/schedule")
def schedule():
    global cnt
    cnt += 1
    return {"data" : "1 - математика, 2 - математика, 3 - русский, 4 - биология"}

@app.get("/count")
def count():
    global cnt
    cnt += 1
    return {"data" : cnt}

@app.get("/clearcount")
def clearcount():
    global cnt
    cnt = 0
    return {"data" : "done"}
if __name__ == "__main__":
    uvicorn.run("ASDFGH:app", host = "127.0.0.1", port = 8000)
