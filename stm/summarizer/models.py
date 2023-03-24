from django.db import models
from .utils import Summarizer, ASR, ActionPointClassifier

summarizer = Summarizer()
asr = ASR()
action_point_classifier = ActionPointClassifier()
##############################################

# class Summarizer:
#     def __init__(self,):
#         pass
    
#     def summarize(self, data, a, b):
#         return data

# summarizer = Summarizer()

# class ASR():
#     def __init__(self) -> None:
#         pass

#     def recognize(self, data):
#         return data

# asr = ASR()