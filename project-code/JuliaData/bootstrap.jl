  cd(@__DIR__)
  using Pkg
  pkg"activate ."

  function main()
    include("JuliaData.jl")
  end

  main()
