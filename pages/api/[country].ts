const Countries = require("./../../src/Datas/Countries.json")

const WorldWide = (req, res) => {
  const { country } = req.query
  //res.status(200).json({ damn: country })
  res.status(200).json({ damn: Countries.name })
}
export default WorldWide
