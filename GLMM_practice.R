### TUTORIAL 1 ###

# define variables pitch and sex
pitch = c(233,204,242,130,112,142)
sex = c(rep("female",3),rep("male",3))

# combine them in a dataframe
my.df.1 = data.frame(sex,pitch)

# run the model to see the effect of sex on pitch based 
# on the data in my.df.1
xmdl.1 = lm(pitch ~ sex, my.df.1)

# view the reuslts 
summary(xmdl.1)

# define a new set of variables (age and pitch) and repeat the process
age = c(14,23,35,48,52,67)
pitch = c(252,244,240,233,212,204)
my.df.2 = data.frame(age,pitch)
xmdl.2 = lm(pitch ~ age, my.df)
summary(xmdl.2)

# add a new column to my.df.2 that subtracts the mean age from 
# every value in my.df.2$age
my.df.2$age.c = my.df.2$age - mean(my.df.2$age)
# plot(my.df.2$age, my.df.2$pitch)
xmdl.3 = lm(pitch ~ age.c, my.df.2)
summary(xmdl.3)

# visualize the residuals
plot(fitted(xmdl.3),residuals(xmdl.3), xlab = "Fitted values", ylab = "Residuals")
abline(a = 0, b = 0, h = 0, lty = 2)
# lty = 2 makes it dotted

# plot random data
plot(rnorm(100),rnorm(100))

# make a histogram and a Q-Q plot of the residuals
hist(residuals(xmdl.3))
qqnorm(residuals(xmdl.3))

# dfbeta to check influential data points:
# how much the slope needs to be modified if a 
# data point is removed
# anything more than 1/2 of the absolute value of 
# the slope is alarming -> run with and without to compare 


### TUTORIAL 2 ###

library(lme4)

# load in the data from bodowinter.com
politeness = read.csv("http://www.bodowinter.com/tutorial/politeness_data.csv")

# data exploration
head(politeness)
tail(politeness)
summary(politeness)
str(politeness)
colnames(politeness)
rownames(politeness)

# data cleaning
# same result:
which(is.na(politeness$frequency))
which(!complete.cases(politeness))

# relationship between politeness and pitch
boxplot(frequency ~ attitude*gender, col = c("white","lightgray"), politeness)

# contrsucting the model with fixed and random effects
politeness.model = lmer(frequency ~ attitude + (1|subject) + (1|scenario), data = politeness)

# view results
summary(politeness.model)

# overwrite the model adding gender as a fixed result
politeness.model = lmer(frequency ~ attitude + gender + (1|subject) + (1|scenario), data = politeness)

# view results
summary(politeness.model)
# the std.dev for subject is much lower now

# show the effect of attitude
# null model (without the factor you're interested in measuring the effect of)
politeness.null = lmer(frequency ~ gender + (1|subject) + (1|scenario), data = politeness, REML = FALSE)
# re-do full model adding REML = FALSE
politeness.model = lmer(frequency ~ gender + attitude + (1|subject) + (1|scenario), data = politeness, REML = FALSE)
# view results 
anova(politeness.null,politeness.model)
# p-value = 0.00065

# find out if there is an interaction 
politeness.reduced = lmer(frequency ~ gender + attitude + (1|subject) + (1|scenario), data = politeness, REML = FALSE)
politeness.full = lmer(frequency ~ gender * attitude + (1|subject) + (1|scenario), data = politeness, REML = FALSE)
anova(politeness.reduced,politeness.full)

# view the coefficients of the model
coef(politeness.model)

# random slope model
politeness.model.rand = lmer(frequency ~ attitude + gender + (1+attitude|subject) + (1+attitude|scenario), data=politeness, REML=FALSE)
coef(politeness.model.rand)

politeness.null = lmer(frequency ~ gender + (1+attitude|subject) + (1+attitude|scenario), data=politeness, REML=FALSE)

anova(politeness.null,politeness.model.rand)

# to check for influential points (dfbeta() doesn't work here)
#all.res=numeric(nrow(mydataframe))
#for(i in 1:nrow(mydataframe)){
#  myfullmodel=lmer(response~predictor+
#                     (1+predictor|randomeffect),POP[-i,])
#  all.res[i]=fixef(myfullmodel)[some number]
#}