"""

"""

import requests
import sys
import os



if __name__ == '__main__':
	sys.path.append(os.path.dirname(__file__) + '/../')
"""
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if path not in sys.path:
    sys.path.insert(1, path)
del path
"""

from config import API_URL, TASK_TAIL, TASKS_TAIL
from config import DEFAULT_PASSWORD as PASSWORD 
from config import DEFAULT_USERNAME as USERNAME 
from api_functional_tests.core.task_parser import ResponseParser

class TaskHandler:

	@classmethod
	def get_task(cls, task_id, username, password):

		raw_response = requests.get(url=API_URL+TASK_TAIL+str(task_id), auth=(username, password))
		# print(r.status_code)
		# print(r.text)
		return ResponseParser.get_task(raw_response)

if __name__ == "__main__":
	task_1 = TaskHandler.get_task(1, USERNAME, PASSWORD)
	print (task_1)