(function () {
  "use strict";

  // Única constante con la URL del backend. Cambiar en T17 al desplegar.
  const API_BASE_URL = "http://localhost:5000";

  async function fetchJson(path) {
    const response = await fetch(API_BASE_URL + path);
    if (!response.ok) {
      throw new Error("HTTP " + response.status);
    }
    const data = await response.json();
    if (!Array.isArray(data)) {
      throw new Error("Respuesta inesperada del servidor.");
    }
    return data;
  }

  window.BeatsAPI = {
    getLatest: () => fetchJson("/api/beats"),
    getPopular: () => fetchJson("/api/beats/popular"),
  };
})();