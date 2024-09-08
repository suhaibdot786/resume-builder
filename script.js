// script.ts
var toggleSkillsButton = document.getElementById('toggle-skills');
var skillsSection = document.getElementById('skills');
// Check if both elements are found before adding the event listener
if (toggleSkillsButton && skillsSection) {
    toggleSkillsButton.addEventListener('click', function () {
        // Toggle the visibility of the skills section
        if (skillsSection.style.display === 'none') {
            skillsSection.style.display = 'block';
        }
        else {
            skillsSection.style.display = 'none';
        }
    });
}
else {
    console.error('Skills section or toggle button not found');
}
