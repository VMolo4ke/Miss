# Этап 1: Сборка приложения
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Этап 2: Запуск
FROM node:22-alpine
WORKDIR /app
# Копируем только результат сборки и настройки
COPY --from=builder /app/.output ./.output
COPY --from=builder /app/package.json ./package.json

ENV NODE_ENV=production
ENV HOST=0.0.0.0
ENV PORT=3000

# Nuxt в режиме standalone запускается через этот файл
CMD ["node", ".output/server/index.mjs"]
