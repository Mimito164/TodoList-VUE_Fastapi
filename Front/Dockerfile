FROM node:22.12

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build
EXPOSE 8080