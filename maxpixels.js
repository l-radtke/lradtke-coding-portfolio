""" defines the maxpixels function that will find the smallest polygon's area"""

maxpixels <- function(polygon){
  a <- 0
  list <- list()
  for(nb in 1:length(polygon@polygons)){
    a <- a + 1
    list <- c(polygon@polygons[[a]]@area)
  }
  min(list)
}