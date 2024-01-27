import os
from typing import Any
import pathlib
import firebase_admin
from firebase_admin import credentials, firestore, storage


class Firebase:
    firebase_service_path: str = ""
    authentication_path: str = ""
    db: Any = None

    def create_firebase_admin_if_not_exist(self):
        """
        Create the firebase admin
        """
        try:
            cred = credentials.Certificate(self.authentication_path)
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
            self.firestore = firestore.client() # client side
        except Exception as e:
            print("firebase auth", e)
            # critical_failure_email(title="Firebase Authentication Error", body=f"Error: {e}")

    def __init__(self):
        """
        Set up and connect the firebase connection
        """
        # Set up the root for private service key
        current_file_path = pathlib.Path(os.path.abspath(__file__))  # Absolute path
        file_dir = current_file_path.parent.parent.parent.parent.parent  
        credentials_parameter = ['credentials', 'serviceAccountKey.json'] # change the directory by then
        default_authentication_path = pathlib.Path(file_dir).joinpath(*credentials_parameter)
        self.authentication_path = os.getenv("FIREBASE_CREDENTIAL", default_authentication_path)

        # Create firebase client
        self.create_firebase_admin_if_not_exist()

    def test(self):
        self.create_firebase_admin_if_not_exist()
        username = 'user1'
        collection_type = ['user_info', 'question']

        data = {
            'password': 'aa',
            'college': 'Engineering',
            'rank': '1'
        }
        score = {
            'score': 9
        }
        quest = {
            'A': 'aa',
            'B': 'aa',
            'C': 's',
            'D': 'cs',
            'Answer': 'ss'
        }

        # add new
        self.firestore.collection('User').document(username).collection(collection_type[0]).document('detail').update(data)

    def insert_LLM_generate_question(self, username, input):
        """
        Insert the multiple choice question and the answer
        :input: {'Question Title': {'A': 'bla bla', 'B': 'blab blab'..., 'D': 'blad blad', 'Answer': 'A' }}
        """
        question_title = list(input.keys())[0]

        question_ref = (self.firestore.collection('User').
                        document(username).collection('question').
                        document(question_title))

        question_data = list(input.values())[0]

        question_ref.set(question_data) # Rewrite the old one, only the latest question will be shown

    def retrieve_LLM_generate_question(self, username, question_name) -> dict:
        """
        Retrieve the multiple choice question and the answer
        :return: dict{str: dict{str: str}}
        Example: {'Question Title': {'A': 'bla bla', 'B': 'blab blab'..., 'D': 'blad blad', 'Answer': 'A' }, ... }
        """
        question_ref = (self.firestore.collection('User').
                        document(username).collection('question').
                        document(question_name))

        question_data = question_ref.get()

        if question_data.exists:
            return question_data.to_dict()
        else:
            error = 'Document does not exist'
            print(error)

    def insert_user_info(self, input_json):
        """
        Insert registration info of each user
        :input: {"username": "user input", "password": "user input", "collegeName": "user input"}
        """
        username = input_json['username']
        user_data = {"password": input_json['password'], "collegeName": input_json['collegeName']}

        user_info_ref = (self.firestore.collection('User').
                         document(username).collection('user_info').
                         document('detail'))

        user_info_ref.set(user_data)

    def retrieve_user_info(self, username: str):
        """
        Retrieve the specific user info according to the pass in username
        :return: dict{'password': 'xxx', 'college': 'Engineering'}
        """
        
        user_info_ref = (self.firestore.collection('User').
                         document(username).collection('user_info').
                         document('detail'))
        
        user_info = user_info_ref.get().to_dict()
        
        del user_info['collegeName']
        
        return user_info
        
        
    def insert_user_score(self, username: str):
        """
        Insert the updated score of each user base on username
        :input: int
        """
        pass
    def retrieve_user_score(self, username: str):
        """
        Retrieve the specific user score
        :return: int
        """
        pass
    def insert_ranklist(self):
        """
        Insert each rank with username and correspond score in an up to down sequence
        :input:
            1 -> {'username': 'bla bla', ''score': 100}
            2 -> {'username': 'bla blaaa', ''score': 90} ...
        """


if __name__ == "__main__":
    data_processor = Firebase()
    data_processor.test()

    # def insert_LLM_generate_question(self, username, input):
    username = 'jackson'
    input = {'Question Title': {'A': 'bla bla', 'B': 'blab blab', 'C': 'aasd', 'D': 'blad blad', 'Answer': 'A' }}
    data_processor.insert_LLM_generate_question(username, input)

    # def retrieve_LLM_generate_question(self, username, question_name):
    username = 'jackson'
    question_title = 'Question Title'
    question_data = data_processor.retrieve_LLM_generate_question(username, question_title)
    print(question_data)
    # Output: {'A': 'bla bla', 'D': 'blad blad', 'C': 'aasd', 'B': 'blab blab', 'Answer': 'A'}

    # def insert_user_info(self):
    input_json = {"username": "jackson", "password": "jacksonssss", "collegeName": "CAS"}
    data_processor.insert_user_info(input_json)
    
    # def retrieve_LLM_generate_question(self, username, question_name):
    username = 'jackson'
    user_info = data_processor.retrieve_user_info(username)
    print(user_info)
    # Output: 
