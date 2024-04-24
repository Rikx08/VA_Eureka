import vosk
import sys
import sounddevice as sd
import queue
import json
model_en = vosk.Model("model_en")
model_ru = vosk.Model("model_ru")
samplerate = 16000
device = 1

q = queue.Queue()


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=1000, device=device, dtype='int16',
                           channels=1, callback=q_callback):

        rec_ru = vosk.KaldiRecognizer(model_ru, samplerate)
        # rec_en = vosk.KaldiRecognizer(model_en, samplerate)

        while True:
            data = q.get()
            if rec_ru.AcceptWaveform(data):
                result_ru = json.loads(rec_ru.Result())["text"]
                callback(result_ru)
            # if rec_en.AcceptWaveform(data):
            #     result_en = json.loads(rec_en.Result())["text"]
            #     callback(result_en)
