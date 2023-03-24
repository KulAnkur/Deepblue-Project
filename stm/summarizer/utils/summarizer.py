from transformers import pipeline

class Summarizer:

    def __init__(self) -> None:
        self.summarizer = pipeline("summarization")

    def summarize(self, article:list, max_length:float = 0.70, min_length:float = 0.30) -> str:
        '''
        Function for summarizing an article
        :param article: list of strings of maximum length 512, all the string will be used to generate the summary.
        :param max_length: maximum percentage of length of the summary
        :param min_length: minimum percentage of length of the summary  
        :return: summary text
        '''
        summary = ''
        for a in article:
            len_a = len(a.split())
            s = self.summarizer(a, max_length=int(len_a*max_length), min_length=int(len_a*min_length), do_sample=False)
            summary += s[0]['summary_text']
        return summary
