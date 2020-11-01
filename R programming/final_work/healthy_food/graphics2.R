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
#=============================================================вектора нужных графиков
colors = c("red","purple","blue","yellow","gold1", "lightcoral","mediumvioletred","navyblue", "tan1","turquoise1","chocolate1","blue","black","brown", "darkseagreen")
pcc = c(1,2,3,4,5,6,7,8,9,10)

#=============================================================подсчеты 1 пункта
for(j in 1:5){
  line = c()
  c=1
  num=0
  for (i in goods){
    funct = switch(j,
                   output1[, i],
                   (input1[,i] - output1[, i]),
                   (output1[, i]*SALE) - (input1[, i]*BUY) - ((input1[, i] - output1[,i])*UTIL),
                   output1[, i]*SALE,
                   100*(((output1[, i]*SALE) - (input1[, i]*BUY) - ((input1[, i] - output1[,i])*UTIL))/(output1[, i]*SALE)))
    line=append(line,funct)
    num = length(funct)
    c=c+1
    
  }
  c=c-1

  names = switch(j,"Объем продаж","Списания","Прибыль","Выручка","Рентабильность")
  plot(x = line[1:num], type = "o", col = "red", xlab = "Дни", ylab = names, pch = CIRCLE <- 1)
  for (i in range(2:c)){
    lines(x = line[((i-1)*num):(i*num)],type="o", col=colors[i],pch=pcc[i])
    legend("topleft", legend=c("Молоко","Хлеб"),col=colors, pch=pcc)
  }
  
}
#=============================================================подсчеты 2 пункта
v=c()
for (i in 1:10){
  assign(paste0("input", as.character(i)), read.table(paste0("d:/healthy_food/Магазин ",as.character(i),"/inall.txt"), head=TRUE))
  assign(paste0("output", as.character(i)), read.table(paste0("d:/healthy_food/Магазин ",as.character(i),"/outall.txt"), head=TRUE))
  v=append(v,eval(parse(text = paste0("output", as.character(i))))[,goods[1]])
  if(i==1){
    plot(x = v, type = "o", col = "red", xlab = "Дни",ylim =c(0,80), ylab = paste0("Объем продаж, шт. Товар: ",goods[1]), pch = pcc[i])
  }
  if(i==10){
    for(j in  2:10){
      lines(x = v[((j-1)*length(v)/10):(j*length(v)/10)], type = "o", col = colors[j], xlab = "Дни", ylab = paste0("Объем продаж, шт. Товар: ",goods[i]))
      legend("topright", legend=c("Магазин 1","Магазин 2","Магазин 3","Магазин 4","Магазин 5","Магазин 6","Магазин 7","Магазин 8","Магазин 9","Магазин 10"),col=colors,pch=pcc[i])
    }
  }
}
#=============================================================подсчеты 3 пункта
v=c()
for (i in 1:10){
  assign(paste0("input", as.character(i)), read.table(paste0("d:/healthy_food/Магазин ",as.character(i),"/inall.txt"), head=TRUE))
  assign(paste0("output", as.character(i)), read.table(paste0("d:/healthy_food/Магазин ",as.character(i),"/outall.txt"), head=TRUE))
  v=append(v,eval(parse(text = paste0("output", as.character(i))))[,goods[1]])
  v=append(v,eval(parse(text = paste0("output", as.character(i))))[,goods[2]])
  if(i==1){
    plot(x = v[1:(length(v)/2)], type = "o", col = colors[i], xlab = "Дни",ylim =c(0,80), ylab = paste0("Объем продаж, шт. Товары: ",goods), pch = 1)
    lines(x = v[(length(v)/2):length(v)], type = "o", col = colors[i],  pch =2)
  }
  if(i==10){
    for(j in  2:10){
      lines(x = v[(length(v)*(j-1)/10):(length(v)*(j-1)/20)], type = "o", col = colors[j],  pch =1)
      lines(x = v[(length(v)*(j-1)/20):(length(v)*j/20)], type = "o", col = colors[j],  pch =2)
      legend("topright", legend=c(goods[1],goods[2]), pch=pcc)
      legend("topleft", legend=c("Магазин 1","Магазин 2","Магазин 3","Магазин 4","Магазин 5","Магазин 6","Магазин 7","Магазин 8","Магазин 9","Магазин 10"),col=colors,pch=1)
    }
  }
}


