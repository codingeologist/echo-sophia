"""CLI module"""
import typer
from EchoSophia.utils import (
	_download_audio,
	_transcription,
	_extract_wisdom
)
app = typer.Typer()


@app.command(name="download")
def download(url: str):
    """
    download audio from YouTube URL
    the downloaded media is in *.webm format
    """
    _download_audio(url=url)


@app.command(name="transcribe")
def transcribe(source: str, output: str = "transcribed.json", chunk: bool = False):
    """
    transcribe audio *.wav file
    for large audio files, the data is split into
    30 minute segments for ease of processing and
    for upload to the model
    """
    _transcription(in_file=source, out_file=output, chunked=chunk)


@app.command(name="extract")
def extract(in_file: str, output: str = "extracted.md"):
    """extract wisdom from audio transcripts"""
    _extract_wisdom(in_file=in_file, out_file=output)


if __name__ == "__main__":

    app()
