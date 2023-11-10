# Import Modules
import time

# Page Title/Heading

print("L I F E 100 // to infinity and beyond.")

# Subheading
slogan = '\"A Journey to a Long Life Experience"'
print(slogan)
# Space
print()
# Greetings
print("|-----------------------------------------------------------------------------|")
print("| Welcome to our Dearest and Fellow Human Being, that soon to be a SuperHuman |\n"
      "|-----------------------------------------------------------------------------|")
print()
# Introduction
print("Introduction:")
print()
# Making the text message align at the center
def align_center_message(introduction, width=110):
    lines = introduction.split('\n')
    for line in lines:
        line = line.strip()  # Remove leading and trailing spaces
        introduction_length = len(line)
        if introduction_length >= width:
            print(line)
        else:
            padding = (width - introduction_length) // 2
            centered_message = " " * padding + line
            print(centered_message)
intro = "In a world that's constantly evolving, with advances in science, technology, and " \
        "\nhealthcare, we have an unprecedented opportunity to extend and enhance the quality of " \
        "\nour lives. " \
        "\nThe aspiration of living to one hundred years old is no longer a mere dream " \
        "\nbut a realistic goal within reach. It's a journey that's not just about adding years to " \
        "\nour life but adding life to our years. Our collective quest to promote longevity is not " \
        "\nonly a celebration of aging but a testament to the potential of the human spirit. " \
        "\nJoin us on this inspiring journey as we explore the keys to unlocking a century of vibrant " \
        "\nliving and discover the secrets to achieving that cherished milestone of a hundred years."
align_center_message(intro)
print()
print("L I F E 100 // to infinity and beyond.")
print("A Journey to a Long Life Experience")
# Users Input
# Putting delay effects at text
customer_question = "Are you ready to experience this kind of journey?\n"
for character in customer_question:
    print(character, end='', flush=True)
    time.sleep(0.1)
print("[1] YES\n[2] NO")
users_input = eval(input("Select: "))
if users_input == 1:
    print("LET's BEGIN!")
else:
    print("Bye, See you next time!")# Import Modules
import time

# Page Title/Heading

print("L I F E 100 // to infinity and beyond.")

# Subheading
slogan = '\"A Journey to a Long Life Experience"'
print(slogan)
# Space
print()
# Greetings
print("|-----------------------------------------------------------------------------|")
print("| Welcome to our Dearest and Fellow Human Being, that soon to be a SuperHuman |\n"
      "|-----------------------------------------------------------------------------|")
print()
# Introduction
print("Introduction:")
print()
# Making the text message align at the center
def align_center_message(introduction, width=110):
    lines = introduction.split('\n')
    for line in lines:
        line = line.strip()  # Remove leading and trailing spaces
        introduction_length = len(line)
        if introduction_length >= width:
            print(line)
        else:
            padding = (width - introduction_length) // 2
            centered_message = " " * padding + line
            print(centered_message)
intro = "In a world that's constantly evolving, with advances in science, technology, and " \
        "\nhealthcare, we have an unprecedented opportunity to extend and enhance the quality of " \
        "\nour lives. " \
        "\nThe aspiration of living to one hundred years old is no longer a mere dream " \
        "\nbut a realistic goal within reach. It's a journey that's not just about adding years to " \
        "\nour life but adding life to our years. Our collective quest to promote longevity is not " \
        "\nonly a celebration of aging but a testament to the potential of the human spirit. " \
        "\nJoin us on this inspiring journey as we explore the keys to unlocking a century of vibrant " \
        "\nliving and discover the secrets to achieving that cherished milestone of a hundred years."
align_center_message(intro)
print()
print("L I F E 100 // to infinity and beyond.")
print("A Journey to a Long Life Experience")
# Users Input
# Putting delay effects at text
customer_question = "Are you ready to experience this kind of journey?\n"
for character in customer_question:
    print(character, end='', flush=True)
    time.sleep(0.1)
print("[1] YES\n[2] NO")
users_input = eval(input("Select: "))
if users_input == 1:
    print("LET's BEGIN!")
else:
    print("Bye, See you next time!")
