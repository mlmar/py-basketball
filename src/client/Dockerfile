# 1) Build stage
FROM node:18 AS build

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

# 2) Serve stage
FROM nginx:alpine AS production

# Copy build output to nginx html folder
COPY --from=build /app/dist /usr/share/nginx/html

# Copy your custom nginx config (optional)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
