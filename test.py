import unittest
from services.BeatService import BeatService
import os
import dotenv
dotenv.load_dotenv()
test_input_wav_path = os.environ.get("")
class BeatGenerateTest(unittest.TestCase):
    def test_beat_generate():
        service = BeatService(test_input_wav_path)
        bpm, beats = service.start()
        
        assert len(bpm) != 0
        
        print("bpm = ", bpm)
        print("beats = ", beats)

if __name__ == '__main__':
    unittest.main()