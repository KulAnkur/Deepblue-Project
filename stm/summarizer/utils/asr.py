from transformers import Wav2Vec2Tokenizer, Wav2Vec2ForCTC
import librosa as lb
import torch

class ASR:
    '''
    Class for Automatic Speech Recognition
    '''
    
    def __init__(self, model: str = 'facebook/wav2vec2-base-960h') -> None:
        self.tokenizer = Wav2Vec2Tokenizer.from_pretrained(model)
        self.model = Wav2Vec2ForCTC.from_pretrained(model)

    def recognize(self, audio_file: str) -> str:
        '''
        Method for generating text from speech in audio file.

        :param audio_file: path to audio_file in .wav format
        :return: string from speech recognition
        '''

        waveform, rate = lb.load(audio_file, sr = 16000)
        input_values = self.tokenizer(waveform, return_tensors='pt').input_values

        logits = self.model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.tokenizer.batch_decode(predicted_ids)

        return transcription
