document.addEventListener('DOMContentLoaded', function() {
    let currentStep = 0;
    const steps = document.querySelectorAll('.step');
    const progressBar = document.getElementById('progress');

    function showStep(n) {
        steps[n].style.display = 'block';
        updateProgressBar();
    }

    function hideStep(n) {
        steps[n].style.display = 'none';
    }

    function updateProgressBar() {
        const progressPercentage = (currentStep / (steps.length - 1)) * 100;
        progressBar.style.width = progressPercentage + '%';
    }

    function nextStep() {
        // Valider les champs de l'étape actuelle
        const inputs = steps[currentStep].querySelectorAll('input');
        let valid = true;
        inputs.forEach(input => {
            if (!input.checkValidity()) {
                input.reportValidity();
                valid = false;
            }
        });
        if (valid) {
            hideStep(currentStep);
            currentStep++;
            if (currentStep < steps.length) {
                showStep(currentStep);
            }
        }
    }

    function prevStep() {
        hideStep(currentStep);
        currentStep--;
        showStep(currentStep);
    }

    // Fonction pour mettre à jour la valeur du slider
    function updateSliderValue(sliderId) {
        const slider = document.getElementById(sliderId);
        const valueSpan = document.getElementById(sliderId + '_value');
        valueSpan.textContent = slider.value;
    }

    // Initialisation : afficher la première étape
    showStep(currentStep);

    // Rendre les fonctions accessibles depuis le HTML
    window.nextStep = nextStep;
    window.prevStep = prevStep;
    window.updateSliderValue = updateSliderValue;

    // Initialiser les valeurs des sliders
    updateSliderValue('retention_rate');
    updateSliderValue('conversion_rate');
    updateSliderValue('fcr_rate');
    updateSliderValue('churn_rate');
});