# Frontend Dockerfile (Vue.js)
FROM node:20

WORKDIR /app

# Устанавливаем зависимости
COPY package*.json ./
RUN npm install

# Копируем код
COPY . .

# Запуск дев-сервера Vue (vite или vue-cli)
CMD ["npm", "run", "dev"]
