import json

def find_task_by_id_function(id):
    """
    Finds a task by its ID.
    Args:
      id (int): The ID of the task to find.
    Returns:
      str: The details of the task, or None if not found.
    Examples:
      >>> find_task_by_id_function(1)
      "Task Details\nClean the kitchen\nIMPORTANT TASK CREATION TIME: 2020-07-01T12:00:00"
    """
    with open('state_of_mind/task_list.json') as f:
        data = json.load(f)
        for task in data['tasks']:
            if task['id'] == id:
                response = "Task Details\n" + task['task'] + "\nIMPORTANT TASK CREATION TIME: " + task['task_created_time']
                return response
        return None