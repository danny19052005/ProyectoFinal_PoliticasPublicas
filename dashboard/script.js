(function () {
  "use strict";

  const DATA_URL = "data/resumen_dashboard_F01_F06.json";

  const state = {
    data: null,
    dimensionFilter: "all",
    hallazgoFilter: "all",
    fuenteTipoFilter: "all",
    fuenteDecisionFilter: "all"
  };

  function byId(id) {
    return document.getElementById(id);
  }

  function setText(el, text) {
    if (!el) return;
    el.textContent = String(text ?? "");
  }

  function clearNode(el) {
    if (!el) return;
    while (el.firstChild) {
      el.removeChild(el.firstChild);
    }
  }

  function toCodeLabel(code, name) {
    return code + " - " + name;
  }

  function statusClassForEstado(estado) {
    if (estado === "Evidencia suficiente") return "estado-suficiente";
    if (estado === "Evidencia parcial") return "estado-parcial";
    if (estado === "Evidencia limitada") return "estado-limitada";
    return "estado-sin";
  }

  function statusClassForNivel(nivel) {
    if (nivel === "Alto") return "nivel-alto";
    if (nivel === "Medio") return "nivel-medio";
    return "nivel-bajo";
  }

  function formatNumberEs(n) {
    return new Intl.NumberFormat("es-EC").format(Number(n));
  }

  function updateStatus(message, isError) {
    const box = byId("statusBox");
    if (!box) return;
    box.classList.toggle("error", Boolean(isError));
    setText(box, message);
  }

  function renderProyecto(data) {
    setText(byId("metaModalidad"), data.proyecto.modalidad);
    setText(byId("metaTerritorio"), data.proyecto.territorio);
    setText(byId("metaPeriodo"), data.proyecto.periodo_principal);
    setText(byId("preguntaCentral"), data.proyecto.pregunta_central);
    setText(byId("estadoGeneral"), data.estado_general);
    setText(byId("footerEstado"), "Estado general: " + data.estado_general);
  }

  function renderEstructura(data) {
    const estructura = data.estructura_planificada;
    const cards = byId("estructuraCards");
    const bars = byId("estructuraBars");
    const refs = byId("estructuraReferencias");

    clearNode(cards);
    clearNode(bars);
    clearNode(refs);

    const items = [
      { nombre: "Ejes", valor: estructura.ejes },
      { nombre: "Objetivos", valor: estructura.objetivos },
      { nombre: "Políticas", valor: estructura.politicas },
      { nombre: "Programas", valor: estructura.programas },
      { nombre: "Proyectos", valor: estructura.proyectos }
    ];

    items.forEach(function (item) {
      const card = document.createElement("article");
      card.className = "card";

      const h3 = document.createElement("h3");
      setText(h3, item.nombre);

      const p = document.createElement("p");
      p.className = "big-number";
      setText(p, String(item.valor));

      card.appendChild(h3);
      card.appendChild(p);
      cards.appendChild(card);
    });

    const max = Math.max.apply(null, items.map(function (it) { return Number(it.valor); }));

    items.forEach(function (item) {
      const barItem = document.createElement("div");
      barItem.className = "bar-item";

      const value = document.createElement("div");
      value.className = "bar-value";
      setText(value, String(item.valor));

      const track = document.createElement("div");
      track.className = "bar-track";

      const fill = document.createElement("div");
      fill.className = "bar-fill";
      fill.style.height = "0%";

      const label = document.createElement("div");
      label.className = "bar-label";
      setText(label, item.nombre);

      track.appendChild(fill);
      barItem.appendChild(value);
      barItem.appendChild(track);
      barItem.appendChild(label);
      bars.appendChild(barItem);

      requestAnimationFrame(function () {
        const pct = Math.round((Number(item.valor) / max) * 100);
        fill.style.height = String(pct) + "%";
      });
    });

    estructura.verificacion.forEach(function (ref) {
      const li = document.createElement("li");
      setText(li, ref);
      refs.appendChild(li);
    });
  }

  function renderDimensiones() {
    const container = byId("dimensionesList");
    const empty = byId("dimensionesEmpty");

    clearNode(container);

    const filtered = state.data.dimensiones.filter(function (dim) {
      return state.dimensionFilter === "all" || dim.estado_evidencia === state.dimensionFilter;
    });

    filtered.forEach(function (dim) {
      const card = document.createElement("article");
      card.className = "card dim-card";

      const title = document.createElement("h3");
      setText(title, toCodeLabel(dim.codigo, dim.nombre));

      const meta = document.createElement("div");
      meta.className = "dim-meta";

      const estado = document.createElement("span");
      estado.className = "chip " + statusClassForEstado(dim.estado_evidencia);
      setText(estado, dim.estado_evidencia);

      const fuentes = document.createElement("span");
      fuentes.className = "chip";
      setText(fuentes, "Fuentes: " + dim.fuentes.join(", "));

      meta.appendChild(estado);
      meta.appendChild(fuentes);

      const hallazgo = document.createElement("p");
      setText(hallazgo, dim.hallazgo);

      const limit = document.createElement("p");
      limit.className = "muted";
      setText(limit, "Limitación: " + dim.limitacion);

      card.appendChild(title);
      card.appendChild(meta);
      card.appendChild(hallazgo);
      card.appendChild(limit);
      container.appendChild(card);
    });

    empty.classList.toggle("hidden", filtered.length !== 0);
  }

  function renderHallazgos() {
    const container = byId("hallazgosList");
    const empty = byId("hallazgosEmpty");

    clearNode(container);

    const filtered = state.data.hallazgos_principales.filter(function (h) {
      return state.hallazgoFilter === "all" || h.nivel_confianza === state.hallazgoFilter;
    });

    filtered.forEach(function (h) {
      const card = document.createElement("article");
      card.className = "card hallazgo-card";

      const title = document.createElement("h3");
      setText(title, h.codigo);

      const meta = document.createElement("div");
      meta.className = "hallazgo-meta";

      const nivel = document.createElement("span");
      nivel.className = "chip " + statusClassForNivel(h.nivel_confianza);
      setText(nivel, "Nivel: " + h.nivel_confianza);

      const fuentes = document.createElement("span");
      fuentes.className = "chip";
      setText(fuentes, "Fuentes: " + h.fuentes.join(", "));

      meta.appendChild(nivel);
      meta.appendChild(fuentes);

      const texto = document.createElement("p");
      setText(texto, h.texto);

      const adv = document.createElement("p");
      adv.className = "muted";
      setText(adv, "Advertencia: " + h.advertencia);

      card.appendChild(title);
      card.appendChild(meta);
      card.appendChild(texto);
      card.appendChild(adv);
      container.appendChild(card);
    });

    empty.classList.toggle("hidden", filtered.length !== 0);
  }

  function renderIndicador(data) {
    const ind = data.indicadores_contextuales[0];
    setText(byId("indicadorValor"), formatNumberEs(ind.valor));
    setText(byId("indicadorDescripcion"), "Emergencias coordinadas asociadas a la localidad Quito en 2024, según la clasificación utilizada por la fuente.");
    setText(byId("indicadorFuente"), ind.fuente);
  }

  function fillFuenteFilters(data) {
    const tipoSelect = byId("filterFuenteTipo");
    const decisionSelect = byId("filterFuenteDecision");

    const tipos = Array.from(new Set(data.fuentes.map(function (f) { return f.tipo; })));
    const decisiones = Array.from(new Set(data.fuentes.map(function (f) { return f.decision; })));

    tipos.forEach(function (tipo) {
      const opt = document.createElement("option");
      opt.value = tipo;
      setText(opt, tipo);
      tipoSelect.appendChild(opt);
    });

    decisiones.forEach(function (dec) {
      const opt = document.createElement("option");
      opt.value = dec;
      setText(opt, dec);
      decisionSelect.appendChild(opt);
    });
  }

  function renderFuentes() {
    const body = byId("fuentesBody");
    const empty = byId("fuentesEmpty");
    clearNode(body);

    const filtered = state.data.fuentes.filter(function (f) {
      const okTipo = state.fuenteTipoFilter === "all" || f.tipo === state.fuenteTipoFilter;
      const okDecision = state.fuenteDecisionFilter === "all" || f.decision === state.fuenteDecisionFilter;
      return okTipo && okDecision;
    });

    filtered.forEach(function (f) {
      const tr = document.createElement("tr");

      const c1 = document.createElement("td");
      setText(c1, f.codigo);
      const c2 = document.createElement("td");
      setText(c2, f.tipo);
      const c3 = document.createElement("td");
      setText(c3, f.decision);
      const c4 = document.createElement("td");
      setText(c4, f.utilidad);
      const c5 = document.createElement("td");
      setText(c5, f.limitacion);

      tr.appendChild(c1);
      tr.appendChild(c2);
      tr.appendChild(c3);
      tr.appendChild(c4);
      tr.appendChild(c5);
      body.appendChild(tr);
    });

    empty.classList.toggle("hidden", filtered.length !== 0);
  }

  function renderLists(data) {
    const limits = byId("limitacionesList");
    const warns = byId("advertenciasList");

    clearNode(limits);
    clearNode(warns);

    const fixedLimitations = [
      "Posible subregistro de delitos",
      "Diferencias de definición y periodo",
      "Falta de desagregación territorial",
      "Información presupuestaria incompleta",
      "F04 sin cifras verificadas específicas de Quito en el texto analizado",
      "F05 correspondiente a 2011",
      "F06 como registro operativo de emergencias y no de delitos",
      "Imposibilidad de atribuir cambios a una sola institución sin diseño causal"
    ];

    fixedLimitations.forEach(function (text) {
      const li = document.createElement("li");
      setText(li, text);
      limits.appendChild(li);
    });

    data.advertencias_metodologicas.forEach(function (text) {
      const li = document.createElement("li");
      setText(li, text);
      warns.appendChild(li);
    });
  }

  function validateData(data) {
    const dimCount = Array.isArray(data.dimensiones) ? data.dimensiones.length : 0;
    const hiCount = Array.isArray(data.hallazgos_principales) ? data.hallazgos_principales.length : 0;
    const fuenteCount = Array.isArray(data.fuentes) ? data.fuentes.length : 0;
    if (dimCount < 11 || hiCount < 11 || fuenteCount < 6) {
      throw new Error("El resumen cargado no contiene todas las secciones mínimas esperadas.");
    }
  }

  function bindEvents() {
    const dimFilter = byId("filterDimensionEstado");
    const hallFilter = byId("filterHallazgoNivel");
    const tipoFilter = byId("filterFuenteTipo");
    const decFilter = byId("filterFuenteDecision");

    dimFilter.addEventListener("change", function () {
      state.dimensionFilter = dimFilter.value;
      renderDimensiones();
    });

    hallFilter.addEventListener("change", function () {
      state.hallazgoFilter = hallFilter.value;
      renderHallazgos();
    });

    tipoFilter.addEventListener("change", function () {
      state.fuenteTipoFilter = tipoFilter.value;
      renderFuentes();
    });

    decFilter.addEventListener("change", function () {
      state.fuenteDecisionFilter = decFilter.value;
      renderFuentes();
    });

    const menuBtn = byId("menuToggle");
    const nav = byId("mainNav");
    menuBtn.addEventListener("click", function () {
      const willOpen = !nav.classList.contains("open");
      nav.classList.toggle("open", willOpen);
      menuBtn.setAttribute("aria-expanded", willOpen ? "true" : "false");
    });

    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        if (window.innerWidth <= 930) {
          nav.classList.remove("open");
          menuBtn.setAttribute("aria-expanded", "false");
        }
      });
    });

    const topBtn = byId("toTopBtn");
    window.addEventListener("scroll", function () {
      topBtn.classList.toggle("show", window.scrollY > 320);
    });
    topBtn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    setText(byId("yearNow"), String(new Date().getFullYear()));
  }

  async function init() {
    bindEvents();

    try {
      updateStatus("Cargando resumen auditado...", false);

      const response = await fetch(DATA_URL, { cache: "no-store" });
      if (!response.ok) {
        throw new Error("Respuesta no exitosa: " + response.status);
      }

      const data = await response.json();
      validateData(data);

      state.data = data;

      renderProyecto(data);
      renderEstructura(data);
      renderDimensiones();
      renderHallazgos();
      renderIndicador(data);
      fillFuenteFilters(data);
      renderFuentes();
      renderLists(data);

      updateStatus("Resumen auditado cargado correctamente.", false);
    } catch (err) {
      updateStatus("No fue posible cargar el resumen de datos. Verifique que el dashboard se esté ejecutando mediante un servidor local o desde Vercel.", true);
      console.error(err);
    }
  }

  document.addEventListener("DOMContentLoaded", init);
})();
