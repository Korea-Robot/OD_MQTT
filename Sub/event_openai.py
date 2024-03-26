from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "warning.wav"
response = client.audio.speech.create(
  model="tts-1",
  voice="onyx",
  input="로봇이 계단을 오르고 있습니다.! 절대 뒤에 따라오지 마십시오"
)


response.stream_to_file(speech_file_path)