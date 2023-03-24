# from flair.data import Sentence
# from flair.models import SequenceTagger

# class POSTagger:

#     def __init__(self) -> None:
        
#         self.tagger = SequenceTagger.load('flair/pos-english-fast')

#     def tag(self, text):
#         sentence = Sentence(text)
#         self.tagger.predict(sentence)
#         # {'text': 'I love you', 'labels': [{'value': 'PRP', 'confidence': 0.9999551773071289}, {'value': 'VBP', 'confidence': 0.9997469782829285}, {'value': 'PRP', 'confidence': 0.9999996423721313}], 'entities': []}
#         return sentence.to_dict()

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import pipeline

class ActionPointClassifier:

    def __init__(self, path="summarizer/huggingface_models/action_point_classifier") -> None:
        self.model = AutoModelForSequenceClassification.from_pretrained(path + "/model")
        self.tokenizer = AutoTokenizer.from_pretrained(path + "/tokenizer")
        self.pipeline = pipeline("text-classification", model=self.model, tokenizer=self.tokenizer)

    def get_action_points(self, meeting):
        '''
        :param meeting: object of class meeting or it's chlid class
        '''
        data = []
        action_points = []


        if isinstance(meeting, str):
            sentence = meeting.split(".")
            for s in sentence:
                if len(s) > 15:
                   data.append(s)

        else:
            for i in meeting.meeting:
                data.append(i.statement)
        
        preds = self.pipeline(data)

        for i, pred in enumerate(preds):
            if pred['label'] == "LABEL_1":
                action_points.append(data[i])

        return action_points
