"""main module"""
import os
import json
import argparse
from EchoSophia.audio import Audio
from EchoSophia.chat import LeChat
from EchoSophia.prompting import PromptEng


def _download_audio(url: str) -> None:
    """download a YT video URL to a local file"""

    print("downloading audio...")
    Audio.download(url=url)


def _transcription(out_file: str):
    """transcribe audio chunk files"""

    print("transcribing audio...")
    lechat = LeChat()
    transcriptions = {}
    for root, dirs, files in os.walk("chunks/wednesday_15_july/s2"):
        for file in sorted(files):
            file_path = os.path.join(root, file)

            try:
                transcriptions[file_path] = lechat.transcribe_audio(file_path)
                total_tokens = transcriptions[file_path]["usage"]["total_tokens"]
                total_duration = transcriptions[file_path]["usage"]["prompt_audio_seconds"]
                print(f"{file_path} transcribed tokens: {total_tokens} duration: {total_duration}s")
            except Exception as ex:
                print(f"error transcribing {file_path}: {ex}")
                transcriptions[file_path] = {"error": f"{ex}"}

    print("saving file...")
    with open(f"{out_file}", "w", encoding="utf-8") as file:
        json.dump(transcriptions, file, indent=4, ensure_ascii=False)
    print("audio transcribed!")
    print("file saved!")


def _extract_wisdom(filename: str) -> None:
    """extract key points from transcribed audio text"""

    print("creating prompt...")
    prompt = PromptEng.data_transform(filename=filename)

    print("gathering insights...")
    lechat = LeChat()
    data = lechat.chat_completion(prompt=prompt)

    print("saving results...")
    content = data["choices"][0]["message"]["content"]
    with open(f"{filename}.md", "w", encoding="utf-8") as md_file:
        md_file.write(content)


def main():
    """main loop"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--download", help="download url")
    parser.add_argument("-t", "--transcribe", help="transcribe audio")
    parser.add_argument("-e", "--extract", help="extract wisdom")
    args = parser.parse_args()

    if args.download:
        _download_audio(url=args.download)
    elif args.transcribe:
        _transcription(out_file=args.transcribe)
    elif args.extract:
        _extract_wisdom(filename=args.extract)
    else:
        print("Invalid argument specified!")


if __name__ == "__main__":

    main()
