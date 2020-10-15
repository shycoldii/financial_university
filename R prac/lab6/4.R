dat4 <- function(day,lang="ru", form = "full"){
  if(is.double(day)){
    day <- round(day)
  } else if (day<1){
    return(print(" "))
  }
  
  day <- day %% 7
  if (day == 0){
    day = 7
  } 
  if (form == "short"){
    day = day+7 #добавляем 7 , если форма короткая
  }
  if ((tolower(lang)=="eng") | (tolower(lang)=="english")|(tolower(lang)=="англ")) {
    day_out_en <- switch(day,
                         "monday",
                         "tuesday",
                         "wednsday",
                         "thursday",
                         "friday",
                         "saturday",
                         "sunday",
                         "mon",
                         "tues",
                         "wed",
                         "thurs",
                         "fri",
                         "sat",
                         "sun"
    )
    return(print(day_out_en))
  } else {
    day_out_rus <- switch(day,
                          "понедельник",
                          "вторник",
                          "среда",
                          "четверг",
                          "пятница",
                          "суббота",
                          "воскресенье",
                          "пн",
                          "вт",
                          "ср",
                          "чт",
                          "пт",
                          "сб",
                          "вск"
    )
    return(print(day_out_rus))
  }
}

dat4(15, "eng", "short")
dat4(11, "ru", "short")
dat4(21, 'ru', "full")
dat4(21, 'анГЛ', "full")
