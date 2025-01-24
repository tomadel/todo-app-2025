languages = ['English', 'German', 'Spanish']


for language in languages:
    with open(f"{language}.txt", "w") as file:
        file.write(language)
        print(file)