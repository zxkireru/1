def replace_char_with_emoji(input_string, char_to_replace):
    modified_string = input_string.replace(char_to_replace, '😎')
    
    return modified_string

input_string = input("Enter a string: ")
char_to_replace = input("Enter the character to be replaced: ")

modified_string = replace_char_with_emoji(input_string, char_to_replace)

print(f"Modified string: {modified_string}")
