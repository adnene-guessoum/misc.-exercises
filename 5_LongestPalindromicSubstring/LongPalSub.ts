/**
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.
 **/

function longestPalindrome(s: string): string {
	// initialisation resultat par default: pas de palindrome substring
	let resultat = "";
	let max = 0;

	// boucle pour verifier egalité des lettres à droite et à gauche
	for (let i = 0; i < s.length; i++) {
		let gauche = i;
		let droite = i;

		//GENERAL: tant que lettre à droite est même que lettre à gauche -> OK

		// cas impaires (aba)
		while (gauche >= 0 && droite < s.length && s[gauche] === s[droite]) {
			if (droite - gauche + 1 > max) {
				// changer substring le plus long (resultat)
				resultat = s.slice(gauche, droite + 1);
				max = droite - gauche + 1;
			}
			gauche -= 1;
			droite += 1;
		}

		// cas paires (abba)
		gauche = i;
		droite = i+1;
		while (gauche >= 0 && droite < s.length && s[gauche]===s[droite]) {
			if (droite - gauche + 1 > max) {
				// changer substring le plus long (resultat)
				resultat = s.slice(gauche, droite + 1);
				max = droite - gauche + 1;
			}
			gauche -= 1;
			droite += 1;
		}
	}
	return resultat;
}
