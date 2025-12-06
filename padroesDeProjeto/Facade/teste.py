from dataclasses import dataclass

@dataclass
class ABSMultimidia:
    input_path: str
    output_path: str
    output_format: str 
    audio_track: str