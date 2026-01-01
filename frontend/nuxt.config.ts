// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ["@nuxtjs/google-fonts", "@pinia/nuxt"],
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