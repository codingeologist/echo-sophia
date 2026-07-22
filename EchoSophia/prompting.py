"""This module transforms model responses to prompts"""
import json


class PromptEng:
    """prompt preparation"""

    @staticmethod
    def data_transform(filename: str) -> str:
        """create prompt for model"""

        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        transcribed_txt = []
        for file_key, transcription in data.items():
            for k, v in transcription.items():
                if k == "text":
                    transcribed_txt.append(v)
        
        full_text = " ".join(transcribed_txt)

        with open("docs/extract_wisdom.md", "r", encoding="utf-8") as file:
            prompt = file.read()
        
        return prompt + full_text