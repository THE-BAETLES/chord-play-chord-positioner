import dotenv
from fastapi import FastAPI
import os
from services.BeatService import BeatService

dotenv.load_dotenv()
listen_port = os.environ.get("SERVER_PORT")
output_midi_save_path = os.environ.get("OUTPUT_MIDI_SAVE_PATH")
app = FastAPI()

@app.get('/beat')
async def beat(wavPath: str) -> str:
    wav_path: str = wavPath
    beat_service = BeatService(wav_path)
    bpm, beats = beat_service.start()
    
    response = {
        "bpm": bpm,
        "beats": beats
    }
    return response

if __name__ == "__main__":
    print(f"[Chord Retrieval Engine Server] start listen on {3000}")
    app.run(host='0.0.0.0', port=3000)