# Text and Morse code Converter 🔤

Project for converting text into valid morse code and vice versa.

---

## 📘 How does it work? 

This project provides **two main functions**, each designed for a specific conversion task. Both functions can work together or independently, depending on your needs.

### 1. Converting Text into Morsecode:
To convert plain text into morse code, use the `text_to_morse()` function.
#### Parameters:
- `codes`: a dictionary where
  - The **Key** is the symbol (e.g., a letter, number, or punctuation mark).  
  - The **Value** is the corresponding morse code.
  - Example: 
    ```python
    codes = {'A': '.-', 'B': '-...', 'C': '-.-.'}
    ```
- `text`: a string containing the text to convert into morse code.  
#### Output:
- Returns a string representing the morse code equivalent of the input text.
  
### 2. Converting Morse code into Text:
To convert morse code into plain text, use the `morse_to_text()` function.  
#### Parameters:
- `codes`: a dictionary where
  - The **Key** is the symbol (e.g., a letter, number, or punctuation mark).  
  - The **Value** is the corresponding morse code.
  - Example: 
    ```python
    codes = {'A': '.-', 'B': '-...', 'C': '-.-.'}
    ```
- `morse`: a string containing the morse code to be converted into text.  
#### Output:
- Returns a string representing the plain text equivalent of the input morse code.

---

## 💡Notes

- The `codes` dictionary must have the same format for both functions to work correctly. Ensure it is consistent and properly structured.  
- Both functions rely entirely on the dictionary you provide for conversions. The accuracy of `text_to_morse()` code and `morse_to_text()` conversions will depend on the completeness and correctness of your dictionary.  
- You can include as few or as many symbols as needed in your dictionary. Customize it to suit your requirements.

---

## 📚 Useful resources

- [Wikipedia Morse Code](https://en.wikipedia.org/wiki/Morse_code)
- [Morse Code Translator](https://morsecode.world/international/translator.html)
 