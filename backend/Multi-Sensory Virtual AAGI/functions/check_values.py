import os
import random
from dotenv import load_dotenv

# load the environment variables from the .env file
load_dotenv()

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")

def check_values_function():
    # define the path to the directory where the text files are stored
    dir_path = STATE_DIR

    # open the text files and read the values
    curiosity = float(open(os.path.join(dir_path, "curiosity.txt")).read())
    creativity = float(open(os.path.join(dir_path, "creativity.txt")).read())
    fear = float(open(os.path.join(dir_path, "fear.txt")).read())
    happiness = float(open(os.path.join(dir_path, "happiness.txt")).read())
    sadness = float(open(os.path.join(dir_path, "sadness.txt")).read())
    anger = float(open(os.path.join(dir_path, "anger.txt")).read())

    # check if all values are 0
    if curiosity == 0 and creativity == 0 and fear == 0 and happiness == 0 and sadness == 0 and anger == 0:
        # generate random values between 0 and 1 but keep happiness, curiosity, and creativity high and remaining low
        curiosity = random.uniform(0.7, 1)
        creativity = random.uniform(0.7, 1)
        fear = random.uniform(0, 0.3)
        happiness = random.uniform(0.7, 1)
        sadness = random.uniform(0, 0.3)
        anger = random.uniform(0, 0.3)

        # write the new values back to the text files
        with open(os.path.join(dir_path, "curiosity.txt"), "w") as f:
            f.write(str(curiosity))
        with open(os.path.join(dir_path, "creativity.txt"), "w") as f:
            f.write(str(creativity))
        with open(os.path.join(dir_path, "fear.txt"), "w") as f:
            f.write(str(fear))
        with open(os.path.join(dir_path, "happiness.txt"), "w") as f:
            f.write(str(happiness))
        with open(os.path.join(dir_path, "sadness.txt"), "w") as f:
            f.write(str(sadness))
        with open(os.path.join(dir_path, "anger.txt"), "w") as f:
            f.write(str(anger))

        print("New values have been written to the Emotion files.")
    else:
        print("Values in the Emotion files are not all 0.")