# EchoSophia

![EchoSophia](docs/hero_image.jpg)

---

### _From speech to wisdom_

---

## Installation

```bash
uv venv venv
source venv/bin/activate
uv pip install -e .
```

## Usage

- Download audio from YouTube URL

```bash
echosophia download <"YOUTUBE_URL">
```

- Transcribe audio *.wav file

```bash
echosophia transcribe <"AUDIO_FILE"> # --output transcribed.json
echosophia transcribe <"chunks/"> --chunk # transcribe split chunks of a larger audio file
```

- extract "wisdom" summary from transcripts

```bash
echosophia extract <"TRANSCRIPT.json"> <"OUTPUT.md">
```

## Convert to WAV

```bash
ffmpeg -i "<FILENAME>.webm" -acodec pcm_s16le -ar 44100 -ac 1 "<filename>.wav"
```

## Split to chunks

```bash
ffmpeg -i "<FILENAME>.wav" \
       -f segment \
       -segment_time 00:30:00 \
       -reset_timestamps 1 \
       "<FILENAME_PART>_chunk_%03d.wav"
```

## Chunk validation

```bash
for f in chunks/<DATE>/<ROOM>/europython_2026_<ROOM>_<DATE>_chunk_*.wav; do echo -n "$f: "; ffprobe -v error -show_entrie
s format=duration -of csv=p=0 "$f"; done
```

## Development tasks

[TODO](TODO.md)

## References

- MistralAI Le Chat was used as an assistant to lookup API and SDK usage in the docs and help guide the programming when encountering an error.

- The hero image/logo was generated using MistralAI's LeChat.

- The `extract_wisdom` prompt was modified from the original in danielmiessler's `Fabric`, an open-source framework for augmenting humans using AI.
