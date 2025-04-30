# Groupe n°6
# specialitetest.py
# Questionnaire de spécialité v.2.4 (ajout de couleur dans les prints console / aménagement global / revu du code en globalité / ajout de print error lorsque l'utilisateur met un chiffre à la place d'un mot et inversement / ajout error dans les questions de choix de spé)
# 2°²
# PACHTER Adam, GEREMIA Lilian, DUPERREY Thomas
# Mise à jour du 15.03.2025

def centresinterets():
    # Centres d'intérêts
    reponses = {}
    for key, question in {
        'sciences': "Les matières scientifiques vous intéressent-elles ? \033[34mOui / Bof / Non\033[0m : ",
        'litterature': "Avez-vous une préférence pour les matières littéraires ? \033[34mOui / Bof / Non\033[0m : ",
        'ses': "Les matières liées à l'économie et à la gestion vous attirent-elles ? \033[34mOui / Bof / Non\033[0m : ",
        'art': "L'art et la créativité sont-ils des aspects importants pour vous ? \033[34mOui / Bof / Non\033[0m : ",
        'langues': "Avez-vous un intérêt pour les langues étrangères ou la culture internationale ? \033[34mOui / Bof / Non\033[0m : ",
        'environnement': "Êtes-vous passionné par l'environnement et les sciences naturelles ? \033[34mOui / Bof / Non\033[0m : "
    }.items():
        while True:
            reponse = input(question)
            if reponse in ['Oui', 'Bof', 'Non']:  # Comparaison stricte
                reponses[key] = reponse
                break
            else:
                print("\033[31mRéponse invalide, merci de répondre avec des lettres (Oui, Bof, Non) ou de bien orthographier la réponse.\033[0m")
    
    points = 0
    # Attribution des points en fonction des réponses
    for reponse in reponses.values():
        if reponse == "Oui":
            points += 3
        elif reponse == "Bof":
            points += 2
        else:
            points += 1
    return points

def calculpoints():
    print('\033[34m\nNous allons désormais calculer vos notes pour compléter votre dossier.\033[0m')
    print("\nEntrez vos notes sur 20 :")
    
    # Notes des matières
    notes = {}
    for key, question in {
        'maths': "Note en \033[33mMathématiques\033[0m : ",
        'physique': "Note en \033[33mPhysique Chimie\033[0m : ",
        'svt': "Note en \033[33m SVT\033[0m : ",
        'francais': "Note en \033[33mFrançais\033[0m : ",
        'histoire': "Note en \033[33mHistoire Géo\033[0m : ",
        'langues': "Note en \033[33mAnglais\033[0m : ",
        'ses': "Note en \033[33mSES\033[0m : ",
    }.items(): # ici le .items signifie un dictionnaire de key qui sont les matières (ex : maths est une key)
        while True:
            try:
                note = float(input(question)) # (float = saisir une valeur au clavier)
                if 0 <= note <= 20:
                    notes[key] = note
                    break
                else:
                    print("\033[031mVeuillez entrer une note valide entre 0 et 20\033[0m")
            except ValueError:
                print("\033[031mVeuillez entrer un nombre valide.\033[0m")

    points = 0
    # Attribution des points en fonction des notes
    for note in notes.values():
        if note >= 16:
            points += 3
        elif note >= 12:
            points += 2
        elif note >= 10:
            points += 1
        else:
            points += 0
    return points, notes

