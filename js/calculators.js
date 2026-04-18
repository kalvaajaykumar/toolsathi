document.addEventListener('DOMContentLoaded', () => {
  // Helper to show/hide error
  function showError(prefix, msg) {
    const box = document.getElementById(`${prefix}-error-box`);
    const txt = document.getElementById(`${prefix}-error-text`);
    const res = document.getElementById(`${prefix}-result-box`);
    if (box && txt) {
      txt.textContent = msg;
      box.style.display = 'block';
      if (res) res.style.display = 'none';
    }
  }

  function hideError(prefix) {
    const box = document.getElementById(`${prefix}-error-box`);
    if (box) box.style.display = 'none';
  }

  function showResult(prefix) {
    const box = document.getElementById(`${prefix}-result-box`);
    if (box) {
      box.style.display = 'block';
      box.classList.add('active');
    }
  }

  // 1. Age Calculator
  const ageForm = document.getElementById('age-form');
  if (ageForm) {
    ageForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const dobInput = document.getElementById('dob').value;
      
      if (!dobInput) {
        showError('age', 'Please enter your date of birth.');
        return;
      }

      const dob = new Date(dobInput);
      const today = new Date();

      if (dob > today) {
        showError('age', 'Date of birth cannot be in the future.');
        return;
      }
      
      hideError('age');

      let years = today.getFullYear() - dob.getFullYear();
      let months = today.getMonth() - dob.getMonth();
      let days = today.getDate() - dob.getDate();

      if (days < 0) {
        months--;
        const prevMonth = new Date(today.getFullYear(), today.getMonth(), 0);
        days += prevMonth.getDate();
      }

      if (months < 0) {
        years--;
        months += 12;
      }

      const totalDays = Math.floor((today.getTime() - dob.getTime()) / (1000 * 60 * 60 * 24));

      document.getElementById('age-result-years').textContent = years;
      document.getElementById('age-result-months').textContent = months;
      document.getElementById('age-result-days').textContent = days;
      
      const totalEl = document.getElementById('age-result-total');
      if(totalEl) totalEl.textContent = totalDays.toLocaleString();

      showResult('age');
    });
  }

  // 2. CGPA Calculator
  const cgpaForm = document.getElementById('cgpa-form');
  const addSubjectBtn = document.getElementById('add-subject-btn');
  const subjectsContainer = document.getElementById('subjects-container');
  
  if (cgpaForm) {
    let subjectCount = 3;

    if (addSubjectBtn) {
      addSubjectBtn.addEventListener('click', () => {
        subjectCount++;
        const div = document.createElement('div');
        div.className = 'form-group flex-between';
        div.innerHTML = `
          <input type="text" class="form-control" placeholder="Subject ${subjectCount}" style="width: 48%;">
          <input type="number" class="form-control gpa-input" placeholder="GPA (0-10)" step="0.01" min="0" max="10" required style="width: 48%;">
        `;
        subjectsContainer.appendChild(div);
      });
    }

    cgpaForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const inputs = document.querySelectorAll('.gpa-input');
      let totalGPA = 0;
      let validInputs = 0;
      let hasInvalid = false;

      inputs.forEach(input => {
        const val = parseFloat(input.value);
        if (isNaN(val) || val < 0 || val > 10) {
          hasInvalid = true;
        } else {
          totalGPA += val;
          validInputs++;
        }
      });

      if (hasInvalid || validInputs === 0) {
        showError('cgpa', 'Please enter valid GPA values (0-10) for all subjects.');
        return;
      }

      hideError('cgpa');
      let cgpa = (totalGPA / validInputs).toFixed(2);
      document.getElementById('cgpa-val').textContent = cgpa;
      showResult('cgpa');
    });
  }

  // 3. EMI Calculator
  const emiForm = document.getElementById('emi-form');
  if (emiForm) {
    emiForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const principal = parseFloat(document.getElementById('loan-amount').value);
      const annualRate = parseFloat(document.getElementById('interest-rate').value);
      const months = parseFloat(document.getElementById('duration-months').value);

      if (isNaN(principal) || principal <= 0 || isNaN(annualRate) || annualRate <= 0 || isNaN(months) || months <= 0) {
        showError('emi', 'Please enter valid positive numbers for all fields.');
        return;
      }

      hideError('emi');
      const r = annualRate / 12 / 100;
      const emi = (principal * r * Math.pow(1 + r, months)) / (Math.pow(1 + r, months) - 1);
      
      document.getElementById('emi-val').textContent = '₹' + emi.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2});
      showResult('emi');
    });
  }

  // 4. Percentage Calculator
  const percForm = document.getElementById('perc-form');
  if (percForm) {
    percForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const percent = parseFloat(document.getElementById('percent-input').value);
      const total = parseFloat(document.getElementById('total-input').value);

      if (isNaN(percent) || isNaN(total)) {
        showError('perc', 'Please enter valid numerical values.');
        return;
      }

      hideError('perc');
      const result = (percent / 100) * total;
      document.getElementById('perc-val').textContent = result.toFixed(2);
      showResult('perc');
    });
  }

  // 5. BMI Calculator
  const bmiForm = document.getElementById('bmi-form');
  if (bmiForm) {
    bmiForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const weight = parseFloat(document.getElementById('weight-input').value);
      const heightCm = parseFloat(document.getElementById('height-input').value);

      if (isNaN(weight) || weight <= 0 || isNaN(heightCm) || heightCm <= 0) {
        showError('bmi', 'Please enter a valid weight and height.');
        return;
      }

      hideError('bmi');
      const heightM = heightCm / 100;
      const bmi = weight / (heightM * heightM);
      let category = '';

      if (bmi < 18.5) category = 'Underweight';
      else if (bmi < 24.9) category = 'Normal weight';
      else if (bmi < 29.9) category = 'Overweight';
      else category = 'Obesity';

      document.getElementById('bmi-val').textContent = bmi.toFixed(1) + ' (' + category + ')';
      showResult('bmi');
    });
  }

  // 6. Discount Calculator
  const discountForm = document.getElementById('discount-form');
  if (discountForm) {
    discountForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const originalPrice = parseFloat(document.getElementById('original-price').value);
      const discountPercent = parseFloat(document.getElementById('discount-percent').value);

      if (isNaN(originalPrice) || originalPrice <= 0 || isNaN(discountPercent) || discountPercent < 0 || discountPercent > 100) {
        showError('discount', 'Please enter valid numbers (Discount: 0-100%).');
        return;
      }

      hideError('discount');
      const savings = (originalPrice * discountPercent) / 100;
      const finalPrice = originalPrice - savings;

      document.getElementById('discount-val').textContent = '₹' + finalPrice.toLocaleString('en-IN', {minimumFractionDigits: 2}) + ' (Saved: ₹' + savings.toLocaleString('en-IN') + ')';
      showResult('discount');
    });
  }

});
