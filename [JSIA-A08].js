//Objetos literais em JavaScript são estruturas que permitem agrupar dados e comportamentos 
// (propriedades e métodos) dentro de um mesmo conjunto. Eles são criados de forma simples, 
// usando chaves {}, e são muito usados para representar entidades do mundo real — como um aluno, 
// um carro, um produto etc.


// Definição do objeto literal
const aluno = {
  nome: "Samir",
  notas: [8, 9, 7],

  // Método que calcula a média das notas
  calcularMedia() {
    const soma = this.notas.reduce((total, nota) => total + nota, 0);
    return soma / this.notas.length;
  }
};

// --- Desestruturação ---
// Extrai a propriedade 'nome' do objeto aluno
const { nome } = aluno;
console.log(`Nome do aluno: ${nome}`);

// --- Spread Operator ---
// Cria um novo array de notas, adicionando uma nova nota
const novasNotas = [...aluno.notas, 10];
console.log("Notas originais:", aluno.notas);
console.log("Novas notas:", novasNotas);

// Calculando a média com o método
console.log(`Média do aluno: ${aluno.calcularMedia()}`);