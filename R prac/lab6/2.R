dat2 <- function(day){
  if (day<1){
    return(" ")
  }
  if(is.double(day)){
    day <- round(day)
  } 
  
  day <- day %% 7
  if (day == 0){
    day = 7
  }
  day_out <- switch(day,
                   "понедельник",
                   "вторник",
                   "среда",
                   "четверг",
                   "пятница",
                   "суббота",
                   "воскресенье"
  )
  return(print(day_out))
}
dat2(14)