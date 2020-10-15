
{
 N = readline(prompt = "Введите N")
 N = as.numeric(N)
 
 now_year = 2020

 if (N<1){
   print("Недопустимое число!") #если пользователь ввел число меньше 1
 }
 else{
   day = N %% 7 #день недели
   if (day == 0){
     day = 7
   }
   day_out <- switch (day,
                      "понедельник",
                      "вторник",
                      "среда",
                      "четверг",
                      "пятница",
                      "суббота",
                      "воскресенье"
   )
   day_of = N%%30
   day_of = ifelse(month==0,30,day_of) #день числом
   
   month = 1 
   res = 0
   for (i in 1:N){
      res = res + 1 #определяем год и месяц
      if (res==31){
         month = month +1
         res = 1
      }
      if (month==13){
         month = 1
         now_year = now_year +1
      }
         
   }
   
   month_out <- switch (month, "январь", "февраль",
                        "март",
                        "апрель",
                        "май",
                        "июнь",
                        "июль",
                        "август",
                        "сентябрь",
                        "октябрь",
                        "ноябрь",
                        "декабрь"
   )
   out = paste0("Число ", N, "- это ",
               month_out, ", ", day_out, ", ", now_year, "-й год. Полная дата: ",day_of,".",month,".",now_year)
   print(out)
   
 }
}

