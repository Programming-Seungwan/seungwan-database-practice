import {Database} from "bun:sqlite"
import {drizzle} from "drizzle-orm/bun-sqlite"
import { movies } from "./drizzle/schema"

const sqliteConnection = new Database("./src/movies.db")
const db = drizzle(sqliteConnection)

const results = await db.select({id: movies.movieId, title: movies.title, overview: movies.overview}).from(movies).limit(50)

console.log(results)