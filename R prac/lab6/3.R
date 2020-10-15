dat3 <- function(day,lang="ru"){
  if(is.double(day)){
    day <- round(day)
  } else if (day<1){
    return(print("Null"))
  }
  
  day <- day %% 7 #определение дня
  if (day == 0){
    day = 7
  }
  days = c("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
  v= c("анг","eng","english","англ")
  if (lang %in% v) {
    day_out_en <- days[day]
    return(print(day_out_en))
  } else {#словарь русских
    day_out_rus <- switch(day, 
                          "понедельник",
                          "вторник",
                          "среда",
                          "четверг",
                          "пятница",
                          "суббота",
                          "воскресенье"
    )
    return(print(day_out_rus))
  }
}

dat3(6, "eng")
dat3(12)
