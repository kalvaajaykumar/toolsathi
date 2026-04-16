// Calculator Logic

document.addEventListener('DOMContentLoaded', () => {

  // 1. Age Calculator
  const ageForm = document.getElementById('age-form');
  if (ageForm) {
    ageForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const dobInput = document.getElementById('dob').value;
      const errBox = document.getElementById('age-error-box');
      const errText = document.getElementById('age-error-text');

      if (!dobInput) {
        if(errBox) { errBox.style.display = 'block'; errText.textContent = 'Please enter your date of birth.'; }
        return;
      }

      const dob = new Date(dobInput);
      const today = new Date();

      if (dob > today) {
        if(errBox) { errBox.style.display = 'block'; errText.textContent = 'Date of birth cannot be in the future.'; }
        return;
      }
      
      if(errBox) errBox.style.display = 'none';

      let years = today.getFullYear() - dob.getFullYear();
      let months = today.getMonth() - dob.getMonth();
      let days = today.getDate() - dob.getDate();

      if (days < 0) {
        months--;
        // Get days in previous month
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

      document.getElementById('age-result-box').classList.add('active');
      document.getElementById('age-result-box').style.display = 'block';
    });
  }

  // 2. CGPA Calculator
  const cgpaForm = document.getElementById('cgpa-form');
  const addSubjectBtn = document.getElementById('add-subject-btn');
  const subjectsContainer = document.getElementById('subjects-container');
  
  if (cgpaForm) {
    let subjectCount = 3; // Default 3 inputs

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

    cgpaForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const inputs = document.querySelectorAll('.gpa-input');
      let totalGPA = 0;
      let validInputs = 0;

      inputs.forEach(input => {
        const val = parseFloat(input.value);
        if (!isNaN(val)) {
          totalGPA += val;
          validInputs++;
        }
      });

      if (validInputs > 0) {
        let cgpa = (totalGPA / validInputs).toFixed(2);
        document.getElementById('cgpa-val').textContent = cgpa;
        document.getElementById('cgpa-result-box').classList.add('active');
      }
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

      if (principal > 0 && annualRate > 0 && months > 0) {
        const r = annualRate / 12 / 100;
        const emi = (principal * r * Math.pow(1 + r, months)) / (Math.pow(1 + r, months) - 1);
        
        document.getElementById('emi-val').textContent = '₹' + emi.toFixed(2);
        document.getElementById('emi-result-box').classList.add('active');
      }
    });
  }

  // 4. Percentage Calculator
  const percForm = document.getElementById('perc-form');
  if (percForm) {
    percForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const percent = parseFloat(document.getElementById('percent-input').value);
      const total = parseFloat(document.getElementById('total-input').value);

      if (!isNaN(percent) && !isNaN(total)) {
        const result = (percent / 100) * total;
        document.getElementById('perc-val').textContent = result.toFixed(2);
        document.getElementById('perc-result-box').classList.add('active');
      }
    });
  }

  // 5. BMI Calculator
  const bmiForm = document.getElementById('bmi-form');
  if (bmiForm) {
    bmiForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const weight = parseFloat(document.getElementById('weight-input').value);
      const heightCm = parseFloat(document.getElementById('height-input').value);

      if (weight > 0 && heightCm > 0) {
        const heightM = heightCm / 100;
        const bmi = weight / (heightM * heightM);
        let category = '';

        if (bmi < 18.5) category = 'Underweight';
        else if (bmi < 24.9) category = 'Normal weight';
        else if (bmi < 29.9) category = 'Overweight';
        else category = 'Obesity';

        document.getElementById('bmi-val').textContent = bmi.toFixed(1) + ' (' + category + ')';
        document.getElementById('bmi-result-box').classList.add('active');
      }
    });
  }

  // 6. Discount Calculator
  const discountForm = document.getElementById('discount-form');
  if (discountForm) {
    discountForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const originalPrice = parseFloat(document.getElementById('original-price').value);
      const discountPercent = parseFloat(document.getElementById('discount-percent').value);

      if (originalPrice > 0 && discountPercent >= 0) {
        const savings = (originalPrice * discountPercent) / 100;
        const finalPrice = originalPrice - savings;

        document.getElementById('discount-val').textContent = '₹' + finalPrice.toFixed(2) + ' (Saved: ₹' + savings.toFixed(2) + ')';
        document.getElementById('discount-result-box').classList.add('active');
      }
    });
  }

});
