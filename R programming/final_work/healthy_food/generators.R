#===================================генерация in
generate_in <- function(nDays=7,min=50,max=120){
  return(as.integer(runif(n=nDays,min=min,max=max)))
}
#===================================генерация out относительно in
generate_out <- function(data.in,min){
  data.out=0
  for(i in 1:length(data.in)){
    data.out[i] <- as.integer(runif(n=1,min=min,data.in[i]))
    if (is.na(data.out[i])){
      data.out[i] =0
    }
  }
  return(data.out)
}
#===================================генерация по saleLevel
generate_out_level <- function(data.in,saleLevel = 50){
  data.out = 0
  
  sum.in = sum(data.in)
  n = 0
  repeat{
    n=n+1
    for(i in 1:length(data.in)){
      data.out[i] = as.integer(runif(n=1,min=0,data.in[i]))
    }
    sum.out = sum(data.out)
    if (sum.out==as.integer(sum.in*saleLevel/100)){
      break
    }
  }
  return(data.out)
}
#===================================вспомогательная функция рандома
rand_num <- function(a, b){
  rand = runif(1)
  return(round(rand * (b-a)+a))
}
#===================================генерация обычных файлов
generate.supply.sale <- function(name="D:/healthy_food/Генерация/Магазин 1/",type="in.txt",min=rand_num(2,10),max=rand_num(50,100),flag=T){
  dataout =""
  datain = generate_in(7,min,max)
  if (type == "out.txt"){
    datain = read.table(paste0(standart_way,as.character(num),"/","in.txt"))
    print(datain[,"Поставка"])
    dataout = generate_out(datain[,"Поставка"],min)
    print(dataout)
  }
  title = ifelse(type=="in.txt","Поставка","Продажа")
  dio <- data.frame("День" = 1:7)
  if (type =="in.txt"){
    
    dio[, title] <- as.integer(datain)
  }
  else{
    dio[, title] <- as.integer(dataout)
  }
  days <- c()
  for (i in dio$День) {
    
    day <- i %% 7
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
                       "воскресенье")
    days <- c(days, day_out)
  }
  
  dio$День = days
  write.table(x = dio, file = paste0(name,type),
              row.names = flag, col.names = flag)
}
#===================================генерация файлов с большими товарами
generate.supply.sale.many <- function(name="D:/healthy_food/Генерация/Магазин 1/", type="inall.txt", min=5, max=100, flag=T, 
                                      days_num=7, goods_num=1, goods="Молоко"){
  days <- c()
  result <- data.frame("День" = 1:days_num)
  names <- c("День")
  names(result) <- names
  for (i in result$День) {
    
    day <- i %% 7
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
                       "воскресенье")
    days <- c(days, day_out)
  }
  
  result$День = days
  result
  # Определим название заголовка столбцов
  title = ifelse(type=="inall.txt","Поставка","Продажа")
  for (good in goods) {
    if(type=="inall.txt"){
      datain = generate_in(days_num,min,max)
      result$Item = datain
      
    }
    else{
      datain = read.table(paste0(standart_way,as.character(num),"/","inall.txt"))
      dataout = generate_out(datain[,good],min)
      result$Item = dataout
      
    }
    names[length(names)+1] = good
    names(result) <- names
    
  }
  print(result)
  write.table(x = result, file =  paste0(name,type),
              row.names = flag, col.names = flag)
  
}
get_sale_value <- function(value,saleLevel){
  return (value*saleLevel/100)
}
#===================================генерация  файлов с заданным уровнем saleLevel
sale.level <- function(way="D:/healthy_food/Генерация/Магазин 1/", name="in.txt",saleLevel=50, filename="outlevel.txt",flag=T){
  if (saleLevel>100){
    saleLevel =100
  }
  if (saleLevel<0){
    saleLevel = 0
  }
  #рассматриваются два случая: обычные файлы и большие
  if(name=="in.txt"){
    title = ("Продажа")
    datain = read.table(paste0(standart_way,as.character(num),"/",name))[,"Поставка"]
    dataout = generate_out_level(datain,saleLevel)
    days <- c()
    dio <- data.frame("День" = 1:7)
    for (i in dio$День) {
      
      day <- i %% 7
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
                         "воскресенье")
      days <- c(days, day_out)
    }
    
    dio$День = days
    dio[, title] <- dataout
    write.table(x = dio, file =  paste0(way,filename),
                row.names = flag, col.names = flag)
    
  }
  if(name=="inall.txt"){
    filename = "outlevelall.txt"
    datain = read.table(paste0(standart_way,as.character(num),"/",name))
    ndays = nrow(datain)
    days <- c()
    result <- data.frame("День" = 1:ndays)
    names <- c("День")
    names(result) <- names
    for (i in result$День) {
      
      day <- i %% 7
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
                         "воскресенье")
      days <- c(days, day_out)
    }
    
    result$День = days
    for(i in 2:ncol(datain)){
      data= datain[i][,]
      dataout = generate_out_level(data,saleLevel)
      print(dataout)
      nameout = colnames(datain)[i]
      result$Item = dataout
      names[length(names)+1] = nameout
      names(result) <- names
    }
    write.table(x = result, file =  paste0(way,filename),
                row.names = flag, col.names = flag)
  }
  
  
}
#===================================главный код с вызовом функций
standart_way = "D:/healthy_food/Магазин "
goods = c("Молоко", "Хлеб")
for (num in 1:10){
  #print(num)
  way = paste0(standart_way,as.character(num),"/")
  #generate.supply.sale(name=way,type="in.txt")
  #generate.supply.sale(name=way,type="out.txt")
  generate.supply.sale.many(way,  
   min <- rand_num(2, 10), max <- rand_num(50, 100),type="inall.txt"
   ,days_num = 30, goods_num = 2, goods = goods)
  generate.supply.sale.many(way,  
   min <- rand_num(2, 10), max <- rand_num(50, 100),type="outall.txt"
  ,days_num = 30, goods_num = 2, goods = goods)
  #sale.level(way)
  #sale.level(way,name="in.txt",saleLevel = 50)
  #sale.level(way,name="inall.txt",saleLevel = 60)
}
