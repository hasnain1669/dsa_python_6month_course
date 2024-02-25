const menuBtn = document.querySelector('#menu-btn');
const nav = document.querySelector('#nav');

menuBtn.addEventListener('click', () => {
  nav.classList.toggle('open');
});

// Add smooth scrolling to navigation links
document.querySelectorAll('nav a').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const targetId = link.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    const targetPosition = targetElement.offsetTop;
    window.scrollTo({
      top: targetPosition,
      behavior: 'smooth'
    });
    nav.classList.remove('open');
  });
});

// Add form validation
const form = document.querySelector('form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const messageInput = document.querySelector('#message');

form.addEventListener('submit', e => {
  e.preventDefault();

  if (!nameInput.value || !emailInput.value || !messageInput.value) {
    alert('Please fill out all fields.');
    return;
  }

  if (!validateEmail(emailInput.value)) {
    alert('Please enter a valid email address.');
    return;
  }

  alert('Message sent successfully!');
});

function validateEmail(email) {
  const re