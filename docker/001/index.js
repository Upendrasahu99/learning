const express = require('express')

const app = express()

app.get('/', (req, res, next) => {
  res.send('Hello World 3 time')
})

app.listen(3000)
console.log('Env variable')
console.log(process.env.DATABASE_URL)