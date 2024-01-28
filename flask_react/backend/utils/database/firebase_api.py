import os
from typing import Any
import pathlib
import firebase_admin
from firebase_admin import credentials, firestore


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

    def insert_answer(self, username, answer):
        """
        Insert an answer
        :param username:
        :param answer:
        :return:
        """
        question_ref = (self.firestore.collection('User').
                        document(username))

        question_ref.set(answer, merge=True)

    def retrieve_answer(self, username):
        question_ref = (self.firestore.collection('User').
                        document(username))

        user_answer = question_ref.get().get('answer')

        return user_answer


    def insert_image_label(self, username, label):

        image_label_ref = (self.firestore.collection('User').
                        document(username))

        image_label_ref.set(label, merge=True)

    def retrieve_image_label(self, username):
        image_label_ref = (self.firestore.collection('User').
                        document(username))

        image_label = image_label_ref.get().get('image_label')

        return image_label

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
        user_data = {"password": input_json['password'], "collegeName": input_json['collegeName'],
                     "score": "0"}

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
        
    def insert_user_score(self, username: str, score):
        """
        Insert the updated score of each user base on username
        :input: int
        """
        score_data = {'score': score}

        user_info_ref = (self.firestore.collection('User').
                         document(username).collection('user_info').
                         document('detail'))

        # 会覆盖
        user_info_ref.set(score_data, merge=True)

    def retrieve_user_score(self, username: str):
        """
        Retrieve the specific user score
        :return: int
        """
        user_info_ref = (self.firestore.collection('User').
                         document(username).collection('user_info').
                         document('detail'))

        user_score = user_info_ref.get().get('score')

        return user_score

    def retrieve_rankedlist(self):
        colleges_ref = self.firestore.collection('CollegeRank')
        colleges = colleges_ref.stream()

        # Create a list to store tuples of (college_dict, numeric_score) for ordering
        college_data = []

        for college in colleges:
            college_dict = college.to_dict()
            college_dict['college_name'] = college.id  # Add college name to the dictionary

            # Convert college_score to a numerical value
            numeric_score = float(college_dict['college_score'])

            # Append the tuple to the list
            college_data.append((college_dict, numeric_score))

        # Sort the list based on the numeric_score
        sorted_colleges = sorted(college_data, key=lambda x: x[1], reverse=True)

        # Extract the college dictionaries from the sorted list
        sorted_college_dicts = [item[0] for item in sorted_colleges]

        return sorted_college_dicts

    def insert_rankedlist(self):
        """
        Insert each rank with username and correspond score in an up to down sequence
        :input:
            1 -> {'username': 'bla bla', ''score': 100}
            2 -> {'username': 'bla blaaa', ''score': 90} ...
        """
        pass

    # college
    def insert_college_score(self, username, score):
        """
        :param username:
        :param score: dict: {'college_score': score}
        :return:
        """
        college_score = {'college_score': score}
        college_name = self.retrieve_user_college(username)

        college_score_ref = (self.firestore.collection('CollegeRank').
                         document(college_name))

        college_score_ref.set(college_score)

    def retrieve_college_score(self, username):
        college_name = self.retrieve_user_college(username)
        college_score_ref = self.firestore.collection('CollegeRank').document(college_name)

        doc = college_score_ref.get()

        if doc.exists and 'college_score' in doc.to_dict():
            return doc.get('college_score')
        else:
            college_score_ref.set({'college_score': '0'}, merge=True)
            return '0'

    def retrieve_user_college(self, username):

        user_college_ref = (self.firestore.collection('User').
                         document(username).collection('user_info').
                         document('detail'))

        return user_college_ref.get().get('collegeName')



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
    # Output: {'password': 'jacksonssss'}

    # def insert_user_score(self, username: str):
    username = 'jackson'
    score = 7
    data_processor.insert_user_score(username, score)

    # def retrieve_user_score(self, username: str):
    username = 'jackson'
    score = data_processor.retrieve_user_score(username)
    print(score)

    # def insert_answer(self, username, answer):
    username = 'test_user'
    data = {'answer': 'B'}
    data_processor.insert_answer(username, data)

    # def retrieve_answer(self, username):
    username = 'jackson'
    answer = data_processor.retrieve_answer(username)
    print(answer)

    # def insert_image_label(self, username, label):
    username = 'test_user'
    label = {'image_label': 'keyboard'}
    data_processor.insert_image_label(username, label)

    username = 'test_user'
    res = data_processor.retrieve_image_label(username)
    print(res)

    data_processor.retrieve_rankedlist()