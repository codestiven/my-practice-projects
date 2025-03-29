

const names = ["Stiven", "Carlos", "María", "Andrés", "Lucía","aaaaaaa"];



function createFrame(names) {
    let salida = "";

    const longest = names.reduce((a, b) => (a.length > b.length ? a : b));

    salida += "*".repeat(longest.length + 4) + "\n";
    for (let i = 0; i < names.length; i++) {


        let spaces = longest.length - names[i].length;
        while (spaces > 0) {
            names[i] += " ";
            spaces--;
        }

        salida += "* " + names[i] + " *\n";
    }
    salida += "*".repeat(longest.length + 4);

    return salida;


}

console.log(createFrame(['midu', 'madeval', 'educalvolpz']));

