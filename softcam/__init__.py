"""Le logiciel SOFTCAM a pour objectif d'aider le bureau d'études à dimensionner des systèmes de distribution. Il se concentre sur le système allant de la came à la soupape. Actuellement, seul le dimensionnement de systèmes à levier est fonctionnel. De nombreuses améliorations sont nécessaires pour que le logiciel soit utilisable.  

Le fonctionnement du logiciel est le suivant :
1. L'utilisateur crée une étude et un assemblage correspondant au système dont il souhaite vérifier le dimensionnement.
2. L'utilisateur crée la loi de levée.
3. L'utilisateur vérifie que, avec l'assemblage renseigné et la loi de levée créée, les critères de dimensionnement sont respectés. La loi de levée sert de loi entrée-sortie pour le calcul des critères de dimensionnement.

Composition :

Le fichier main.py permet de lancer le logiciel depuis un interpréteur.

Le logiciel est composé de 3 packages principaux :
- domain: Regroupe la logique mathématique et physique du logiciel
- application: Regroupe la logique de l'application en faisant le lien entre les actions de l'utilisateur et la logique mathématique et physique.
- infrastructure: Regroupe le code de contrôle du logiciel, le code permettant le stockage et l'accès aux données et le code permettant de générer l'interface utilisateur.

Pour qu'il soit simple de maintenir les liens entre les packages, le code de "domain" ne doit dépendre d'aucun autre package, le code de "application" peut dépendre de "domain" mais ne doit pas dépendre de "infrastructure". Enfin le code de "infrastructure" peut dépendre de tous les packages.
"""