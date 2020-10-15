dat5 <- function(month,lang="ru", form = "full"){
  if(is.double(month)){
    month <- round(month)
  } else if (month<1){
    return(print(" "))
  }
  if (month>12){
    month = month%%12
  }
  if (month==0){
    month=12
  }
  
  if (form == "short"){
    month = month+12
  }
  if ((tolower(lang)=="eng") | (tolower(lang)=="english")|(tolower(lang)=="англ")) {
    day_out_en <- switch(month,
                         "january",
                         "february",
                         "march",
                         "april",
                         "may",
                         "june",
                         "july",
                         "august",
                         "september",
                         "october",
                         "november",
                         "december",
                         "jan",
                         "feb",
                         "mar",
                         "apr",
                         "may",
                         "june",
                         "july",
                         "aug",
                         "sept",
                         "oct",
                         "nov",
                         "dec"
    )
    return(print(day_out_en))
  } else {
    day_out_rus <- switch(month,
                          "январь",
                          "февраль",
                          "март",
                          "апрель",
                          "май",
                          "июнь",
                          "июль",
                          "август",
                          "сентябрь",
                          "октябрь",
                          "ноябрь",
                          "декабрь",
                          "янв",
                          "фев",
                          "март",
                          "апр",
                          "май",
                          "июнь",
                          "июль",
                          "авг",
                          "сент",
                          "окт",
                          "нояб",
                          "дек"
    )
    return(print(day_out_rus))
  }
}

dat5(13, "eng", "short")
dat5(11, "ru", "short")
dat5(2, 'ru', "full")
dat5(2, 'анГЛ', "full")
