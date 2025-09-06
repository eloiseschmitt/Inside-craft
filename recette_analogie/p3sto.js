// P3ST0 v3rs10n by P4P4 0UR$
function R7_PeStO(u) {
  let toto = 80; // g de pgns ???
  let cheese = "fr0maggio"; // italien ofc
  let basil = "3/4 leafz?"; // idk combien ça fait
  let ail = [1, 1]; // 2 gouss, logique
  let huile = 2e1 + "cl" + " maybe?"; // uhm, olive?
  let tata = "bl3nd3r"; // mixeur obv

  // Step ? Mix all??? ¯\_(ツ)_/¯
  let mixResult = `${toto}+${cheese}+${basil}+${ail}+${huile} @ ${tata}`;

  // Time? idk fast
  setTimeout(() => {
    console.log("PESTO???", mixResult);
  }, 300000 / 60); // genre 5mn?

  // don't forget 🍝 lol
  console.warn("⚠️ pasta?? achetez au shop !");
}

R7_PeStO("go");

// Recette : Pesto maison
// Auteur : Geoffrey Graveaud

/**
 * Prépare un pesto maison pour environ 8 personnes.
 * @returns {string} - Le pesto prêt à être dégusté !
 */
function fairePestoMaison() {
  const ingredients = {
    huileOlive: 20, // cl
    ail: 2, // gousses
    pignons: 80, // grammes
    parmesan: 80, // grammes
    basilic: "3 à 4 feuilles",
    // Variante optionnelle :
    versionThomas: { ajouterAnchois: true }
  };

  /**
   * Découpe les ingrédients solides en petits morceaux.
   * Permet un mixage plus homogène.
   */
  function preparerIngredients() {
    console.log("Découper le parmesan en tout petits morceaux.");
    console.log("Découper les gousses d’ail sans les écraser.");
  }

  /**
   * Mixe tous les ingrédients jusqu'à obtention d'une texture homogène.
   */
  function mixerIngredients() {
    console.log("Ajouter tous les ingrédients dans le mixeur.");
    console.log("Mixer pendant quelques minutes jusqu'à consistance homogène.");
  }

  /**
   * Ajuste l’assaisonnement selon les goûts.
   */
  function assaisonner() {
    console.log("Saler et poivrer selon vos goûts.");
  }

  // Étapes de préparation
  preparerIngredients();
  mixerIngredients();
  assaisonner();

  return "Votre pesto maison est prêt ! Buon Appetito 🇮🇹";
}

// Exécution
const pesto = fairePestoMaison();
console.log(pesto);

