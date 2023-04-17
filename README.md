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


