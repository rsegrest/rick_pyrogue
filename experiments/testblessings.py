from blessings import Terminal

term = Terminal()
if term.does_styling:
    with term.location(0, term.height - 1):
        print('Progress: [=======>   ]')
print(term.bold('Important stuff'))