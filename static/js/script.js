document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.getElementById("navToggle");
  var nav = document.querySelector(".site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      nav.classList.toggle("open");
    });
  }

  // Auto-dismiss flash messages
  document.querySelectorAll(".flash").forEach(function (el) {
    setTimeout(function () {
      el.style.transition = "opacity .4s ease";
      el.style.opacity = "0";
      setTimeout(function () { el.remove(); }, 400);
    }, 5000);
  });

  // Skill bar animation on load
  document.querySelectorAll(".skill-bar-fill").forEach(function (el) {
    var target = el.style.width;
    el.style.width = "0";
    requestAnimationFrame(function () {
      setTimeout(function () { el.style.transition = "width .8s ease"; el.style.width = target; }, 100);
    });
  });
});
