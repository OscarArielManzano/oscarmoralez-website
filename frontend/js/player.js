(function () {
  "use strict";

  const VIDEO_ID_PATTERN = /^[A-Za-z0-9_-]{11}$/;
  const playerContainer = document.getElementById("player");

  function extractVideoId(href) {
    let url;
    try {
      url = new URL(href);
    } catch (error) {
      return null;
    }

    let id = null;
    if (url.hostname === "youtu.be") {
      id = url.pathname.slice(1);
    } else if (url.hostname.endsWith("youtube.com")) {
      id = url.searchParams.get("v");
    }

    return id && VIDEO_ID_PATTERN.test(id) ? id : null;
  }

  function renderPlayer(videoId) {
    const iframe = document.createElement("iframe");
    iframe.src = "https://www.youtube.com/embed/" + videoId + "?autoplay=1";
    iframe.title = "Reproductor de YouTube";
    iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
    iframe.allowFullscreen = true;
    playerContainer.replaceChildren(iframe);
  }

  // Delegación de eventos: un solo listener para ambas listas de beats.
  document.getElementById("beats").addEventListener("click", function (event) {
    // Los clics en el enlace "Ver en YouTube" los gestiona el navegador.
    if (event.target.closest("a")) {
      return;
    }

    const card = event.target.closest(".beat-card");
    if (!card) {
      return;
    }

    const link = card.querySelector(".beat-card-link");
    const videoId = link ? extractVideoId(link.href) : null;

    if (!videoId) {
      console.error("No se pudo obtener el ID del video.");
      return;
    }

    renderPlayer(videoId);
    playerContainer.scrollIntoView({ behavior: "smooth", block: "center" });
  });
})();