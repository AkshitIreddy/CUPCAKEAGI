# CUPCAKEAGI 🧁🍰🎉🤖🧠🍩🍪

Hey there cupcake lovers🧁❤️! I am excited to introduce you to my latest project, CupcakeAGI!

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

# ✨ About

![Screenshot 2023-04-17 092049](https://user-images.githubusercontent.com/90443032/232563766-c2bd698b-c029-4221-8e33-3d20d9b0777f.png)


CupcakeAGI is an agent that aims to mimic human-like behavior and cognitive abilities to assist users in performing various tasks. It's equipped with some sweet🍬 features, including the ability to dream😴, have random thoughts, and perform mental simulations on how to complete a task. Just like how we humans have thoughts floating around our heads, CupcakeAGI has a thought bubble💭 with abstract words.

To make CupcakeAGI more expressive, I've added emotion parameters. This will allow it to interact with users in a more personal way❤️.

One of CupcakeAGI's most impressive features is its ability to accept various forms of sensory data, such as images🐶, videos📹, and audio🎵. Although I haven't implemented smell👃, touch✋ and taste👅 yet, it should be similar to what I did for image, video, and audio. You'll need a function to convert the sensory data to text and then it will get added as a file description for the file which will be used while prompting the model.

CupcakeAGI provides two main features for user interaction: talk and task. The talk feature allows for immediate responses to user queries using tools like search engines, calculators, and translators, making it a real-time problem solver. And who doesn't love a good problem solver🧠, especially when it comes to baking cupcakes🧁?

The task feature is used for completing tasks at a start time or by a deadline. This feature allows for chaining multiple tools together using a natural language task function that converts the output of one tool into the input of another, making different tools compatible with each other. So, whether you need to bake some cupcakes for a birthday party or a cupcake contest, CupcakeAGI is here to help you out!

Overall, I hope you find CupcakeAGI to be a sweet addition to your life. This project was a lot of fun to create, and I'm excited to see where it goes. Thanks for reading, and happy baking!✨

# ✨ Why?

- Our brain processes and integrates these sensory inputs to form a coherent perception of the world around us. Similarly, in the realm of artificial intelligence, the ability to process and integrate multisensory data is crucial for building intelligent agents that can interact with humans in a more natural and effective way.

- In recent years, large language models (LLMs) such as ChatGPT and GPT-4 have demonstrated remarkable abilities in generating human-like text based on vast amounts of training data. However, these models are typically limited to working with text and image data and lack the ability to process other types of sensory inputs.

- Beyond the ability to process multisensory data, the human-like LLM agent presented in this paper also exhibits several cognitive abilities that are typically associated with humans. For instance, the agent is equipped with the ability to dream and have random thoughts, which are thought to play important roles in human creativity, memory consolidation, and problem-solving. By incorporating these features into the LLM agent, we aim to create an agent that can assist users in performing tasks in a more natural and effective way and make these agents more human-like.

# ✨ Multisensory Data

- 🧁 Welcome back to the world of cupcakes and baking! We all know that human experience is much more than just text-based interactions. It's not just about reading, but also about experiencing the world with all our senses, including sight 👀, sound 🔊, smell 👃, taste 👅, and touch 👐. Similarly, an LLM agent that can work with multisensory data can open up a new world of possibilities for machine learning.

- Instead of missing out on the rich and varied data available through other sensory modalities, we can use neural network architectures that convert various forms of sensory data into text data that the LLM can work with.

- For instance, we can use image captioning models like vit-gpt2 and blip to convert images into text data, which the LLM agent can then process. Similarly, for audio data, audio-to-text models like OpenAI's Whisper can be used to convert audio signals into text data.📷🎤

- Now, I know what you're thinking: what about videos 🎥, smell 👃, taste 👅, and touch 👐? Don't worry, we got you covered! To save computation, we can use one frame per second of video data and use image captioning models to convert each frame into text. The audio track from the video can be separated and transcribed using audio-to-text models, providing the LLM agent with both visual and auditory data.

- As for smell 👃, taste 👅, and touch 👐, we can use electronic noses and tongues to capture different types of chemical and taste data and convert them into text data that the LLM can process. Haptic sensors can capture pressure, temperature, and other physical sensations and convert them into text data using a neural network or anything else.

- Remember, these models should be used as modular components that can be easily switched out as new models emerge. Think of them as lego blocks or react components that we can assemble to create a more comprehensive system.

- So, let's get baking with CupcakeAGI and incorporate multisensory data into an LLM agent to create a more natural and effective human-machine interaction. With the availability of different sensory data, the LLM agent can process and understand various types of data, leading to a more human-like agent that can assist us in different tasks.🧁💻

# ✨ Human Like Behavior and Persistent Memory

🧁👋 Welcome to CupcakeAGI, where we bake up some sweet and creamy AI goodness! 🍰🤖

Here are some of the key features of our LLM agent that make it more human-like and effective:

- 🧠 Human-like behavior: Our LLM agent is equipped with several features that mimic human behavior, including the ability to dream, have random thoughts, and perform mental simulations of how to complete a task. These features allow the agent to better understand and respond to user queries.

- 🤖 Persistent memory: Our LLM agent has a state of mind where all files relating to its personality, emotions, thoughts, conversations, and tasks are stored. Even if the agent has stopped running, all relevant information is still stored in this location. This allows the agent to provide a more personalized and effective experience.

- 😃 Emotion parameters: We use emotion parameters such as happiness, sadness, anger, fear, curiosity, and creativity to make the LLM agent more expressive and better understand the user's needs and preferences.

- 💭 Thought bubble: Our LLM agent also has a thought bubble, which is essentially a list of lists that corresponds to different topics. This allows the agent to more effectively process and integrate its thoughts with the user's queries and tasks.

- 🗣️ Conversation storage: The LLM agent stores the conversation it has had so far and the list of tasks it needs to perform. It breaks the conversation into chunks and summarizes it to maintain coherence and relevance. This allows the agent to maintain a coherent and relevant conversation with the user.

With these features, our LLM agent is better equipped to assist users in performing tasks in a natural and effective way. We hope you enjoy our sweet and creamy AI goodness! 🧁🍰🤖

# ✨ Talk & Task

🧁👋 Welcome to CupcakeAGI! Here are some sweet deets about the LLM agent that will make your tasks a cakewalk:

- 🗣️ Talk and Task modes make it easy for users to communicate with the LLM and get things done seamlessly.
- 📁 The LLM converts files like images, videos, and audio to text, making them easy to store and retrieve.
- 🔍 With access to various tools like search engines, wikis, and translators, the LLM can provide users with the necessary information for their queries.
- 🧰 Natural language task functions allow users to chain together different tools, making them compatible with each other.
- 🕰️ The Task mode is particularly useful for lengthy tasks and can be set to start at a specific time, allowing users to focus on other things while the LLM takes care of the task.
- 💭 The LLM experiences random thoughts and dreams, just like humans, making it more relatable and human-like.
- 🧑‍💻 The LLM can even use Python packages like Hugging Face models to complete tasks, making it a highly versatile agent.
So go ahead and give CupcakeAGI a try! With its modular approach, you can easily add new tools and features as needed. Who knew cupcakes and AI could go so well together? 🧁🤖

# ✨ Limitations

Welcome to CupcakeAGI! 🧁🍰🍩🍪

Let's talk about some important things you need to know about this sweet project:

- Complex tasks: While CupcakeAGI is as human-like as possible, it may not be able to solve complex tasks that require significant back and forth. We're talking about tasks that involve negotiating with multiple parties to reach a solution. CupcakeAGI is intended to assist individuals on a personal level, but it may not be suitable for solving highly intricate problems. Don't worry, though, CupcakeAGI is still your go-to for all your cupcake baking needs! 🧁👩‍🍳

- Accuracy of sensory data conversion: The effectiveness of CupcakeAGI relies heavily on the accuracy of the neural network architectures used to convert sensory data into text. If these models are not accurate, CupcakeAGI may misunderstand the user's input, leading to incorrect or ineffective responses. But don't fret, we're constantly working on improving CupcakeAGI's accuracy to ensure you get the best experience possible! 🤖🎂

- Ethics and Privacy: CupcakeAGI has the potential to collect and process a large amount of personal data from the users. Thus, there is a risk that sensitive data may be compromised, leading to privacy concerns. CupCakeAGI will do it's best to keep your cupcake secrets safe! 🔒🤫

Thanks for checking out CupcakeAGI, and remember, with CupcakeAGI by your side, you'll always have the perfect cupcake recipe! 🧁💻

# ✨ Conclusion

Welcome to the conclusion of our multisensory LLM agent project! 🎉🧁🤖🧠

Here are the key takeaways from our project 🤪🧁

- Our LLM agent is like a cupcake, made with many different ingredients - it can work with multisensory data, dream, have random thoughts, and show emotions 🧁💭😍
- By incorporating multisensory data, our agent can understand different types of information, just like a baker uses different ingredients to make a delicious cupcake 🍰👀
- With its cognitive abilities and persistent memory, our agent can assist users in a more human-like way, just like a friendly baker who helps you choose the perfect cupcake flavor 🤝🧁
- This project represents a small but important step towards building more natural and effective AI assistants, just like a small cupcake can bring a smile to someone's face and brighten their day 🌞🧁
- We hope our project has inspired you to think about the possibilities of multisensory LLM agents and how they can improve human-machine interaction. Thank you for taking the time to check out our project - it was made with lots of love and cupcakes! ❤️🧁

