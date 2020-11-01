#=============================================================чтение данных
num = 1 #номер магазина для анализа
shop_ways <- c("d:/healthy_food/Магазин 1/","d:/healthy_food/Магазин 2/","d:/healthy_food/Магазин 3/")
input1 =  read.table(file = paste0(shop_ways[num], "inall", ".txt"), header = TRUE)
output1 =  read.table(file = paste0(shop_ways[num], "outall", ".txt"), header = TRUE)
#input2 =  read.table(file = paste0(shop_ways[2], "inall", ".txt"), header = TRUE)
#output2 =  read.table(file = paste0(shop_ways[2], "outall", ".txt"), header = TRUE)
#input3 =  read.table(file = paste0(shop_ways[3], "inall", ".txt"), header = TRUE)
#output3 =  read.table(file = paste0(shop_ways[3], "outall", ".txt"), header = TRUE)

#=============================================================константы
BUY <- 150 # За сколько купили
SALE <- 300 # За сколько продаем
UTIL <- 10 # За сколько утилизируем
#=============================================================названия товаров

goods <- names(input1) #
goods <- goods[2:length(goods)]

#=============================================================подсчеты

for (i in goods){
  print(i)
  o = output1[, i] #магазин объем продаж
  s = (input1[,i] - output1[, i]) #списания
  name = paste0("Объем продаж и списаний в магазине ",num,". Товар: ",i,", шт")
  plot(x = o, type = "o", col = "red", xlab = "Дни", ylab = name, pch = CIRCLE <- 16)
  lines(x = s,type="o", col="blue")
  legend("topright", legend=c("Списание","Объем продаж"),col=c("blue","red"), pch=c(1,16))
  
  v = output1[, i]*SALE #выручка
  p = (output1[, i]*SALE) - (input1[, i]*BUY) - ((input1[, i] - output1[,i])*UTIL) #прибыль
  name = paste0("Выручка и прибыль в магазине ",num,". Товар: ",i,", руб")
  plot(x = p, ylim=c(min(min(p),min(v)),max(max(p),max(v))), type = "o", col = "purple", xlab = "Дни", ylab = name, pch = CIRCLE <- 16)
  lines(x = v,type="o", col="green",pch=1)
  legend("topright", legend=c("Выручка","Прибыль"),col=c("green","purple"), pch=c(1,16))
  r = 100 * (p/v)
  name= paste0("Рентабельность в магазине ",num,". Товар: ",i,", %")
  plot(x = r, type = "o", col = "red", xlab = "Дни", ylab = name, pch = CIRCLE <- 16)
  
}

