from datetime import datetime
from transcriber import transcribe_audio
from summarizer import generate_summary
from exporter import (
    save_transcript_txt,
    save_transcript_md,
    save_summary_md,
    save_metadata
)

AUDIO_FILE = "audio/meeting_complete.m4a"


def main():

    total_start = datetime.now()

    print(f"Inicio total: {total_start}")

    # -------------------------
    # TRANSCRIPCIÓN
    # -------------------------

    transcription_start = datetime.now()

    transcript, metadata = transcribe_audio(AUDIO_FILE)

    transcription_end = datetime.now()

    print(
        f"Transcripción completada en: "
        f"{transcription_end - transcription_start}"
    )

    save_transcript_txt(transcript)
    save_transcript_md(transcript)
    save_metadata(metadata)

    # -------------------------
    # SUMMARY
    # -------------------------

    summary_start = datetime.now()

    summary = generate_summary(transcript)

    summary_end = datetime.now()

    print(
        f"Resumen completado en: "
        f"{summary_end - summary_start}"
    )

    save_summary_md(summary)

    # -------------------------
    # TOTAL
    # -------------------------

    total_end = datetime.now()

    print(f"Fin total: {total_end}")

    print(
        f"Duración total: "
        f"{total_end - total_start}"
    )

    print("Proceso completado")


if __name__ == "__main__":
    main()