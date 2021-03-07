import random

choises = ['Πέτρα', 'Ψαλίδι', 'Χαρτί']
score = {'Computer': 0, 'Player': 0}

menu = """1) Πέτρα
2) Ψαλίδι
3) Χαρτί
0) Για να βγείτε απο το πρόγραμμα """

def show_result(choise, computer_choise):
    if choise == computer_choise:
        print('Ισσοπαλία')
        return

    if choise - computer_choise in [-1, 2]: # Dimitris Android sugestion
        print('Κερδίσατε!')
        score['Player'] += 1
        return
        
    print('Χάσατε!')
    score['Computer'] += 1
    return

    
def show_result_refactored_1(choise, computer_choise):
    if choise == computer_choise:
        print('Ισσοπαλία')
        return

    if (choise - computer_choise) % 3 == 1:
        print('Χάσατε!')
        score['Computer'] += 1
        return

    print('Κερδίσατε!')
    score['Player'] += 1 
    return

def show_result_refactored_2(choise, computer_choise):
    if choise == computer_choise:
        print('Ισσοπαλία')
        return

    if choise - computer_choise == -1 or choise - computer_choise == 2:
        print('Κερδίσατε!')
        score['Player'] += 1 
        return

    print('Χάσατε!')
    score['Computer'] += 1 
    return





while True:
    print(f"To σκορ είναι: Υπολογιστής: {score['Computer']} | Εσείς: {score['Player']}")
    print(menu)
    choise = int(input('Παρακαλώ επιλέξτε:'))

    if choise not in range(4):
        print('Παρακαλώ επιλέξτε έναν αριθμό απο το 0 έως το 3')
        continue

    if choise == 0:
        break

    choise -= 1
    
    print(f'Επιλέξατε {choises[choise]}')

    computer_choise = random.randrange(3)
    print(f'O Υπολογιστής επέλεξε {choises[computer_choise]}')
    # show_result(choise, computer_choise)
    show_result_refactored_2(choise, computer_choise)
    print('-'*80)