"use client";
import { useState, useEffect, useRef } from "react";
import { chatOutput } from "./chatoutput";
import Loader from "./loader";

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState("");
  const [load, setLoad] = useState(false);
  const [file, setFile] = useState(null);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (load == true) {
      chatOutput(
        messages[messages.length - 1].text,
        file,
        setFile,
        setLoad,
        messages,
        setMessages
      );
    }
  }, [file, load, messages]);

  const handleSendMessage = () => {
    const newMessage = { text: message, sender: "user" };
    setMessages([...messages, newMessage]);
    setMessage("");
    setLoad(true);
  };

  const handleMessage = (event) => {
    setMessage(event.target.value);
  };

  const handleKeyDown = (event) => {
    if (event.keyCode === 13) {
      handleSendMessage();
    }
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  };

  return (
    <div className="flex h-full flex-col rounded-3xl p-4">
      <div className="aa flex-grow overflow-y-auto">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`mb-4 flex ${
              message.sender == "user" ? "justify-end" : "justify-start"
            }`}
          >
            <div
              className={`rounded-xl rounded-b-xl border-2 border-black px-4 py-2 font-semibold shadow-2xl ${
                message.sender == "user"
                  ? "ml-8 rounded-r-none"
                  : "mr-8 rounded-l-none"
              }`}
            >
              {message.text.split("\n").map((line, i) => (
                <div key={i}>{line}</div>
              ))}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div className="mt-4 flex">
        <input
          type="text"
          className="flex-grow rounded-lg border-2 border-gray-300 px-4 py-2"
          placeholder="Type your message here"
          value={message}
          onChange={handleMessage}
          onKeyDown={handleKeyDown}
        />
        {load ? (
          <Loader />
        ) : (
          <div className="ml-4 flex space-x-4">
            <label htmlFor="fileInput">
              <a className="group relative inline-block rounded px-5 py-2.5 font-medium text-white">
                <span className="absolute left-0 top-0 h-full w-full rounded bg-gradient-to-br from-purple-600 to-blue-500 opacity-50 blur-sm filter"></span>
                <span className="absolute inset-0 ml-0.5 mt-0.5 h-full w-full rounded bg-gradient-to-br from-purple-600 to-blue-500 opacity-50 filter group-active:opacity-0"></span>
                <span className="absolute inset-0 h-full w-full rounded bg-gradient-to-br from-purple-600 to-blue-500 shadow-xl filter transition-all duration-200 ease-out group-hover:blur-sm group-active:opacity-0"></span>
                <span className="absolute inset-0 h-full w-full rounded bg-gradient-to-br from-blue-500 to-purple-600 transition duration-200 ease-out"></span>
                <span className="relative">Upload</span>
              </a>
            </label>
            <input
              id="fileInput"
              type="file"
              accept="image/*"
              onChange={handleFileChange}
              style={{ display: "none" }}
            />
            <a
              className="ease group relative z-30 ml-2 box-border inline-flex w-auto cursor-pointer items-center justify-center overflow-hidden rounded-md bg-pink-600 px-8 py-3 font-bold text-white ring-1 ring-indigo-300 ring-offset-2 ring-offset-indigo-200 transition-all duration-300 hover:ring-offset-pink-500 focus:outline-none"
              onClick={handleSendMessage}
            >
              <span className="absolute bottom-0 right-0 -mb-8 -mr-5 h-20 w-8 translate-x-1 rotate-45 transform bg-white opacity-10 transition-all duration-300 ease-out group-hover:translate-x-0"></span>
              <span className="absolute left-0 top-0 -ml-12 -mt-1 h-8 w-20 -translate-x-1 -rotate-45 transform bg-white opacity-10 transition-all duration-300 ease-out group-hover:translate-x-0"></span>
              <span className="relative z-20 flex items-center text-sm">
                <svg
                  className="relative mr-2 h-5 w-5 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M13 10V3L4 14h7v7l9-11h-7z"
                  ></path>
                </svg>
                Send
              </span>
            </a>
          </div>
        )}
      </div>
    </div>
  );
};

export default Chat;
