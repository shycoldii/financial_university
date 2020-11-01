DEBUG_ON <- TRUE
DEBUG_OFF <- FALSE

pow1 <- function(x,y, z, isDebug = DEBUG_OFF) {
  if(isDebug){
    if(z!=0 && is.numeric(x) && is.numeric(y)){
      return(print(paste0('pow1: x=', x, ' y=', y, ' z=',z ,', ответ = ',(x^y)/z)))
    } else {
      return(print("Ошибка!"))
    }
  }
}

l <- pow1(2, 3, 2, DEBUG_ON)
