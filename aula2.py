nome = 'matheus';
idade = 20;
altura = 1.74;
curso = "Análise e desenvolvimento de sistemas";

linha1 = f'Seu nome é {nome}, você tem {idade} anos com {altura:.2f} e cursa {curso}'.format("matheus", "idade", "curso");
linha2 = f"Seu nome é {nome}"
print(linha1, linha2);


a = 'A';
b ='B';
c = 1.2;

string = "A= {string1}, B= {string2} e C= {string3}";

formato = string.format(
    string1= a,
    string2= b,
    string3=c
)
print(formato);