"""This module integrates with the MistralAI API"""
import os
import sys
from httpx import LocalProtocolError
from mistralai.client import Mistral


class LeChat:
    """MistralAI Client"""

    def __init__(self) -> None:
        """initialise client"""

        self.api_key = os.getenv(key="MISTRAL_API_KEY")
        self.chat_model = os.getenv(key="MISTRAL_MODEL")
        self.transcribe_model = os.getenv(key="VOXTRAL_MODEL")
        self.client = Mistral(api_key=self.api_key)


    def transcribe_audio(self, filename: str) -> dict:
        """generate transcriptions from file"""

        sys.stdout.write(f"transcribing audio: {filename}...\n")
        try:
            with open(f"{filename}", "rb") as f:
                response = self.client.audio.transcriptions.complete(
                        model=self.transcribe_model,
                        file={
                            "content": f,
                            "file_name": filename
                            }
                        )

            return response.model_dump()
        except Exception as ex:
            err = f"error transcribing audio: {ex}\n"
            sys.stdout.write(err)
            sys.exit(1)


    def chat_completion(self, prompt: str) -> dict:
        """generate text responses"""

        sys.stdout.write("querying model...\n")
        try:
            chat_response = self.client.chat.complete(
                model=self.chat_model,
                messages = [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return chat_response.model_dump()
        except LocalProtocolError as ex:
            err = f"Forgot the API KEY or model: {ex}\n"
            sys.stdout.write(err)
            sys.exit(1)
