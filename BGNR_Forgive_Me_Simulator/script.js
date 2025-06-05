const noButton = document.getElementById("noButton");
const yesButton = document.getElementById("yesButton");
const responseText = document.getElementById("responseText");

let shrinkCount = 0;
const warningMessages = [
  "Please don't! 😭",
  "You're breaking my heart 💔",
  "I have cookies 🍪",
  "Are you sure?? 😢",
  "Think twice! 😵",
  "You're gonna regret this...",
  "But I did the dishes!",
  "I'll be sad forever 😔",
  "Forgiveness is trendy now!"
];

noButton.addEventListener("mouseenter", () => {
  noButton.style.position = "absolute";

  const maxX = window.innerWidth - noButton.offsetWidth;
  const maxY = window.innerHeight - noButton.offsetHeight;

  const newX = Math.floor(Math.random() * maxX);
  const newY = Math.floor(Math.random() * maxY);

  noButton.style.left = `${newX}px`;
  noButton.style.top = `${newY}px`;

  shrinkCount++;
  const scale = Math.max(1 - shrinkCount * 0.1, 0.3);
  noButton.style.transform = `scale(${scale})`;

  const randomMsg = warningMessages[Math.floor(Math.random() * warningMessages.length)];
  createWarningText(randomMsg);

  if (shrinkCount >= 7) {
    noButton.style.opacity = "0";
    setTimeout(() => {
      noButton.style.display = "none";
    }, 300);
  }
});

yesButton.addEventListener("click", () => {
  responseText.innerText = "Fine... but I'm watching you 👀❤️";
  for (let i = 0; i < 40; i++) {
    createHeart();
  }
});

function createHeart() {
  const heart = document.createElement("div");
  heart.classList.add("heart");
  heart.innerText = "💖";
  heart.style.left = Math.random() * 100 + "vw";
  heart.style.fontSize = `${Math.random() * 20 + 20}px`;
  heart.style.animationDuration = `${Math.random() * 2 + 2}s`;
  document.body.appendChild(heart);

  setTimeout(() => {
    heart.remove();
  }, 5000);
}

function createWarningText(text) {
  const warning = document.createElement("div");
  warning.classList.add("warning-text");
  warning.innerText = text;
  warning.style.left = Math.random() * 80 + 10 + "vw";
  warning.style.top = Math.random() * 80 + 10 + "vh";
  document.body.appendChild(warning);
  setTimeout(() => warning.remove(), 2000);
}
