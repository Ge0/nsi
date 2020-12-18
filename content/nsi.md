# Numérique et Sciences de l’Informatique (NSI)

Ce document a pour objectif de fournir des ressources supplémentaires et optionnelles pour l’élève
étudiant de la spécialité NSI au lycée.

## FizzBuzz

Le FizzBuzz est un exercice de programmation simple qui consiste en l’énoncé suivant :

Pour chaque nombre de 1 à 100, afficher sur l’écran :

- "Fizz" si le nombre courant est divisible par 3 ;
- "Buzz" si le nombre courant est divisible par 5 ;
- "FizzBuzz" si le nombre courant est divisible par 3 et par 5 ;
- le nombre courant dans tous les autres cas.

Cet exercice paraît trivial en soi… Et pourtant il est proposé aux candidats à un poste de
développeur dans la plupart des entreprises ! Cela permet d’écarter très rapidement des
personnes qui ne seraient pas à même de résoudre un problème aussi simple.


## La suite de Fibonnaci

La suite de Fibonnaci est aussi un exercice assez récurrent que l’on présente aux candidats à
un entretien.

Pour rappel, il s’agit de la suite mathématique suivante :

$$\forall n \subset \mathbb N, n \geq 2, U_n = U_{n-1} + U_{n-2}$$

avec : 

$$U_0 = U_1 = 1$$

En termes simples, il s’agit d’additionner les deux éléments précédents de la suite pour obtenir
l’élément courant. On considère $U_0$ le premier élément de la suite (qui vaut 1) et $U_1$ le deuxième
élément de la suite (qui vaut 1 aussi).

Ainsi,

$U_2 = U_1 + U_0 = 1 + 1 = 2$

$U_3 = U_2 + U_1 = 2 + 1 = 3$

$U_4 = U_3 + U_2 = 3 + 2 = 5$

Etc.

On obtient donc les nombres suivants : 1, 1, 2, 3, 5, 8, 13, 21…

L’idée est d’écrire une fonction qui prend en entrée un nombre $n$ supérieur ou égal à 0 et renvoie l’élément
de la suite correspondant.

Cet exercice algorithmique est encore plus intéressant que le FizzBuzz, car il introduit des notions mathématiques
et invite à réfléchir sur les variables à utiliser.

## La factorielle

En mathématique, une factorielle est une fonction unaire (ne prend qu’un seul argument) et correspond au produit de ce nombre
par ses prédécesseurs dans les entiers naturels strictement positif. La factorielle du nombre $n$ se note $n!$ (point d’exclamation
après le nombre).

On a donc :

$$\forall n 	\subset \mathbb N^*, n! = \prod_{i=1}^{n} i$$

Cas particulier : $0! = 1$.

Remarque : 

Pour les non-adeptes de la beauté du langage mathématique, quelques exemples pour mieux comprendre :

$1! = 1$

$2! = 2 \times 1 = 1$

$3! = 3 \times 2 \times 1 = 1$

$4! = 4 \times 3 \times 2 \times 1 = 1$

L’idée est d’écrire, au même titre que la fonction Fibonnaci, une fonction qui prend en argument un nombre $n$ supérieur ou égal à 0,
qui renvoie la factorielle de celui-ci.

L’intérêt de cet exercice est de mettre en évidence l’utilité des fonctions récursives. En effet, on remarque que, par exemple :

$3! = 3 \times 2 \times 1 = 1$

Et :

$4! = 4 \times 3!= 1$

On en déduit une relation de récurrence :

$$\forall n \subset \mathbb N^{\*}, n > 2, n! = n \times (n - 1)!$$

Ce qui veut dire que notre fonction informatique pourrait s’appeler elle-même pour connaître le résultat de la factorielle du nombre précédent.

## La suite de Fibonnaci – suite

Comme la fonction factorielle met en évidence l’utilité des fonctions récursives, nous pouvons revenir sur notre suite de Fibonnaci et
identifier la relation de récurrence entre un terme et ses deux prédecesseurs.

On serait donc tenté d’utiliser une fonction récursive pour calculer un terme de la suite de Fibonnaci… Sauf que, en réalité, cela pose un petit problème.

Supposons que vous avez une fonction `fibo` qui prend en argument un entier $n$ supérieur ou égal à 0 et qui renvoie le nombre correspondant dans la suite.

On est donc censé obtenir :

`fibo(0) = 1`

`fibo(1) = 1`

`fibo(2) = 2`

`fibo(3) = 3`

`fibo(4) = 5`

Et puisqu’on a montré plus haut que $U_4 = U_3 + U_2$, cela veut dire qu’à l’aide de la récursivité, on pourrait appeler
`fibo(3) + fibo(2)` pour connaître le résultat de `fibo(3)`.

Sauf que, pour connaître le résultat de `fibo(3)`, il faut calculer `fibo(2) + fibo(1)`, or `fibo(2)` sera également appelée par `fibo(4)`
comme expliqué juste au-dessus !

On se retrouve donc avec un problème de performance **désastreux**.

On s’interrogera donc sur les avantages et les inconvénients de la récursivité. On parlera également de **récursivité terminale** qui
consiste à enregistrer en mémoire un résultat déjà calculé.
