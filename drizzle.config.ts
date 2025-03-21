import {defineConfig} from 'drizzle-kit'

export default defineConfig({
  dialect: "sqlite",
  schema: "./drizzle/schema.ts",
  out: "./drizzle",
  dbCredentials: {
    url: "./src/movies.db",
  }
})