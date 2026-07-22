const structureData = [
  { label: "Ejes", value: 4 },
  { label: "Objetivos", value: 5 },
  { label: "Políticas", value: 8 },
  { label: "Programas", value: 15 },
  { label: "Proyectos", value: 27 }
];

function renderStructureCards() {
  const cardsContainer = document.getElementById("structure-cards");
  if (!cardsContainer) return;

  cardsContainer.innerHTML = "";

  structureData.forEach((item) => {
    const card = document.createElement("article");
    card.className = "card stat";
    card.innerHTML = `<h3>${item.label}</h3><p><strong>${item.value}</strong></p>`;
    cardsContainer.appendChild(card);
  });
}

function renderBarsChart() {
  const chart = document.getElementById("bars-chart");
  if (!chart) return;

  chart.innerHTML = "";
  const maxValue = Math.max(...structureData.map((d) => d.value));

  structureData.forEach((item) => {
    const barItem = document.createElement("div");
    barItem.className = "bar-item";

    const value = document.createElement("div");
    value.className = "bar-value";
    value.textContent = String(item.value);

    const track = document.createElement("div");
    track.className = "bar-track";

    const fill = document.createElement("div");
    fill.className = "bar-fill";
    fill.style.height = "0%";
    fill.setAttribute("aria-hidden", "true");

    track.appendChild(fill);

    const label = document.createElement("div");
    label.className = "bar-label";
    label.textContent = item.label;

    barItem.appendChild(value);
    barItem.appendChild(track);
    barItem.appendChild(label);
    chart.appendChild(barItem);

    requestAnimationFrame(() => {
      const heightPercent = (item.value / maxValue) * 100;
      fill.style.height = `${heightPercent}%`;
    });
  });
}

function enableSourceFilter() {
  const filter = document.getElementById("state-filter");
  const rows = document.querySelectorAll("#sources-table tbody tr");
  if (!filter || rows.length === 0) return;

  filter.addEventListener("change", () => {
    const selected = filter.value;
    rows.forEach((row) => {
      const state = row.getAttribute("data-state") || "";
      row.style.display = selected === "all" || state === selected ? "" : "none";
    });
  });
}

function enableSmoothNavigation() {
  const links = document.querySelectorAll('.nav-links a[href^="#"]');
  links.forEach((link) => {
    link.addEventListener("click", (event) => {
      const targetId = link.getAttribute("href");
      if (!targetId) return;
      const target = document.querySelector(targetId);
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
}

function setFooterYear() {
  const yearEl = document.getElementById("current-year");
  if (!yearEl) return;
  yearEl.textContent = String(new Date().getFullYear());
}

document.addEventListener("DOMContentLoaded", () => {
  renderStructureCards();
  renderBarsChart();
  enableSourceFilter();
  enableSmoothNavigation();
  setFooterYear();
});