const API_URL = "http://127.0.0.1:8000/chat";

async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const userMessage = input.value.trim();
  if (!userMessage) return;

  chatBox.innerHTML += `<div><strong>You:</strong> ${userMessage}</div>`;
  input.value = "";

  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: userMessage })
  });

  const data = await response.json();
  chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
