"""utils module"""
import os
import sys
import json
from EchoSophia.audio import Audio
from EchoSophia.chat import LeChat
from EchoSophia.prompting import PromptEng


def _download_audio(url: str) -> None:
    """download a YT video URL to a local file"""

    sys.stdout.write("downloading audio...\n")
    Audio.download(url=url)


def _transcription(in_file: str, out_file: str, chunked: bool = True):
    """transcribe audio chunk files"""

    sys.stdout.write("transcribing audio...\n")
    lechat = LeChat()
    transcriptions = {}
 
    if chunked:
        for root, dirs, files in os.walk(in_file):
            for file in sorted(files):
                file_path = os.path.join(root, file)
                try:
                    transcriptions[file_path] = lechat.transcribe_audio(file_path)
                    total_tokens = transcriptions[file_path]["usage"]["total_tokens"]
                    total_duration = transcriptions[file_path]["usage"]["prompt_audio_seconds"]
                    msg = f"path: {file_path}\ntranscribed tokens: {total_tokens}\nduration: {total_duration}s\n"
                    sys.stdout.write(msg)
                except Exception as ex:
                    err = f"error transcribing {file_path}: {ex}\n"
                    sys.stdout.write(err)
                    transcriptions[file_path] = {"error": f"{err}"}
                    sys.stdout.write(err)
                    sys.exit(1)
    else:
        try:
            transcriptions[in_file] = lechat.transcribe_audio(in_file)
            total_tokens = transcriptions[in_file]["usage"]["total_tokens"]
            total_duration = transcriptions[in_file]["usage"]["prompt_audio_seconds"]
            msg = f"in_file: {in_file}\ntranscribed tokens: {total_tokens}\nduration: {total_duration}s\n"
            sys.stdout.write(msg)
        except Exception as ex:
            err = f"error transcribing {in_file}: {ex}\n"
            transcriptions[in_file] = {"error": f"{err}"}
            sys.stdout.write(f"{err}")
            sys.exit(1)

    sys.stdout.write("saving file...\n")
    with open(f"{out_file}", "w", encoding="utf-8") as file:
        json.dump(transcriptions, file, indent=4, ensure_ascii=False)
    sys.stdout.write("audio transcribed!\n")
    sys.stdout.write("file saved!\n")


def _extract_wisdom(in_file: str, out_file: str) -> None:
    """extract key points from transcribed audio text"""

    sys.stdout.write("creating prompt...\n")
    prompt = PromptEng.data_transform(filename=in_file)

    sys.stdout.write("gathering insights...\n")
    lechat = LeChat()
    data = lechat.chat_completion(prompt=prompt)

    sys.stdout.write("saving results...\n")
    content = data["choices"][0]["message"]["content"]
    with open(f"{out_file}", "w", encoding="utf-8") as md_file:
        md_file.write(content)
