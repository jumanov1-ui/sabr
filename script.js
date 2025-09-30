const termRange = document.getElementById('term');
const termValue = document.getElementById('term-value');
const amountInput = document.getElementById('amount');
const monthlyOutput = document.getElementById('monthly');

function formatNumber(num) {
  return num.toLocaleString('uz-UZ');
}

function updateSummary() {
  const amount = Number(amountInput.value || 0);
  const term = Number(termRange.value);
  const rate = 0.12 / 12; // 12% annual

  const monthlyPayment = amount * (rate * Math.pow(1 + rate, term)) / (Math.pow(1 + rate, term) - 1 || 1);

  termValue.textContent = term;
  monthlyOutput.textContent = `${formatNumber(Math.round(monthlyPayment))} so'm`;
}

termRange?.addEventListener('input', updateSummary);
amountInput?.addEventListener('input', updateSummary);

document.getElementById('loan-form')?.addEventListener('submit', (event) => {
  event.preventDefault();
  alert('Arizangiz qabul qilindi! Tez orada menejerimiz bog\'lanadi.');
});

updateSummary();
