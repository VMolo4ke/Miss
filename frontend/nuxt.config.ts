// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ["@nuxtjs/google-fonts", "@pinia/nuxt", "@vite-pwa/nuxt"],
  pwa: {
    manifest: {
      name: "Miss",
      short_name: "Miss",
      description: "Тут вам не соскучится",
      theme_color: "#2c2420",
      background_color: "#2c2420",
      display: "standalone",
      icons: [
        {
          src: "icons/icon-192x192.png",
          sizes: "192x192",
          type: "images/png",
        },
        {
          src: "icons/icon-512x512.png",
          sizes: "512x512",
          type: "images/png",
        },
      ],
    },
    workbox: {
      navigateFallback: "/",
    },
    devOptions: {
      enabled: true,
      type: "module",
    },
  },
  googleFonts: {
    families: {
      Manrope: [400, 500, 700],
    },
    display: "swap",
    download: true,
  },
  css: [
    "~/assets/scss/main.scss", // Подключаем главный файл стилей
  ],

  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "~/assets/scss/_vars.scss" as *;',
        },
      },
    },
  },
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
});
