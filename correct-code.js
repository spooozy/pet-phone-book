class NumberProcessor {
	constructor(numbers) {
		this.numbers = numbers;
	}

	getEvenNumbers() {
		return this.numbers.filter((num) => num % 2 === 0);
	}
}

function processNumbersDemo() {
	const numbersArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
	const processor = new NumberProcessor(numbersArray);

	console.log("Исходный массив:", numbersArray);
	console.log("Чётные числа:", processor.getEvenNumbers());
	console.log("Сумма чисел:", processor.calculateSum());
}

processNumbersDemo();
