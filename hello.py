import time
import sys

lyrics = [
    "Chal wahan jaate hain, chal wahan jaate hain",
    "Pyar karne chalo hum wahan jaate hain",
    "Chal wahan jaate hain, chal wahan jaate hain",
    "Pyar karne chalo hum wahan jaate hain",
    "Oh, jaate hain",
    "Chal jaate hain"
]

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # delay for each character (like typing effect)
    print()  # new line after each lyric line
    time.sleep(0.8)  # pause before next line
