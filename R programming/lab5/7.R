{
  N <- readline(prompt = "Введите число: ")
  N = as.numeric(N)
  
  N2 <- N
  year <- 20
  c <- 4 #параметр, отвечающий за високосность 
  #день недели не зависит от високосности
  temp <- N%%7
  if (temp == 0){
    temp <- 7
  }
  
  #выбираем день по индексу
  day_out <- switch (temp,
                     "понедельник",
                     "вторник",
                     "среда",
                     "четверг",
                     "пятница",
                     "суббота",
                     "воскресенье"
  )
  
  while ((N2 >366)&(c == 4)|((N2>365)&(c<4))){
    if (c == 4){
      N2 <- N2 -366
      year <- year +1
      c <- 1
    }else{
      N2<-N2-365
      year <- year + 1
      c <- c + 1
    }
  }
  days = N2 #дней в текущем для расчета году
  # для расчета високосности года
  if (year%%4 > 0){
    check_vis <- 0
  } else {
    check_vis <- 1
  }
  
  tot_count <- 0
  
  # Для месяца
  if (days < 32){
    month_out <- "января"
  }
  if(check_vis == 1){ #если невисокосный
    if ((31 < days)&&(days< 61)){
      month_out <- "февраля"
    }
    if ((60 < days)&&(days < 92)){
      month_out <- "марта"
    }
    if ((91 < days)&&(days < 122)){
      month_out <- "апреля"
    }
    if ((121 < days)&&(days < 153)){
      month_out <- "мая"
    }
    if ((152 < days)&&(days < 183)){
      month_out <- "июня"
    }
    if ((182 < days)&&(days < 214)){
      month_out <- "июля"
    }
    if ((213 < days)&&(days < 245)){
      month_out <- "августа"
    }
    if ((244 < days)&&(days < 275)){
      month_out <- "сентября"
    }
    if ((274 < days)&&(days < 306)){
      month_out <- "октября"
    }
    if ((305 < days)&&(days <= 335)){
      month_out <- "ноября"
    }
    if ((335 < days)&&(days <= 366)){
      month_out <- "декабря"
    }
  }else{
    if ((31 < days)&&(days < 60)){
      month_out <- "февраля"
    }
    if ((59 < days)&&(days < 91)){
      month_out <- "марта"
    }
    if ((90 < days)&&(days < 121)){
      month_out <- "апреля"
    }
    if ((120 < days)&&(days < 152)){
      month_out <- "мая"
    }
    if ((151 < days)&&(days < 182)){
      month_out <- "июня"
    }
    if ((181 < days)&&(days < 213)){
      month_out <- "июля"
    }
    if ((212 < days)&&(days< 244)){
      month_out <- "августа"
    }
    if ((243 < days)&&(days < 274)){
      month_out <- "сентября"
    }
    if ((273 <days)&&(days < 305)){
      month_out <- "октября"
    }
    if ((304 < days)&&(days <= 334)){
      month_out <- "ноября"
    }
    if ((334 < days)&&(days <= 365)){
      month_out <- "декабря"
    }
  }
  
  #задаем соответствие для будущего определения дня
  cur_mont <- switch(month_out, 
                     'января'=1,
                     'февраля'=2,
                     'марта'=3,
                     'апреля'=4,
                     'мая'=5,
                     'июня'=6,
                     'июля'=7,
                     'августа'=8,
                     'сентября'=9,
                     'октября'=10,
                     'ноября'=11,
                     'декабря'=12)
  if (check_vis ==1){
    number_prev <-switch(cur_mont,
                         0,31,60,91,121,152,182,213,244,274,305,335)
  }else{
    number_prev <-switch(cur_mont,
                         0,31,59,90,120,151,181,212,243,275,304,334)
  }
  
  cur_day <- days - number_prev #чистое число месяца
  
 
  
  out <- paste0("Введенное значение ", N, "- это ", day_out,",", cur_day," ", month_out, ",", as.character(year), "-й год",".Четкая дата: ",cur_day,".",cur_mont,".",year)
  
  print(out)
  
}