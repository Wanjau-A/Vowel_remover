def remove_vowels(text):
    vowels = "AEIOUaeiou"
    text_without_vowels = ""
    for char in text:
        if char not in vowels:
            text_without_vowels += char
    return text_without_vowels

def main():
    user_input = input("Enter a text: ")
    result = remove_vowels(user_input)
    print("Text without vowels:", result)

if __name__ == "__main__":
    main()