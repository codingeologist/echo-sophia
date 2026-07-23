"""This module downloads and processes youtube audio data"""
import sys
import yt_dlp


class Audio:
    """Download audio data to a file"""


    @staticmethod
    def download(url: str) -> None:
        """download a YT video to a file"""

        ydl_options = {
                    "format": "bestaudio/best",
                    "outtmpl": "%(title)s.%(ext)s"
                }

        try:
            with yt_dlp.YoutubeDL(ydl_options) as ydl:
                ydl.download([url])
                sys.stdout.write("downloaded audio successfully...\n")
        except Exception as ex:
            err = f"error downloading audio from {url}: {ex}\n"
            raise ConnectionError(err)
