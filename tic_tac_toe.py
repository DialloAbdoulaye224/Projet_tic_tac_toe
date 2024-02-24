def afficher_grille(grille):
    print("  " + " ".join(str(i) for i in range(3)))
    print(" +" + "--" * 3)

    for i, ligne in enumerate(grille):
        ligne_affichee = f"{i}|"
        for case in ligne:
            ligne_affichee += f" {case} |"
        print(ligne_affichee)
        print(" +" + "--" * 3)

def verifier_victoire(grille, symbole):
    # Vérification des lignes et des colonnes
    for i in range(3):
        if all(grille[i][j] == symbole for j in range(3)) or all(grille[j][i] == symbole for j in range(3)):
            return True

    # Vérification des diagonales
    if all(grille[i][i] == symbole for i in range(3)) or all(grille[i][2 - i] == symbole for i in range(3)):
        return True

    return False
def minimax(grille, symbole_ia, symbole_joueur):
    # Fonction d'évaluation pour le jeu de Tic-Tac-Toe
    def evaluer(grille, symbole):
        if verifier_victoire(grille, symbole_ia):
            return 1
        elif verifier_victoire(grille, symbole_joueur):
            return -1
        else:
            return 0

    def minimax_rec(grille, profondeur, maximisant, symbole):
        if profondeur == 0 or verifier_victoire(grille, symbole_ia) or verifier_victoire(grille, symbole_joueur):
            return evaluer(grille, symbole_ia)

        if maximisant:
            meilleur_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if grille[i][j] == " ":
                        grille[i][j] = symbole
                        score = minimax_rec(grille, profondeur - 1, False, symbole_joueur)
                        grille[i][j] = " "
                        meilleur_score = max(meilleur_score, score)
            return meilleur_score
        else:
            meilleur_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if grille[i][j] == " ":
                        grille[i][j] = symbole
                        score = minimax_rec(grille, profondeur - 1, True, symbole_ia)
                        grille[i][j] = " "
                        meilleur_score = min(meilleur_score, score)
            return meilleur_score

    meilleur_score = float('-inf')
    meilleur_coup = None
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = symbole_ia
                score = minimax_rec(grille, 4, False, symbole_joueur)
                grille[i][j] = " "
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = (i, j)
    return meilleur_coup

def jouer_tic_tac_toe():
    grille = [[" "]*3 for _ in range(3)]
    tour = 0
    symboles = ["X", "O"]
    ia = True

    while True:
        afficher_grille(grille)
        symbole = symboles[tour % 2]
        print(f"C'est au tour de {symbole}")

        if ia and symbole == "O":
            ligne, colonne = minimax(grille, "O", "X")
        else:
            ligne = int(input("Choisissez une ligne (0-2) : "))
            colonne = int(input("Choisissez une colonne (0-2) : "))

        if grille[ligne][colonne] == " ":
            grille[ligne][colonne] = symbole
            if verifier_victoire(grille, symbole):
                afficher_grille(grille)
                print(f"Le joueur {symbole} a gagné !")
                break
            tour += 1
        else:
            print("La case est déjà occupée. Choisissez une autre case.")

        if tour == 9:
            afficher_grille(grille)
            print("Match nul !")
            break

if __name__ == "__main__":
    jouer_tic_tac_toe()
