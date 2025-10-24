
// Optional: Change button text when toggled
const checkbox = document.getElementById('toggleBtn');
const label = document.querySelector('label[for="toggleBtn"]');

checkbox.addEventListener('change', () => {
  if (checkbox.checked) {
    label.textContent = 'Sale ✅';
    label.classList.remove('btn-outline-primary');
    label.classList.add('btn-primary');
  } else {
    label.textContent = 'Sale';
    label.classList.remove('btn-primary');
    label.classList.add('btn-outline-primary');
  }
}); const mainShoe = document.getElementById("mainShoe");
const sideIcons = document.querySelectorAll(".side-icons img");
let index = 0;

// function copyMenu() {
//   var dptCategory = document.querySelector('.dpt-cat');
//   var dptPlace = document.querySelector('.deparments');
//   dptPlace.innerHTML = dptCategory.innerHTML;
//   var mainNav = document.querySelector('.header-nav nav');
//   var navPlace = document.querySelector('.off-canvas nav');
//   navPlace.innerHTML = mainNav.innerHTML;
//   var topNav = document.querySelector('.header-top .wrapper');
//   var topPlace = document.querySelector('.off-canvas .thetop-nav');
//   topPlace.innerHTML = topNav.innerHTML;
// }
// copyMenu();

// const submenu = document.querySelector('.has-child .icon-smell');
// submenu.forEach((menu) => menu.addEventListener('click', toggle));

// function toggle(e){
//   e.preventDafault();
//   submenu.forEach((item) => item != this ? item.closest('.has-child').classList.remove('expand') : null);

//   if (this.closest('.has-child').classList != 'expand');
//   this.closest('.has-child').classList.toggle('expand')
// }


