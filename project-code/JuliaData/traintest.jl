using DelimitedFiles
using MLDataUtils

function traintest()
  a = readdlm("data/travel.txt", ',')
  a = shuffleobs(a, obsdim=1)
  train, test = splitobs(a, at = 0.7, obsdim=1)
  train, test
  open("data/train.txt", "w") do f
    writedlm(f, train, ",")
  end
  open("data/test.txt", "w") do f
    writedlm(f, test, ",")
  end
end
traintest()
