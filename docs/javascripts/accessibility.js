// Retain Material's state bindings while exposing native keyboard controls.
document.querySelectorAll(
  '.md-header label[for="__drawer"], label[for="__search"], [data-md-component="palette"] label'
).forEach((control) => {
  if (control.classList.contains("md-search__overlay")) return;
  const name = control.title || (
    control.htmlFor === "__drawer" ? "Open chapter navigation" : "Toggle workshop search"
  );
  const button = document.createElement("button");
  button.type = "button";
  button.className = `${control.className} workshop-control`;
  button.innerHTML = control.innerHTML;
  button.title = name;
  button.setAttribute("aria-label", name);
  button.hidden = control.hidden;
  button.addEventListener("click", () => {
    document.getElementById(control.htmlFor).click();
    if (control.closest('[data-md-component="palette"]')) {
      requestAnimationFrame(() => {
        control.parentElement.querySelector(".workshop-control:not([hidden])").focus();
      });
    }
  });
  new MutationObserver(() => {
    button.hidden = control.hidden;
  }).observe(control, { attributes: true, attributeFilter: ["hidden"] });
  control.classList.add("workshop-control-label");
  control.setAttribute("aria-hidden", "true");
  control.after(button);
});
