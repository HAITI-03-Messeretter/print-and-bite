// PRINT&BITE Design-System - kleines Verhalten für die Mockups.
// Klassisches Script (kein ES-Modul), damit die Seiten auch per Doppelklick (file://) laufen.
(function () {
  document.documentElement.classList.add("js");

  // Scroll-Reveal: Elemente mit [data-reveal] blenden beim Hereinscrollen ein.
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealables = document.querySelectorAll("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    revealables.forEach(function (el) {
      el.classList.add("is-visible");
    });
  } else {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -10% 0px", threshold: 0.12 }
    );
    revealables.forEach(function (el) {
      observer.observe(el);
    });
  }

  // Mini-Quiz: <div data-quiz data-feedback-correct="..." data-feedback-wrong="...">
  document.querySelectorAll("[data-quiz]").forEach(function (quiz) {
    var feedback = quiz.querySelector(".ds-quiz__feedback");
    quiz.querySelectorAll(".ds-quiz__option").forEach(function (option) {
      option.setAttribute("aria-pressed", "false");
      option.addEventListener("click", function () {
        quiz.querySelectorAll(".ds-quiz__option").forEach(function (o) {
          o.setAttribute("aria-pressed", "false");
        });
        option.setAttribute("aria-pressed", "true");
        var correct = option.getAttribute("data-correct") === "true";
        quiz.setAttribute("data-answered", correct ? "correct" : "wrong");
        if (feedback) {
          feedback.hidden = false;
          feedback.textContent = quiz.getAttribute(correct ? "data-feedback-correct" : "data-feedback-wrong");
        }
      });
    });
  });

  // Mobiles Menü schließen, sobald ein Link gewählt wurde.
  document.querySelectorAll(".ds-menu").forEach(function (menu) {
    menu.addEventListener("click", function (event) {
      if (event.target.closest("a")) menu.removeAttribute("open");
    });
  });

  // Präsentation: Pfeiltasten wechseln zwischen den Mockups (Links mit rel="prev"/"next" in .ds-mockbar).
  document.addEventListener("keydown", function (event) {
    if (event.altKey || event.ctrlKey || event.metaKey) return;
    if (event.target.closest("input, textarea, select, [contenteditable]")) return;
    var rel = event.key === "ArrowRight" ? "next" : event.key === "ArrowLeft" ? "prev" : null;
    if (!rel) return;
    var link = document.querySelector('.ds-mockbar a[rel="' + rel + '"]');
    if (link) window.location.href = link.href;
  });
})();
