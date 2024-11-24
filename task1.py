file="file.txt"



with open("file.txt","r", encoding="UTF-8") as file:
    for line in file:
        print(line)



author = input("Хто написав ці рядки?")
with open (file, 'author', encoding='UFT-8') as file:
    file.write(f'(author)\n')


    while True:
        answer = input("Бажаєте додати ще одну цитату? (так / ні)")
        answer = answer.lower()
        quote = input("Введіть цитату:")
        author = input("Введіть автора:")
        file = open(file "a", encoding = "UFT-8")
        file.write("{quote}\n{author})\n")
        file.close()
    else:
        break

with open("file.txt","r", encoding="UTF-8") as file:
    for line in file:
        print(line)