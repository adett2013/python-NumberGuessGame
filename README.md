# 🎯 Python Number Guess Game

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/License-AGPL%20v3-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Difficulty-Beginner%20Friendly-brightgreen?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <b>A fun command-line number guessing game built in Python — made after just 1 hour of learning! 🚀</b>
</p>

---

## 📖 About

Howdy! This is a **Number Guessing Game** created as a beginner Python project. The computer picks a secret random number and you try to guess it — getting *higher* or *lower* hints along the way until you nail it! 🎉

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎲 Random Number Generation | A new secret number is picked every game |
| 💬 Interactive Hints | Get "Too high!" or "Too low!" feedback after every guess |
| 🔄 Replay Support | Play as many rounds as you like |
| 🏆 Attempt Counter | See how many guesses it took you to win |
| 🛡️ Input Validation | Handles non-numeric input gracefully |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.x** installed on your machine. Download it from [python.org](https://www.python.org/downloads/).

### Installation

```bash
# Clone this repository
git clone https://github.com/adett2013/python-NumberGuessGame.git

# Navigate into the project directory
cd python-NumberGuessGame
```

### Running the Game

```bash
python number_guess.py
```

---

## 🎮 How to Play

1. **Run** the script using the command above.
2. The program will **pick a random secret number** within a set range (e.g. 1–100).
3. **Enter your guess** when prompted.
4. You'll receive one of three hints:
   - 📈 `Too high!` — your guess is above the secret number
   - 📉 `Too low!` — your guess is below the secret number
   - 🎉 `Correct!` — you guessed it!
5. Keep guessing until you find the secret number.
6. Your **total number of attempts** will be displayed when you win.

---

## 📸 Example Gameplay

```
Welcome to the Number Guessing Game! 🎯
I'm thinking of a number between 1 and 100...

Enter your guess: 50
📉 Too low! Try again.

Enter your guess: 75
📈 Too high! Try again.

Enter your guess: 62
📉 Too low! Try again.

Enter your guess: 68
🎉 Correct! You guessed it in 4 attempts. Well done!
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. Open a **Pull Request**

---

## 📜 License

This project is licensed under the **GNU Affero General Public License v3.0**. See the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ and Python · Happy Guessing! 🎯</p>

