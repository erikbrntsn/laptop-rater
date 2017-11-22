import json
from pprint import pprint

with open("scores", "r") as fh:
  scores = json.load(fh)


def ratingFunc(d):
  return d["cpuScore"]**2 * d["gpuScore"] / d["price"]**2
  # return d["cpuScore"] * d["gpuScore"]
  # return d["cpuScore"]**2 / (d["price"] * d["weight"]**2)


for score in scores:
  score["rating"] = ratingFunc(score)


for laptop in sorted(scores, key=lambda x: x["rating"]):
  print("Score:\t{:4.2f}\t{:}\t{:} kg\t{:}\n\t".format(float(laptop["rating"]), laptop["price"], laptop["weight"], laptop["name"]) +
        "Original:\t\t{:<30}\tOriginal:\t\t{:<30}\n\t".format(laptop["originalCpuName"], laptop["originalGpuName"]) +
        "Matched:\t\t{:<30}\tMatched:\t\t{:<30}\n\t".format(laptop["matchedCpuName"], laptop["matchedGpuName"]) +
        "MatchType:\t{:<30}\tMatchType:\t{:<30}\n\t".format(laptop["matchTypeCpu"], laptop["matchTypeGpu"]) +
        "Score:\t\t\t{:<30}\tScore:\t\t\t{:<30}\n\n".format(laptop["cpuScore"], laptop["gpuScore"]))
