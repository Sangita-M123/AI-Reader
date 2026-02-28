// Sample JavaScript Code for Testing

// Function to greet a user
function greetUser(name) {
  console.log("Hello, " + name + "!");
  return "Welcome to AI Document Reader";
}

// Function to calculate sum of array
function calculateSum(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
}

// Class for Document Processing
class DocumentProcessor {
  constructor(fileName) {
    this.fileName = fileName;
    this.processed = false;
  }

  process() {
    console.log("Processing: " + this.fileName);
    this.processed = true;
    return "Document processed successfully";
  }

  getStatus() {
    return this.processed ? "Completed" : "Pending";
  }
}

// Main execution
const user = "Developer";
greetUser(user);

const numbers = [1, 2, 3, 4, 5];
const total = calculateSum(numbers);
console.log("Total: " + total);

const doc = new DocumentProcessor("sample.pdf");
doc.process();
console.log("Status: " + doc.getStatus());