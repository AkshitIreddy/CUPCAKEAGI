from functions.check_values import check_values_function
from functions.determine_task_talk import determine_task_talk_function
from functions.talk import talk_function
from functions.create_task import create_task_function
from functions.update_task_list import update_task_list_function
from functions.start_task_message import start_task_message_function

def main_function(id):
    """
    Main function to determine the action and response.
    Args:
      id (int): The id of the user.
    Returns:
      tuple: A tuple containing the action and response.
    Examples:
      >>> main_function(1)
      ('Talk', 'What can I do for you?')
    """
    check_values_function()
    action = determine_task_talk_function()
    print("Action is " + action)
    if action == "Talk":
        response = talk_function(id)
        print(response)
        return action, response

    well_defined_task = create_task_function()
    print("Task is " + well_defined_task)
    update_task_list_function(well_defined_task, id)
    response = start_task_message_function(well_defined_task)
    print(response)
    return action, response