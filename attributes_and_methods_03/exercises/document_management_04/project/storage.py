"""
Class Storage
Upon initialization the class Storage will not receive any parameters.
It should have 3 attributes: categories (empty list), topics (empty list), documents (empty list).
The class should have the following methods:
    • add_category(category:Category) – add the category if it does not exist
    • add_topic(topic:Topic) – add the topic if it does not exist
    • add_document(document:Document) – add the document if it does not exist
    • edit_category(category_id: int, new_name:str) – edit the name of the category with the provided id
    • edit_topic(topic_id: int, new_topic: str, new_storage_folder: str) – edit the topic with the given id
    • edit_document(document_id: int, new_file_name: str) – edit the document with the given id
    • delete_category(category_id) – delete the category with the provided id
    • delete_topic(topic_id) – delete the topic with the provided id
    • delete_document(document_id) – delete the document with the provided id
    • get_document(document_id) – return the document with the provided id
    • __repr__() – returns a string representation of each document on separate lines
"""
class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self. documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        category = [category for category in self.categories if category.id == category_id][0]
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name:str):
        document = [document for document in self.documents if document.id == document_id][0]
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [category for category in self.categories if category.id == category_id][0]
        self.categories.remove(category)


    def delete_topic(self, topic_id):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [document for document in self.documents if document.id == document_id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        return [document for document in self.documents if document.id == document_id][0]

    def __repr__(self):
        return "\n".join([d.__repr__() for d in self.documents])

from attributes_and_methods_03.exercises.document_management_04.project.category import Category
from attributes_and_methods_03.exercises.document_management_04.project.document import Document
#from attributes_and_methods_03.exercises.document_management_04.project.storage import Storage
from attributes_and_methods_03.exercises.document_management_04.project.topic import Topic

#
c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
