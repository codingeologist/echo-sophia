# EchoSophia

![EchoSophia](docs/hero_image.jpg)

### _From speech to wisdom_

---

## Rationale

__*Echo*__ (*Ἠχώ*) was a mythological Greek __*Oread*__ (*Ὀρειάς*), a mountain nymph and companion of __*Artemis*__, the goddess of hunting, wildnerness and wild animals. In his __*Metamorphoses*__, Ovid talks about the Jealousy of __*Hera*__ over her husband __*Zeus*__'s many different affairs. Whenever she was about to catch him, __*Echo*__ would distract her with long conversations. When she learned about this, she cursed __*Echo*__, the talkative nymph, that she would only be able to repeat the most recently spoken words of another person.

__*Sophia*__ (*Σοφία*), is the Greek personification of __wisdom__. A practical wisdom of sound judgement and intelligence. Distinct from the *understanding* of __*Logos*__ (*lɒɡɒs*), excellence of character and good judgement of Phronesis (*φρόνησις*) and the spritual knowledge and insight of __*Gnosis*__ (*γνῶσις*). Within the Church, the feminine personification of divine wisdom, __*Ἁγία Σοφία*__ (*Hagía Sophía*), referred to __Christ__, the __Word of God__ or to the __Holy Spirit__, like the dedication of the Eastern Roman empire's Church, in Constantinople.

The culmination of these two concepts, the loquaciousness of __Echo__ with the practical wisdom of __Sophia__, is the fundamental rationale behind building this tool. Large Language Models have been trained on a vast subset of human records, a monument to our species' efforts of understanding (__Logos__), however it remains a facsimile of practical wisdom (__Sophia__). In Plato's __Protagoras__, the wisdom and knowledge was stolen from Olympus by __Prometheus__, to help humanity. Similarly, this tool is being built, to aid the user to use AI to extract knowledge from online sources. However, a word of warning must be heeded, just like __Echo__ (due to the curse by __Hera__) AI/LLMs, are only capable of repeating and regurgitating human speech, writing and knowledge.

The hero image generated for this project, an owl shield with a pen/sword on a field of mountains, is a tribute to __Echo__, the pursuit of __Sophia__ and the watchful gaze of wisdon; __Athena__ (__Minerva__).

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

- The `extract_wisdom` prompt was modified from the original in [danielmiessler's Fabric](https://github.com/danielmiessler/Fabric), an open-source framework for augmenting humans using AI.
