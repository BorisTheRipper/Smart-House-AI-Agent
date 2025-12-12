from fastapi import APIRouter, UploadFile, File, HTTPException

from server.app.helpers import transcribe_audio_file
from server.app.helpers import analyze_intent

router = APIRouter()


@router.post("/voice-message")
async def transcribe_voice(file: UploadFile = File(...)):
    try:
        transcription = await transcribe_audio_file(file)
        if transcription:
            print(f"Thinking about: {transcription}")
            intent = analyze_intent(transcription)
            print(f"Intent detected: {intent}")
            return {"text": transcription, "intent": intent}
        else:
            raise HTTPException(500, "Too short to transcribe")
    except Exception as e:
        print(f"Transcribe error: {e}")
        raise HTTPException(500, f"Transcribe error: {e}")
