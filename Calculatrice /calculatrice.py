class Calculatrice:
    def __init__(self):
        self.result = 0
        
    def addition(self, a, b):
        return a + b
    
    def soustraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b == 0:
            raise ValueError("Division par zéro n'est pas permise")
        return a / b
    
    def exponentiation(self, a, b):
        return a ** b


if __name__ == "__main__":
    calc = Calculatrice()
    print("Calculatrice simple")
    
    while True:
        print("\nOpérations disponibles:")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Quitter")
        
        choix = input("\nChoisissez une opération (1-6): ")
        
        if choix == '6':
            print("Au revoir!")
            break
            
        if choix not in ['1', '2', '3', '4', '5']:
            print("Choix invalide. Veuillez réessayer.")
            continue
            
        try:
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            
            if choix == '1':
                resultat = calc.addition(a, b)
                print(f"Résultat: {a} + {b} = {resultat}")
            elif choix == '2':
                resultat = calc.soustraction(a, b)
                print(f"Résultat: {a} - {b} = {resultat}")
            elif choix == '3':
                resultat = calc.multiplication(a, b)
                print(f"Résultat: {a} * {b} = {resultat}")
            elif choix == '4':
                try:
                    resultat = calc.division(a, b)
                    print(f"Résultat: {a} / {b} = {resultat}")
                except ValueError as e:
                    print(f"Erreur: {e}")
            elif choix == '5':
                resultat = calc.exponentiation(a, b)
                print(f"Résultat: {a} ^ {b} = {resultat}")
        except ValueError:
            print("Veuillez entrer des nombres valides.")