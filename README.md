# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Look at the "Developer Debug Info" tab to see the secret number shown for debugging.
2. In the main game tab, type a number into the guess input field and click the "Submit" button.
3. Read the hint that appears: it will say whether your guess is too high (Go LOWER) or too low (Go HIGHER).
4. Adjust your next guess according to the hint and submit again; repeat until you see "🎉 Correct!".
5. When you win, note the attempts and score shown; use the "Reset" or change difficulty to play another round.

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here --> ![alt text](image.png)

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
pytest
========================== test session starts ===========================
platform darwin -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0
rootdir: /Users/abiralshrestha/Documents/Python/CodePath/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.10.0
collected 9 items                                                        

tests/test_game_logic.py .........                                 [100%]

=========================== 9 passed in 0.02s ============================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
