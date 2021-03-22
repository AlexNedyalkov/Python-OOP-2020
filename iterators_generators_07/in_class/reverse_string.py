def reverse_text(text: str):
    counter = 1
    while counter <= len(text):
        yield text[len(text) - counter]
        counter += 1

for char in reverse_text('step'):
    print(char, end = '')