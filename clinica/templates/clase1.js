'use strict';

console.log('Hello world');

//concatenar : +
console.log('Hello' + 'World');

//format string
const nombre ='Johan';
const apellido ='Chevez';

console.log(`hello ${nombre} ${apellido}`);

// scope: ambito de las variables (locales y globales)
// var: tiene un scope global
// let : tiene un scope local( en el bloque donde fue declarada)
// const: igual que let, pero no permite reasignacion de valores a excepcion de listas y objetos

for( var i =1; i <= 5 ; i++)
{
	console.log(i);
}

console.log( 'Afuera del bucle : ' + i);

// console.log('Afuera del bucle ')

/*{
	 const n=50
	 n++;
	 console.log (n);
}*/

const n =["Javascript"]; //lista
const m ={'nombre':'Johan'};
n.push('C#');

console.log(n);