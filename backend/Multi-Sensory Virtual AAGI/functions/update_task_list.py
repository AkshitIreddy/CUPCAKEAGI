import json
from datetime import datetime
import os
from dotenv import load_dotenv

# load the environment variables from the .env file
load_dotenv()

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")

def update_task_list_function(well_defined_task, id):
    """
    Updates a task list with a new task.
    Args:
      well_defined_task (str): The task to add to the list.
      id (int): The ID of the task.
    Side Effects:
      Writes the updated task list to a JSON file.
    Returns:
      None
    Examples:
      >>> update_task_list_function("Clean the kitchen", 1)
      None
    """
    dir_path = STATE_DIR
    # load the JSON file
    with open(os.path.join(dir_path, "task_list.json"), 'r') as f:
        data = json.load(f)

    # create a new task
    new_task = {
        "id": id,
        "task": well_defined_task,
        "task_created_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # insert the new task into the list of tasks
    data['tasks'].append(new_task)

    # save the updated JSON file
    with open(os.path.join(dir_path, "task_list.json"), 'w') as f:
        json.dump(data, f, indent=2)