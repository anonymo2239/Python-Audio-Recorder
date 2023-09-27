import pyaudio
import wave

alperen_filename = "my_record2.wav"
a_chunk = 1250
FORMAT = pyaudio.paInt16
a_channels = 2 #this value can be made 1
a_sample_rate = 44100
a_record_seconds = 5
p = pyaudio.PyAudio()

akis = p.open(format=FORMAT,
                channels=a_channels,
                rate=a_sample_rate,
                input=True,
                output=True,
                frames_per_buffer=a_chunk)

frames = []
print("Kaydediliyor...")
for i in range(int(a_sample_rate / a_chunk * a_record_seconds)):
    data = akis.read(a_chunk)
    frames.append(data)
print("Kayıt bitti.")

akis.stop_stream()
akis.close()

p.terminate()

wf = wave.open(alperen_filename, 'wb')
wf.setnchannels(a_channels)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(a_sample_rate)
wf.writeframes(b"".join(frames))
wf.close()
