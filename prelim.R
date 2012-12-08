library(reshape)
library(ggplot2)
f <- read.csv("formats_normalized.csv", colClasses="numeric")

fs <- melt(f)
ft <- fs[fs$value==1,]
table(ft$variable)

ggplot(ft, aes(x=variable)) + geom_bar() + coord_flip()

# the book category is swamping things; let's try it without.
no_book =  ft[ft$variable != "Book",]
ggplot(no_book, aes(x=variable)) + geom_bar() + coord_flip()
