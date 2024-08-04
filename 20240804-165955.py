import time
from threading import Thread

lyrics = [
    {"text": "Cause I'll be waiting for your love", "speed": 0.08},
    {"text": "Let's fly away together", "speed": 0.07},
    {"text": "Let's get this dream forever", "speed": 0.05},
    {"text": "Let's dance like we're in heaven", "speed": 0.06},
    {"text": "Just give me your sweet love", "speed": 0.06},
    {"text": "Let's fly away together", "speed": 0.08},
    {"text": "Let's get this dream forever", "speed": 0.08},
    {"text": "Let's dance like we're in heaven", "speed": 0.08},
    {"text": "Just give me your sweet love", "speed": 0.06},
]

delays = [0.9, 2.0, 3.7, 5.4, 7.1, 8.8, 10.5, 12.2, 13.9]

def type_lyrics():
    for i in range(len(lyrics)):
        lyric = lyrics[i]
        delay = delays[i] - delays[i - 1] if i > 0 else delays[i]
        time.sleep(delay)
        for char in lyric['text']:
            print(char, end='', flush=True)
            time.sleep(lyric['speed'])
        print()

if __name__ == "__main__":
    type_lyrics()