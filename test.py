import unittest
from services.BeatService import BeatService
import os
import dotenv
dotenv.load_dotenv()
test_input_wav_path = os.environ.get("INPUT_WAV_PATH")
class BeatGenerateTest(unittest.TestCase):
    def test_beat_generate(self):
        
        print(test_input_wav_path)
        
        service = BeatService(test_input_wav_path)
        bpm, beats = service.start()
        assert len(beats) != 0
        print("bpm = ", bpm)
        print("beats = ", beats)

if __name__ == '__main__':
    unittest.main()