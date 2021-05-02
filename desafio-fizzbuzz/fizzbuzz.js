//Programa baseado no desafio contido no vídeo "FizzBuzz: One Simple Interview Question", por Tom Scott.

/*O programa consiste em declarar a palavra "Fizz" para múltiplos de 3 e "Buzz" para múltiplos de 5. Caso um número seja múltiplo de ambos, passa então a se declarar "FizzBuzz". O programa é originalmente feito para expressar estas declarações entre 1 e 100, porém, pode facilmente ser alterado para que declare-se mais ou menos números.*/


for (num = 1; num <= 100; num++){
    let n1 = 3
    let n2 = 5
    if ((num % n1 == 0) && (num % n2 == 0)){
        console.log('FizzBuzz')
    } 
    else if (num % n1 == 0){
        console.log('Fizz')
    }
    else if (num % n2 == 0){
        console.log('Buzz')
    } else {
        console.log(num)
    }
}

/*Com esta solução, não há necessidade de diversas alterações no código em caso de mudança nos múltiplos (3 e 5, no exemplo). Ao declará-los enquanto variáveis, pode-se alterar apenas n1 e n2 como se bem entenda e o programa funcionará de acordo com o esperado, modificando apenas um único elemento e sem necessidade de mais programação de else statements, permitindo grande flexibilização.*/





/*for (num = 1; num <= 100; num++){
    if ((num % 3 == 0) && (num % 5 == 0)){
        console.log('FizzBuzz')
    } 
    else if(num % 3 == 0){
        console.log('Fizz')
    }
    else if(num % 5 == 0){
        console.log('Buzz')
    } else {
        console.log(num)
    }
}
*/