def calculprobas(points, specialites):
    probas = {}
    for specialite in specialites:
        if specialite == "Mathématiques":
            if points >= 18:
                probas[specialite] = "Très probable"
            elif points >= 15:
                probas[specialite] = "Probable"
            elif points >= 12:
                probas[specialite] = "Peu probable"
            else:
                probas[specialite] = "Quasi impossible"
        
        elif specialite == "Physique Chimie":
            if points >= 18:
                probas[specialite] = "Très probable"
            elif points >= 15:
                probas[specialite] = "Probable"
            elif points >= 12:
                probas[specialite] = "Peu probable"
            else:
                probas[specialite] = "Quasi impossible"
        
        elif specialite == "SVT":
            if points >= 18:
                probas[specialite] = "Très probable"
            elif points >= 15:
                probas[specialite] = "Probable"
            elif points >= 12:
                probas[specialite] = "Peu probable"
            else:
                probas[specialite] = "Quasi impossible"
        
        elif specialite == "Français":
            if points >= 18:
                probas[specialite] = "Très probable"
            elif points >= 14:
                probas[specialite] = "Probable"
            elif points >= 10:
                probas[specialite] = "Peu probable"
            else:
                probas[specialite] = "Quasi impossible"
        
        elif specialite == "SES":
            if points >= 17:
                probas[specialite] = "Très probable"
            elif points >= 14:
                probas[specialite] = "Probable"
            elif points >= 10:
                probas[specialite] = "Peu probable"
            else:
                probas[specialite] = "Quasi impossible"
        
        elif specialite == "Anglais":
            if points >= 16:
                probas[specialite] = "Très probable"
            elif points >= 12:
                probas[specialite] = "Probable"
            elif points >= 8:
                probas[specialite] = "Peu probable"
            else:
                probas[specialite] = "Quasi impossible"
        
        elif specialite == "Histoire Géo":
            if points >= 16:
                probas[specialite] = "Très probable"
            elif points >= 12:
                probas[specialite] = "Probable"
            elif points >= 8:
                probas[specialite] = "Peu probable"
            else:
                probas[specialite] = "Quasi impossible"
    
    return probas


def main():
    print("Bienvenue dans le questionnaire pour déterminer la probabilité d'obtenir vos spécialités en 1ère !")
    
    # Calcul des points pour les centres d'intérêt
    ptsinteret = centresinterets()

    # Calcul des points pour les notes
    ptsnotes, notes = calculpoints()

    # Demander 3 spécialités
    print("\nLes spécialités possibles sont :")
    print("\033[34m'1'\033[0m: Mathématiques")
    print("\033[34m'2'\033[0m: Physique Chimie")
    print("\033[34m'3'\033[0m: SVT")
    print("\033[34m'4'\033[0m: Français")
    print("\033[34m'5'\033[0m: SES")
    print("\033[34m'6'\033[0m: Anglais")
    print("\033[34m'7'\033[0m: Histoire Géo")

    # Convertir les entrées en noms complets de spécialités
    specialites_dict = {
        '1': "Mathématiques",
        '2': "Physique Chimie",
        '3': "SVT",
        '4': "Français",
        '5': "SES",
        '6': "Anglais",
        '7': "Histoire Géo",
    }
    
    specialites = []
    for i in range(3):
        while True:
            choix = input(f"\nChoisissez votre spécialité n°{i+1} (1-7) : ")
            if choix in specialites_dict:
                # Vérifier si la spécialité (nom complet) a déjà été choisie
                if specialites_dict[choix] in specialites:
                    print("\033[31mVous avez déjà choisi cette spécialité. Veuillez en choisir une autre.\033[0m")
                else:
                    specialites.append(specialites_dict[choix])
                    break
            else:
                print("\033[31mRéponse invalide. Veuillez entrer un chiffre entre 1 et 7.\033[0m")
    
    # Calcul de la probabilité pour les 3 spécialités choisies
    probas = calculprobas(ptsinteret + ptsnotes, specialites)
    
    # Affichage du résultat
    print("\nTotal des points obtenus (centres d'intérêts + notes) : {}".format(ptsinteret + ptsnotes))
    for specialite in specialites:
        prob = probas.get(specialite, "Non calculé")
        print(f"La probabilité d'obtenir la spécialité \033[34m{specialite}\033[0m est : \033[34m{prob}\033[0m")


if __name__ == "__main__":
    main()

print("Simulation terminée.")
