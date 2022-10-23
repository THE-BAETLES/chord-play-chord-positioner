import essentia.standard as es
import time

# wav separate csv midi
class BeatService:
    def __init__(self, wav_path):
        self.wav_path = wav_path
    
    def start(self):
        st = time.time()
        print("Beat Detection Start")
        audio = es.MonoLoader(filename=self.wav_path)()
        rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
        bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)
        
        print(f"Beat Detection end in {time.time() - st}s")
        
        return float(bpm), beats.tolist()
        
    
    