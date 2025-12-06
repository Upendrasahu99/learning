const express = require('express')

const app = express()

app.get('/', (req, res, next) => {
  res.send('Hello World 3 time')
})

app.listen(3000)