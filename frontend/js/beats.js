(function () {
  "use strict";

  const popularContainer = document.getElementById("popular-beats");
  const latestContainer = document.getElementById("latest-beats");

  function createBeatCard(beat) {
    const card = document.createElement("article");
    card.className = "beat-card";

    const img = document.createElement("img");
    img.src = beat.thumbnail;
    img.alt = beat.title;
    img.loading = "lazy";

    const title = document.createElement("h4");
    title.className = "beat-card-title";
    title.textContent = beat.title;

    const link = document.createElement("a");
    link.className = "beat-card-link";
    link.href = beat.url;
    link.target = "_blank";
    link.rel = "noopener";
    link.textContent = "Ver en YouTube";

    card.append(img, title, link);
    return card;
  }

  function showMessage(container, message) {
    const p = document.createElement("p");
    p.textContent = message;
    container.replaceChildren(p);
  }

  function renderBeats(container, beats) {
    if (beats.length === 0) {
      showMessage(container, "No hay beats disponibles.");
      return;
    }
    container.replaceChildren(...beats.map(createBeatCard));
  }

  async function loadSection(container, loader) {
    showMessage(container, "Cargando beats...");
    try {
      const beats = await loader();
      renderBeats(container, beats);
    } catch (error) {
      console.error("Error al cargar beats:", error);
      showMessage(container, "No se pudieron cargar los beats.");
    }
  }

  loadSection(popularContainer, window.BeatsAPI.getPopular);
  loadSection(latestContainer, window.BeatsAPI.getLatest);
})();