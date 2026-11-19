(function () {
  "use strict";

  const POPULAR_LIMIT = 5;
  const LATEST_LIMIT = 24;

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

  function renderBeats(container, beats) {
    container.replaceChildren(...beats.map(createBeatCard));
  }

  function renderEmptyState(container, message) {
    const p = document.createElement("p");
    p.textContent = message;
    container.replaceChildren(p);
  }

  function init(beats) {
    const popularContainer = document.getElementById("popular-beats");
    const latestContainer = document.getElementById("latest-beats");

    if (!Array.isArray(beats) || beats.length === 0) {
      renderEmptyState(popularContainer, "No hay beats disponibles.");
      renderEmptyState(latestContainer, "No hay beats disponibles.");
      return;
    }

    const popular = [...beats]
      .sort((a, b) => b.viewCount - a.viewCount)
      .slice(0, POPULAR_LIMIT);

    const latest = [...beats]
      .sort((a, b) => new Date(b.publishedAt) - new Date(a.publishedAt))
      .slice(0, LATEST_LIMIT);

    renderBeats(popularContainer, popular);
    renderBeats(latestContainer, latest);
  }

  fetch("js/mock-beats.json")
    .then((response) => {
      if (!response.ok) {
        throw new Error("HTTP " + response.status);
      }
      return response.json();
    })
    .then(init)
    .catch((error) => {
      console.error("Error al cargar beats:", error);
      renderEmptyState(
        document.getElementById("popular-beats"),
        "No se pudieron cargar los beats."
      );
      renderEmptyState(
        document.getElementById("latest-beats"),
        "No se pudieron cargar los beats."
      );
    });
})();