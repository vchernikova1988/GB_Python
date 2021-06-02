rus = ['Один', 'Два', 'Три', 'Четыре']
eng = ['One', 'Two', 'Three', 'Four']

with open('4.txt', 'r') as f:
    content = f.read()
    for i, w in enumerate(eng):
        if w in content:
            content = content.replace(w, rus[i])
            print(content)

with open('4rus.txt', 'w', encoding='utf-8') as f:
    f.write(content)

