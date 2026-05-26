import json
from pathlib import Path


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)



def save_transcript_txt(transcript):

    with open(
        OUTPUT_DIR / "transcript.txt",
        "w",
        encoding="utf-8"
    ) as f:

        for item in transcript:
            line = (
                f"[{item['start']} - {item['end']}] "
                f"{item['text']}"
            )
            f.write(line + "\n")



def save_transcript_md(transcript):

    with open(
        OUTPUT_DIR / "transcript.md",
        "w",
        encoding="utf-8"
    ) as f:

        f.write("# Transcripción\n\n")

        for item in transcript:

            line = (
                f"- **{item['start']}s**: "
                f"{item['text']}"
            )

            f.write(line + "\n")



def save_summary_md(summary):

    with open(
        OUTPUT_DIR / "summary.md",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(summary)



def save_metadata(metadata):

    with open(
        OUTPUT_DIR / "metadata.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(metadata, f, indent=4)