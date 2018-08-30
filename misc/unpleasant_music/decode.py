import wave

if __name__ == '__main__':
    w = wave.open("music.wav", 'rb')
    binary_data = w.readframes(w.getnframes())
    with open('file.rar', 'wb') as f:
        f.write(binary_data)