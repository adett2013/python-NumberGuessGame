# 🎯 Python Number Guess Game

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/License-AGPL%20v3-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Range-1--5-orange?style=for-the-badge" alt="Number Range">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <b>A fun command-line number guessing game built in Python — made after just 1 hour of learning! 🚀</b>
</p>

---

## 📖 About

Howdy! This is a **Number Guessing Game** created as a beginner Python project. The computer randomly picks a number between **1 and 5** and you get one shot to guess it. Guess right and you win — guess wrong and a new number is picked for another round! 🎉

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎲 Random Number Generation | A new secret number (1–5) is picked every round |
| ⚡ Single-Guess Rounds | One guess per round — beat the odds! |
| 🔄 Replay Support | Type `y` or `yes` after winning to play again |
| 🕵️ Number Reveal | If you miss, the correct number is shown so you always learn |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.6+** installed on your machine. Download it from [python.org](https://www.python.org/downloads/).

### Installation

```bash
# Clone this repository
git clone https://github.com/adett2013/python-NumberGuessGame.git

# Navigate into the project directory
cd python-NumberGuessGame
```

### Running the Game

```bash
python main.py
```

---

## 🎮 How to Play

1. **Run** the script using the command above.
2. The program picks a **random number between 1 and 5**.
3. **Type your guess** (a number from 1 to 5) and press Enter.
4. Two outcomes are possible:
   - 🎉 **Correct!** — The number is revealed and you're asked if you want to play again.
   - ❌ **Wrong!** — The correct number is revealed, and a fresh round starts automatically.
5. After a correct guess, type `y` or `yes` to play again, or anything else to quit.

---

## 📸 Example Gameplay

**Winning round:**
```
Welcome to the number guessing game! You have to guess the random number between 1-5. Lets go!
Type your guess! 3
You've guessed the correct number! Number: 3
Type y to play again. Type n to quit. y
Type your guess! 
```

**Losing round:**
```
Welcome to the number guessing game! You have to guess the random number between 1-5. Lets go!
Type your guess! 2
The random number was 4
Try again. Note: The number has changed after your guess.
Type your guess! 
```

**Quitting:**
```
Type y to play again. Type n to quit. n
Thanks for playing my game. This means a lot to me!
Find more games on https://www.arne-dettmer.de
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
<p align="center">Find more games on <a href="https://www.arne-dettmer.de">arne-dettmer.de</a></p>

