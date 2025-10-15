from pydub import AudioSegment

meet = AudioSegment.from_file("sample_data/audio/test_mic.wav")
mic = AudioSegment.from_file("sample_data/audio/test_yt.wav")

mixed = meet.overlay(mic)
mixed.export("./final_mix.wav", format="wav")
print("✅ Combined audio saved!")
