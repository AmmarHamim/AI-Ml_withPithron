from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")
client= genai.Client(api_key=api_key)


def output_generation(img,opt):
        if opt == "Hints":
            prompt = """
            This is a screenshot of code with an error.
            Analyze it and give ONLY hints to fix the issue.
            Do not provide full code.
            """
        else:
            prompt = """
            This is a screenshot of code with an error.
            Analyze it and:
            1. Explain the error clearly
            2. Provide the corrected code
            """

        response=client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=[img,prompt]
        )

        return response.text