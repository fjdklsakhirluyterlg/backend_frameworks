express = require("express")
app = express()

app.get("/", (req, res) => {
    res.send("hello there")
})

app.run()