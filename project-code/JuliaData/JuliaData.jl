module JuliaData

using Genie, Genie.Router, Genie.Renderer, Genie.AppServer

function main()
  Base.eval(Main, :(const UserApp = JuliaData))

  include("genie.jl")

  Base.eval(Main, :(const Genie = JuliaData.Genie))
  Base.eval(Main, :(using Genie))
end

main()

end
