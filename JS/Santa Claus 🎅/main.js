

gifts = [3, 7, 12, 5, 8, 3, 9, 12, 6, 5, 15, 7, 14, 9, 10, 8, 6, 11, 14, 10, 22];
salida = [];


function eliminarDuplicados(gifts) {
    for (let i = 0; i < gifts.length; i++) {
        if (!salida.includes(gifts[i])) {
            salida.push(gifts[i]);
        }
    }

    return salida.sort((a, b) => a - b);


}

console.log(eliminarDuplicados(gifts));