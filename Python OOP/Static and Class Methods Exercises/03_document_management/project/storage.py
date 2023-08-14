from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id:int, new_name: str):
        try:
            category = next(filter(lambda c: c.id == category_id, self.categories))
            category.edit(new_name)
        except StopIteration:
            pass

    def edit_topic(self, topic_id:int, new_topic: str, new_storage_folder: str):
        try:
            topic = next(filter(lambda t: t.id == topic_id, self.topics))
            topic.edit(new_topic, new_storage_folder)
        except StopIteration:
            pass

    def edit_document(self, document_id: int, new_file_name: str):
        try:
            document = next(filter(lambda d: d.id == document_id, self.documents))
            document.edit(new_file_name)
        except StopIteration:
            pass

    def delete_category(self, category_id: int):
        try:
            category = next(filter(lambda c: c.id == category_id, self.categories))
            self.categories.remove(category)
        except StopIteration:
            pass

    def delete_topic(self, topic_id: int):
        try:
            topic = next(filter(lambda t: t.id == topic_id, self.topics))
            self.topics.remove(topic)
        except StopIteration:
            pass

    def delete_document(self, document_id: int):
        try:
            document = next(filter(lambda d: d.id == document_id, self.documents))
            self.documents.remove(document)
        except StopIteration:
            pass

    def get_document(self, document_id: int):
        try:
            document = next(filter(lambda d: d.id == document_id, self.documents))
            return document.__repr__()
        except StopIteration:
            pass

    def __repr__(self):
        result = []

        for doc in self.documents:
            result.append(doc.__repr__())

        return "\n".join(result)

