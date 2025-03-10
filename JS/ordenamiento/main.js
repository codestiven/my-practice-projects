/* Dado un array de enteros no ordenado llamado 
 nums, devuelve el entero positivo más pequeño que falte. */

const nums = [3, 7, 1, 2, 8, 5, 10, 6, 12, 14, 11, 9, 13, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0];

function smallestMissingPositive(nums) {
    // Filtramos solo los positivos y eliminamos duplicados con Set
    const set = new Set(nums.filter(num => num > 0));

    // Buscamos el primer número positivo que falta
    for (let i = 1; i <= nums.length + 1; i++) {
        if (!set.has(i)) {
            return i;
        }
    }
}

console.log(smallestMissingPositive(nums)); // Salida esperada: 16
