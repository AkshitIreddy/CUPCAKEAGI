export const chatOutput = async (
  question,
  file,
  setFile,
  setLoad,
  messages,
  setMessages
) => {
  const formData = new FormData();
  formData.append("question", question);
  if (file) {
    formData.append("file", file);
  } else {
    formData.append("file", new File([], "empty-file.txt"));
  }
  for (const [key, value] of formData.entries()) {
    console.log(`${key}: ${value}`);
  }

  const headers = new Headers();
  headers.append("Authorization", "Basic " + btoa("myusername:mypassword"));

  const response = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    body: formData,
    headers: headers,
  });
  const result = await response.json();
  const response_text = result.text;
  const chatbotMessage = {
    text: response_text,
    sender: "chatbot",
  };
  const response_emotion_values = result.emotion_values;
  const chatbotMessage1 = {
    text: response_emotion_values,
    sender: "chatbot",
  };
  const response_sense_values = result.sense_values;
  const chatbotMessage1_2 = {
    text: response_sense_values,
    sender: "chatbot",
  };
  const response_thought = result.thought;
  const chatbotMessage2 = {
    text: response_thought,
    sender: "chatbot",
  };
  const conversation = result.conversation;
  const updatedMessages = conversation.map((message) => ({
    text: message.message,
    sender: message.sender.toLowerCase() === "assistant" ? "chatbot" : "user",
  }));
  setMessages([
    ...updatedMessages,
    chatbotMessage2,
    chatbotMessage1,
    chatbotMessage1_2,
    chatbotMessage,
  ]);
  setLoad(false);
  setFile(null);
};
