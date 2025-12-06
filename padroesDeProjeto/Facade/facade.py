from teste import ABSMultimidia

class VideoConverter:
    def convert_video(self, input_file, format):
        print(f"-> [VideoConverter]: Lendo arquivo: {input_file}")
        print(f"-> [VideoConverter]: Convertendo para o formato {format}...")
        return f"video_convertido.{format}"

class AudioMixer:
    def mix_audio(self, video_file, track):
        print(f"-> [AudioMixer]: Mixando a trilha '{track}' com o vídeo.")
        return f"video_com_audio_mixado_{video_file}"

class FileSaver:
    def save_file(self, processed_file, output_path):
        print(f"-> [FileSaver]: Salvando o arquivo final em: {output_path}")
        return f"Arquivo '{output_path}/{processed_file}' salvo com sucesso."


class MultimediaFacade:
    def __init__(self):
        self._converter = VideoConverter()
        self._mixer = AudioMixer()
        self._saver = FileSaver()

    def process_media_file(self, multimedia: ABSMultimidia):
        print("\n*** Fachada: Iniciando Processamento de Mídia ***")

        converted_file = self._converter.convert_video(multimedia.input_path, multimedia.output_format)
        mixed_file = self._mixer.mix_audio(converted_file, multimedia.audio_track)
        final_result = self._saver.save_file(mixed_file, multimedia.output_path)

        print("*** Fachada: Processamento Concluído ***")
        return final_result
    
if __name__ == "__main__":
    # CORREÇÃO: Chamando o construtor sem argumentos.
    processor = MultimediaFacade()

    resultado = processor.process_media_file(
        ABSMultimidia(
            input_path="input/video_original.mov",
            output_path="output/final",
            output_format="mp4",
            audio_track="MusicaTema"
        )
    )

    print(f"\nResultado final relatado ao Cliente: {resultado}")