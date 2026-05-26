from faster_whisper import WhisperModel
from cleaner import clean_text


MODEL_SIZE = "medium"


model = WhisperModel(
    MODEL_SIZE,
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path: str):

    segments, info = model.transcribe(
        audio_path,
        language="es",
        beam_size=5,
        vad_filter=True
    )

    transcript = []

    for segment in segments:

        text = clean_text(segment.text)

        transcript.append({
            "start": round(segment.start, 2),
            "end": round(segment.end, 2),
            "text": text
        })

    metadata = {
        "language": info.language,
        "language_probability": info.language_probability,
        "model": MODEL_SIZE
    }

    return transcript, metadata