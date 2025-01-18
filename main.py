def text_to_morse(codes: {}, text: str) -> str:
    """
    :param codes: Accepts a dictionary of morse codes, where the Key is the symbol and the Value is the morse code.
    :param text: Accepts a string that contains the plain message to convert into morse code.
    :return: Returns a string containing the converted text into morse code.
    """
    convertedMessage = ""
    for letter in text:
        if letter.upper() in codes.keys():
            convertedMessage += codes[letter.upper()] + " "

    return convertedMessage


def morse_to_text(codes: {}, morse: str) -> str:
    """
    :param codes: Accepts a dictionary of morse codes, where the Key is the symbol and the Value is the morse code.
    :param morse: Accepts a string that contains the morse code message to convert into plain text.
    :return: Returns a string containing the converted morse code message into plain text.
    """
    formattedCodes = {}
    for key, value in codes.items():
        formattedCodes[value] = key

    listCodes = morse.split(" ")
    convertedMessage = ""
    for code in listCodes:
        if code in formattedCodes.keys():
            convertedMessage += formattedCodes[code]

    return convertedMessage


if __name__ == "__main__":
    morseCodes = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }
    plainMessage = input("Introduce your text for morse code convertion (only letters and numbers): ")
    print(f"Converted text to morse: {text_to_morse(morseCodes, plainMessage)}")

    plainMessage = input("Introduce your morse to text convertion: ")
    print(f"Converted morse to text: {morse_to_text(morseCodes, plainMessage)}")
