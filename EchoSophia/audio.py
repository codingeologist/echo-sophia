"""This module downloads and processes youtube audio data"""
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
                print("downloaded audio successfully...")
        except Exception as ex:
            print(f"error downloading audio from {url}: {ex}")
