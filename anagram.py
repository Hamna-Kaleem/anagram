from IPython.core.display import display, HTML
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Anagram Game 💥</title>
  <style>
    body {
      font-family: 'Comic Sans MS', sans-serif;
      background-color: #fff8f0;
      text-align: center;
      padding: 40px;
    }

    h1 {
      font-size: 2.5em;
      color: #4a2d6e;
    }

    #anagram {
      font-size: 2em;
      margin: 20px 0;
      color: #ff7f50;
    }

    #message {
      font-size: 1.5em;
      margin: 20px 0;
    }

    input[type="text"] {
      padding: 10px;
      font-size: 1em;
      width: 200px;
    }

    button {
      padding: 10px 20px;
      font-size: 1em;
      margin: 10px 5px;
      cursor: pointer;
      background-color: #ffb347;
      border: none;
      border-radius: 5px;
    }

    #reshuffle {
      background-color: #ffd966;
    }

    #restart {
      background-color: #90ee90;
      display: none;
    }

    #stop {
      background-color: #ff6347;
    }

    #score {
      margin-top: 20px;
      font-size: 1.2em;
      color: #444;
    }
  </style>
</head>
<body>

  <h1>💥 Anagram Game 🧠</h1>
  <div id="anagram">Loading...</div>
  <input type="text" id="guess" placeholder="Type your guess">
  <br>
  
  <button id="reshuffle" onclick="reshuffleWord()">🔄 Reshuffle</button>
  <button id="stop" onclick="stopGame()">🛑 Stop</button>
  <div id="message"></div>
  <div id="score">Score: 0</div>
  <button id="restart" onclick="newGame()">🔁 Play Again</button>

  <script>
    const words = [
  { word: "apple", hint: "A fruit 🍎" },
  { word: "dog", hint: "A loyal pet 🐕" },
  { word: "friend", hint: "Someone you trust 👯" },
  { word: "table", hint: "Furniture with four legs 🪑" },
  { word: "house", hint: "Where you live 🏠" },
  { word: "computer", hint: "A device for work and play 💻" },
  { word: "window", hint: "See through this at the outside 🌳" },
  { word: "clock", hint: "Tells time 🕒" },
  { word: "ball", hint: "Round object for playing ⚽" },
  { word: "music", hint: "What you listen to with your ears 🎶" },
  { word: "book", hint: "Read this to learn 📖" },
  { word: "car", hint: "A vehicle you drive 🚗" },
  { word: "pizza", hint: "Cheesy and round 🍕" },
  { word: "computer", hint: "An essential device for work 💻" },
  { word: "school", hint: "Place for learning 🎓" },
  { word: "coffee", hint: "A hot drink ☕" },
  { word: "beach", hint: "Where you can find sand and water 🏖️" },
  { word: "mountain", hint: "A tall natural formation ⛰️" },
  { word: "summer", hint: "Season for sun and heat ☀️" },
  { word: "birthday", hint: "Celebrate this once a year 🎉" },
  { word: "rainbow", hint: "Colorful arc in the sky 🌈" },
  { word: "chocolate", hint: "Sweet treat 🍫" },
  { word: "family", hint: "Your loved ones 👨‍👩‍👧‍👦" },
  { word: "friendship", hint: "Bond between best friends 👯‍♂️" },
  { word: "garden", hint: "Place where plants grow 🌷" },
  { word: "summer", hint: "A hot and sunny season 🌞" },
  { word: "shopping", hint: "Buying things from stores 🛍️" },
  { word: "painting", hint: "Art done with colors 🎨" },
  { word: "guitar", hint: "Musical instrument with strings 🎸" },
  { word: "tea", hint: "A warm drink 🍵" },
  { word: "basket", hint: "Used for carrying things 🧺" },
  { word: "computer", hint: "For work and games 💻" },
  { word: "camera", hint: "For taking photos 📸" },
  { word: "park", hint: "Outdoor space for walking and playing 🌳" },
  { word: "sunshine", hint: "Bright sunlight 🌞" },
  { word: "snow", hint: "Cold, white flakes ❄️" }
];
    let current, tries = 3, score = 0, shuffled = "", gameActive = true;

    function shuffle(str) {
      return str.split('').sort(() => Math.random() - 0.5).join('');
    }

    function newGame() {
      current = words[Math.floor(Math.random() * words.length)];
      shuffled = shuffle(current.word);
      document.getElementById("anagram").textContent = " " + shuffled;
      document.getElementById("message").textContent = "";
      document.getElementById("guess").value = "";
      tries = 3;
      document.getElementById("restart").style.display = "none";
      gameActive = true;
    }

    function checkGuess() {
      if (!gameActive) return;
      const guess = document.getElementById("guess").value.toLowerCase().trim();
      if (guess === current.word) {
        document.getElementById("message").innerHTML = "✅ Correct! 🎉 You're a brain ninja!";
        score++;
        updateScore();
        setTimeout(newGame, 1500); // Automatically start next round after 1.5 seconds
      } else {
        tries--;
        if (tries > 0) {
          document.getElementById("message").innerHTML = `❌ Nope! Hint: ${current.hint}<br>Tries left: ${tries}`;
        } else {
          document.getElementById("message").innerHTML = `💀 Game Over! The word was: <b>${current.word}</b>`;
          setTimeout(newGame, 1500); // Automatically start next round after 1.5 seconds
        }
      }
      document.getElementById("guess").value = "";
    }

    function reshuffleWord() {
      shuffled = shuffle(current.word);
      document.getElementById("anagram").textContent = " " + shuffled;
    }

    function updateScore() {
      document.getElementById("score").textContent = "Score: " + score;
    }

    document.getElementById("guess").addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
        checkGuess();
      }
    });

    function stopGame() {
      gameActive = false;
      document.getElementById("message").innerHTML = "🛑 Game stopped. Thanks for playing!";
      document.getElementById("restart").style.display = "inline-block";
    }

    newGame();
  </script>

</body>
</html>


"""

display(HTML(html_code))
