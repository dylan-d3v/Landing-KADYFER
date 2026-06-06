"use strict";

const siteConfig = Object.freeze({
  whatsappNumber: "593983956295",
  address: "",
  mapsUrl: "",
  schedule: "",
  instagramUrl: "",
  facebookUrl: "",
});

const whatsappMessages = Object.freeze({
  general: "Hola, quiero agendar una valoración en KADYFER.",
  sueroterapia: "Hola, quiero información sobre Sueroterapia Ortomolecular en KADYFER.",
  "terapia-neural": "Hola, quiero agendar una valoración para Terapia Neural en KADYFER.",
  "faciales-corporales":
    "Hola, quiero información sobre tratamientos faciales y corporales en KADYFER.",
});

const availableAssetPaths = new Set([
  "assets/brand/favicon.png",
]);

const buildWhatsAppUrl = (messageKey) => {
  const message = whatsappMessages[messageKey] ?? whatsappMessages.general;
  return `https://wa.me/${siteConfig.whatsappNumber}?text=${encodeURIComponent(message)}`;
};

const configureWhatsAppLinks = () => {
  document.querySelectorAll("[data-whatsapp]").forEach((link) => {
    link.href = buildWhatsAppUrl(link.dataset.whatsapp);
  });
};

const configureNavigation = () => {
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const navigation = document.querySelector("[data-nav]");
  const header = document.querySelector("[data-header]");

  if (!menuToggle || !navigation || !header) return;

  const closeMenu = () => {
    menuToggle.setAttribute("aria-expanded", "false");
    navigation.classList.remove("is-open");
  };

  menuToggle.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isOpen));
    navigation.classList.toggle("is-open", !isOpen);
  });

  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
      menuToggle.focus();
    }
  });

  const updateHeader = () => {
    header.classList.toggle("is-fixed", window.scrollY > 40);
  };

  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });
};

const configureOptionalImages = () => {
  const optionalImages = document.querySelectorAll("[data-optional-image]");
  const gallery = document.querySelector("[data-gallery]");
  const galleryEmpty = document.querySelector("[data-gallery-empty]");
  let loadedGalleryImages = 0;

  optionalImages.forEach((image) => {
    const frame = image.closest("[data-image-frame]");
    const isGalleryImage = Boolean(image.closest("[data-gallery]"));
    const imagePath = image.dataset.src;

    const revealImage = () => {
      if (frame) frame.hidden = false;
      if (image.classList.contains("brand-logo")) {
        const fallback = document.querySelector("[data-brand-fallback]");
        image.hidden = false;
        if (fallback) fallback.hidden = true;
      }
      if (isGalleryImage) {
        loadedGalleryImages += 1;
        if (galleryEmpty) galleryEmpty.hidden = true;
        if (gallery) gallery.dataset.loadedImages = String(loadedGalleryImages);
      }
    };

    const hideImage = () => {
      if (frame) frame.hidden = true;
      image.remove();
    };

    if (!imagePath) {
      hideImage();
      return;
    }

    image.addEventListener("load", revealImage, { once: true });
    image.addEventListener("error", hideImage, { once: true });

    if (!availableAssetPaths.has(imagePath)) {
      hideImage();
      return;
    }

    if (frame) frame.hidden = false;
    image.closest("picture")?.querySelectorAll("source[data-srcset]").forEach((source) => {
      source.srcset = source.dataset.srcset;
    });
    image.src = imagePath;
  });
};

const configureFavicon = () => {
  const faviconPath = "assets/brand/favicon.png";

  if (!availableAssetPaths.has(faviconPath)) return;

  const favicon = document.querySelector('link[rel="icon"]');
  if (!favicon) return;
  favicon.type = "image/png";
  favicon.href = faviconPath;
};

const configureOptionalContact = () => {
  const container = document.querySelector("[data-optional-contact]");
  if (!container) return;

  const contactItems = [];

  if (siteConfig.address) {
    const address = document.createElement(siteConfig.mapsUrl ? "a" : "span");
    address.textContent = siteConfig.address;

    if (siteConfig.mapsUrl) {
      address.href = siteConfig.mapsUrl;
      address.target = "_blank";
      address.rel = "noopener noreferrer";
    }

    contactItems.push(address);
  }

  if (siteConfig.schedule) {
    const schedule = document.createElement("span");
    schedule.textContent = siteConfig.schedule;
    contactItems.push(schedule);
  }

  if (contactItems.length) {
    const contactList = document.createElement("div");
    contactList.className = "optional-contact-list";
    contactItems.forEach((item) => contactList.append(item));
    container.append(contactList);
  }

  const socialLinks = [
    ["Instagram", siteConfig.instagramUrl],
    ["Facebook", siteConfig.facebookUrl],
  ].filter(([, url]) => Boolean(url));

  if (socialLinks.length) {
    const socialList = document.createElement("div");
    socialList.className = "social-list";

    socialLinks.forEach(([label, url]) => {
      const link = document.createElement("a");
      link.href = url;
      link.textContent = label;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      socialList.append(link);
    });

    container.append(socialList);
  }
};

const configureYear = () => {
  const year = document.querySelector("[data-current-year]");
  if (year) year.textContent = String(new Date().getFullYear());
};

configureWhatsAppLinks();
configureNavigation();
configureOptionalImages();
configureFavicon();
configureOptionalContact();
configureYear();
