# CUPCAKEAGI

# ✨ Demo



https://user-images.githubusercontent.com/90443032/232546182-19258002-755d-43cc-bfe2-a45179f51be1.mp4



# 🚨 Requirements

Open up a terminal and go to backend/Multi-Sensory Virtual AAGI
```sh
conda create --name aagi python=3.9
conda activate aagi
pip install -r requirements.txt
```

# 🔌 How to use

Open up a terminal and go to backend/Multi-Sensory Virtual AAGI
```sh
uvicorn inference:app
```

Open up another terminal and go to frontend/assistant
```sh
npm run dev
```
Enter your API keys in .env file, You'll need an OPENAI API key, SERPER API key

# 🚀 Features

- 🌐 Access to internet
- 🐶 Upload Images
- 🎵 Upload Audio
- 📹 Upload Video
- 💾 Persistent Memory
- ❤️ Emotions
- 💭 Random Thoughts
- 😴 Dreams
- 📝 Assign & schedule Tasks
- 🧑‍💻 Creat & Run Python Code
- 🧠 GPT-3.5 as the brain

# About

Hey there cupcake lovers🧁❤️! I am excited to introduce you to my latest project, CupcakeAGI!

CupcakeAGI is an agent that aims to mimic human-like behavior and cognitive abilities to assist users in performing various tasks. It's equipped with some sweet🍬 features, including the ability to dream😴, have random thoughts, and perform mental simulations on how to complete a task. Just like how we humans have thoughts floating around our heads, CupcakeAGI has a thought bubble💭 with abstract words.

To make CupcakeAGI more expressive, I've added emotion parameters. This will allow it to interact with users in a more personal way❤️.

One of CupcakeAGI's most impressive features is its ability to accept various forms of sensory data, such as images🐶, videos📹, and audio🎵. Although I haven't implemented smell👃, touch✋ and taste👅 yet, it should be similar to what I did for image, video, and audio. You'll need a function to convert the sensory data to text and then it will get added as a file description for the file which will be used while prompting the model.

CupcakeAGI provides two main features for user interaction: talk and task. The talk feature allows for immediate responses to user queries using tools like search engines, calculators, and translators, making it a real-time problem solver. And who doesn't love a good problem solver🧠, especially when it comes to baking cupcakes🧁?

The task feature is used for completing tasks at a start time or by a deadline. This feature allows for chaining multiple tools together using a natural language task function that converts the output of one tool into the input of another, making different tools compatible with each other. So, whether you need to bake some cupcakes for a birthday party or a cupcake contest, CupcakeAGI is here to help you out!

Overall, I hope you find CupcakeAGI to be a sweet addition to your life. This project was a lot of fun to create, and I'm excited to see where it goes. Thanks for reading, and happy baking!✨

# Why?

- Our brain processes and integrates these sensory inputs to form a coherent perception of the world around us. Similarly, in the realm of artificial intelligence, the ability to process and integrate multisensory data is crucial for building intelligent agents that can interact with humans in a more natural and effective way.

- In recent years, large language models (LLMs) such as ChatGPT and GPT-4 have demonstrated remarkable abilities in generating human-like text based on vast amounts of training data. However, these models are typically limited to working with text and image data and lack the ability to process other types of sensory inputs.

- Beyond the ability to process multisensory data, the human-like LLM agent presented in this paper also exhibits several cognitive abilities that are typically associated with humans. For instance, the agent is equipped with the ability to dream and have random thoughts, which are thought to play important roles in human creativity, memory consolidation, and problem-solving. By incorporating these features into the LLM agent, we aim to create an agent that can assist users in performing tasks in a more natural and effective way and make these agents more human-like.

# Multisensory Data
- Welcome back to the world of cupcakes and baking! We all know that human experience is much more than just text-based interactions. It's not just about reading, but also about experiencing the world with all our senses, including sight, sound, smell, taste, and touch. Similarly, an LLM agent that can work with multisensory data can open up a new world of possibilities for machine learning.

- Instead of missing out on the rich and varied data available through other sensory modalities, we can use neural network architectures that convert various forms of sensory data into text data that the LLM can work with.

- For instance, we can use image captioning models like vit-gpt2 and blip to convert images into text data, which the LLM agent can then process. Similarly, for audio data, audio-to-text models like OpenAI's Whisper can be used to convert audio signals into text data.

- Now, I know what you're thinking: what about videos, smell, taste, and touch? Don't worry, we got you covered! To save computation, we can use one frame per second of video data and use image captioning models to convert each frame into text. The audio track from the video can be separated and transcribed using audio-to-text models, providing the LLM agent with both visual and auditory data.

- As for smell, taste, and touch, we can use electronic noses and tongues to capture different types of chemical and taste data and convert them into text data that the LLM can process. Haptic sensors can capture pressure, temperature, and other physical sensations and convert them into text data using a neural network or anything else.

- Remember, these models should be used as modular components that can be easily switched out as new models emerge. Think of them as lego blocks or react components that we can assemble to create a more comprehensive system.

- So, let's get baking with CupcakeAGI and incorporate multisensory data into an LLM agent to create a more natural and effective human-machine interaction. With the availability of different sensory data, the LLM agent can process and understand various types of data, leading to a more human-like agent that can assist us in different tasks.



