# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- The logic is reversed, if the number is lower, it says higher and vice versa
- The enter submit key is not working
- Mismatch with the game state in hamburger and the home area
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used github copilot to move all the logic part from app.py to logic.py
- I categorized the bugs into logic issue, ui issue and Initialization issues and worked with them in a separate chat
- Correct suggestion : I asked copilot to fix reversed hint messages. It suggested to just swap the messages. I verified it through writing test cases. The test cases passed all the test.
- Incorrect suggestion : I thought update_score was broken because the score kept dropping unevenly. Copilot told me the -5 per wrong guess was intentional design, not a bug. The real issue was that attempts started at 1 instead of 0, making the win bonus calculate 10 points too low. I caught this by writing a pytest test that expected 80 points and got 70.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I asked copilot to write test and checked through it, for the user experience part, I asked it myself
- For example, test_update_score_win_bonus_first_attempt expected 80 points but returned 70, which revealed the off-by-one bug in attempts initialization.
- For UI bugs like the Enter key not working, I tested manually in the browser. I told Copilot about the bugs. It helped me know what to test , and it wrote the test cases.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  -> Every time you click a button or type something, Streamlit reruns the whole app. State is like a variable that stores the data between those refresh phase

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- One habit is I will try to divide the bugs based on their type (logic, UI). This way I AI model will not hallucinate.
- Next time, I will first run test-cases on AI generated code then only accept the changes
- This project taught me that AI-generated code can look correct but hide subtle bugs; reading and testing it yourself is still necessary.
