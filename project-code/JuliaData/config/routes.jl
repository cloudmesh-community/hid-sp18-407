using Genie.Router
using MyLib

route("/") do
  serve_static_file("/welcome.html")
end

route("/hello") do
  "Welcome to Genie!"
end

route("/getdata") do
  MyLib.GetData()
end

route("/traintest") do
  MyLib.TrainTest()
end

