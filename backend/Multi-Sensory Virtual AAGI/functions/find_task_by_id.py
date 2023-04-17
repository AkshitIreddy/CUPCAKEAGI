import json

def find_task_by_id_function(id):
    with open('state_of_mind/task_list.json') as f:
        data = json.load(f)
        for task in data['tasks']:
            if task['id'] == id:
                response = "Task Details\n" + task['task'] + "\nIMPORTANT TASK CREATION TIME: " + task['task_created_time']
                return response
        return None