import pytest
import sys
import os

if __name__ == '__main__':
	sys.path.append(os.path.dirname(__file__) + '/../')

from api_functional_tests.core.task_handler import TaskHandler 
from config import DEFAULT_PASSWORD as PASSWORD 
from config import DEFAULT_USERNAME as USERNAME 

def parametrize_task_id():
	return pytest.mark.parametrize("task_id, expected_title", [
    (1, "Buy groceries"),
    (2, "Learn Python"),
    (3, "Learn Java8")
	], ids=['First task','Second task','Third task'])

class TestGetMethod:

	@classmethod 
	def setup_class(cls):
		cls.task_handler = TaskHandler

	@parametrize_task_id()
	def test_get_task(self, task_id, expected_title):#, task_id, username, password):
		actual_task = self.task_handler.get_task(task_id=task_id, username=USERNAME, password=PASSWORD)		
		print(actual_task)
		assert actual_task.title == expected_title, 'Invalid title'


		# print(task_id)
		# print(expected_title)

if __name__ == "__main__":
	pytest.main([__file__, "-v"])