# Human vs Machine Verification

---

## 1. Turing Test

### Purpose
This test is used to determine whether a system responding to questions behaves like a human or a computer program.

### System Components

- **User Input Interface**  
  Allows the judge to ask questions to the system.

- **Response Controller**  
  Selects whether the response will come from a human-like module or an AI module.

- **Human Response Module**  
  Produces answers that imitate natural human communication.

- **AI Response Module**  
  Generates responses using predefined machine-style replies.

- **Result Evaluation Unit**  
  Compares the judge’s guess with the actual responder and determines whether the guess is correct.

### Program File
```
Turing.py
```

---

## 2. CAPTCHA

### Purpose
A CAPTCHA mechanism is used to verify whether the user interacting with a system is a human rather than an automated program.

### System Components

- **Challenge Generator**  
  Creates a random text sequence that acts as the CAPTCHA.

- **Display Interface**  
  Shows the generated CAPTCHA to the user.

- **User Input Handler**  
  Accepts the CAPTCHA text entered by the user.

- **Verification Module**  
  Checks whether the entered text matches the generated CAPTCHA.

- **Access Decision Module**  
  Grants verification if the input is correct; otherwise requests another attempt.

### Program File
```
CAPTCHA.py
```
