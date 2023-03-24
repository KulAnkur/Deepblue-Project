import json
from docx import Document

class Statement:
    '''
    Class to deals with a single statement made by a speaker.
    A Metting consists of a number of Statement by differnt speakers.
    '''

    def __init__(self, speaker: str, statement:str, start_time: str, end_time: str) -> None:
        '''
        :param speaker: Name of the speaker
        :param statement: statement made by the speaker
        :param start_time: time stamp when speaker started speaking
        :param end_time: time stamp when speaker ended speaking
        :return: None
        '''
        self.speaker = speaker
        self.statement = statement
        self.start_time = start_time
        self.end_time = end_time

    @classmethod
    def from_json(cls, json):
        '''
        Method for initiaing the class using dictionary/json.

        :param json: a dictinoary/json containing statement data
        :return: an object of the class 
        '''
        return cls(**json)

    def as_json(self,):
        '''
        Method for returning the statement data as a dictonary/json.
        '''
        return {'speaker': self.speaker,
                'statement': self.statement,
                'start_time': self.start_time,
                'end_time': self.end_time,}


class Meeting:
    '''
    Class to deals with a single meeting.
    A Metting consists of a number of Statement by differnt speakers.
    '''

    def __init__(self, meeting:list, date:str = None) -> None:
        '''
        :param meeting: a list of Statement objects
        :return: None
        '''
        self.meeting = meeting
        self.date = date

    @classmethod
    def from_json(cls, json):
        '''
        Method for initiaing the class using dictionary/json.

        :param json: a dictinoary/json containing statement data
        :return: an object of the class
        ''' 

        meeting_list = []
        for statement_dict in json:
            statement = Statement(**statement_dict)
            meeting_list.append(statement)

        return cls(meeting_list)

    @classmethod
    def from_json_file(cls, file):
        '''
        Method for initiaing the class using json file.

        :param file: path to json file
        :return: an object of the class
        ''' 
        
        with open(file) as f:
            data = json.load(f)

        return cls.from_json(data)


    def save_as_json(self, file) -> None:
        '''
        Method for saving the meeting data as a json file.
        
        :param file: location where the json file has to be created/over-written and saved
        :return: None
        '''
        
        meeting_list = []
        for statement in self.meeting:
            meeting_list.append(statement.as_json())

        with open(file, "w") as f:
            json.dump(meeting_list, f, indent = 4)

    def as_str(self, delimiter:str = " ", include_speaker = True, concat_str:str = " said ", max_len=512) -> str:
        '''
        Method for getting the meeting data as a string.
        Creats a string containing all the statements.
        This string can be used for summarization.

        :param delimiter: used as a seperator betting two statements
        :param include_speaker: to concatenate the speaker name before the statement or not
        :param concat_str: string concatentaed in between speaker and the statement
        :param max_len: maximum number of words a single string can have
        :return: list of string containing all the statements of the meeting
        '''

        meeting_str = ""
        meeting_list = []

        if include_speaker:
            for statement in self.meeting:
                if statement != "":
                    new_str = statement.speaker + concat_str + statement.statement + delimiter
                    if len((meeting_str + new_str).split()) > max_len:
                        meeting_list.append(meeting_str)
                        meeting_str = new_str
                    else:
                        meeting_str += new_str
        else:
            for statement in self.meeting:
                if statement != "":
                    new_str = statement.statement + delimiter
                    if len((meeting_str + new_str).split()) > max_len:
                        meeting_list.append(meeting_str)
                        meeting_str = new_str
                    else:
                        meeting_str += new_str

        if len(meeting_list)== 0:
            meeting_list.append(meeting_str)
        elif meeting_str != meeting_list[-1]:
            meeting_list.append(meeting_str)

        return meeting_list

    def duration(self):
        '''
        Finds the duration of the meeting.

        :return (str): duration of meeting in hours, mins, seconds format
        '''
        
        hour, min, sec = self.meeting[-1].end_time.split(":")
        hour, min, sec = int(hour), int(min), int(float(sec))
        return f"{hour} hours, {min} minutes and {sec} seconds"

    def num_speakers(self):
        '''
        Returns the number of speakers in the meeting.
        returns
        '''
        speakers= []
        for m in self.meeting:
            speakers.append(m.speaker)
        
        return len(set(speakers))



class TeamsMeet(Meeting):
    '''
    Class to deals with a single MicroSoft Teams meeting.
    '''

    def __init__(self, meeting: list, date=None) -> None:
        super().__init__(meeting, date)

    @classmethod
    def from_doc(cls, file):
        '''
        Method for initiaing the class using MS Teams transcript file in .docx format.

        :param file: path to docx file
        :return: an object of the class
        '''

        document = Document(file)

        meeting_list = []

        for para in document.paragraphs:
            lines = para.text.split("\n")
            assert len(lines) == 3 # time, speaker, statement thus len = 3

            start_time, end_time = lines[0].split(" --> ")
            speaker = lines[1]
            statement = lines[2]

            meeting_list.append(Statement(speaker, statement, start_time, end_time))

        return cls(meeting_list)

    @classmethod
    def from_vtt(cls, file):
        '''
        Method for initiaing the class using MS Teams transcript file in .vtt format.

        :param file: path to docx file
        :return: an object of the class
        '''
        raise NotImplementedError()

class GoogleMeet(Meeting):
    def __init__(self, meeting: list, date: str = None) -> None:
        super().__init__(meeting, date)
        raise NotImplementedError()

class ZoomMeet(Meeting):
    def __init__(self, meeting: list, date: str = None) -> None:
        super().__init__(meeting, date)
        raise NotImplementedError
