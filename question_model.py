# Creating a new class in python
class Question:
    # Define an init statement with parameters inside the brackets
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_q = Question("asds", "False")
print(new_q.text)
