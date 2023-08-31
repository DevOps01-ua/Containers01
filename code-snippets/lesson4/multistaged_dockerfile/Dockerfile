# ---- Base Node ----
FROM node:14 AS base
WORKDIR /app
COPY package*.json ./

# ---- Dependencies ----
FROM base AS dependencies
# Install app dependencies including 'devDependencies'
RUN npm install

# ---- Build ----
FROM dependencies AS build
COPY . .
# Here you might typically run transpilers or other build steps.

# ---- Release ----
FROM base AS release
# Copy 'node_modules' from 'dependencies' stage and binaries from 'build' stage
COPY --from=dependencies /app/node_modules ./node_modules
COPY --from=build /app/ ./
EXPOSE 3000
CMD ["npm", "start"]
