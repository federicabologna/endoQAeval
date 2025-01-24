library(tidyverse)
library(krippendorffsalpha)
library(irr)

info_ratings <- read_csv("./info_r.csv")
info_ratings <- select(info_ratings, -...1)
info_matrix <- as.matrix(info_ratings)

empathy_ratings <- read_csv("./empathy_r.csv")
empathy_ratings <- select(empathy_ratings, -...1)
empathy_matrix <- as.matrix(empathy_ratings)

actionability_ratings <- read_csv("./actionability_r.csv")
actionability_ratings <- select(actionability_ratings, -...1)
actionability_matrix <- as.matrix(actionability_ratings)

## Hughes' Krippendorff's Alpha
set.seed(42)
fit.full = krippendorffs.alpha(info_matrix, level = "interval",
                               control = list(parallel = FALSE),
                               verbose = TRUE)
summary(fit.full)

set.seed(42)
fit.full = krippendorffs.alpha(empathy_matrix, level = "interval",
                               control = list(parallel = FALSE),
                               verbose = TRUE)
summary(fit.full)

set.seed(42)
fit.full = krippendorffs.alpha(actionability_matrix, level = "interval",
                               control = list(parallel = FALSE),
                               verbose = TRUE)
summary(fit.full)



## Standard Krippendorffs' Alpha
kripp.alpha(info_matrix, method = "interval")