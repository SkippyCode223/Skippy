import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        
def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)
    
def sing_song():
    lyrics = [
        ("\n""Aduh abang bukan maksudku begitu", 0.09),
        ("Masalah stecu bukan brati tak mau", 0.08),
        ("Jual mahal dikit kan bisa", 0.07),
        ("Coba kasi effortnya saja", 0.07),
        ("Kalo memang cocok bisa datang ke rumah", 0.08),
        ("STECU STECU", 0.14),
        ("Stelan cuek baru malu", 0.12),
        ("Adu ade ini mau juga abang yang rayu""\n", 0.08),
    ]
    
    delays = [0.1, 1.4, 2.2, 3.2 , 4.4, 5.12, 6.15, 7.4, 8.4]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
        
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    sing_song()
