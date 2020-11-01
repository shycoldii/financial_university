#===================================константы
BUY1 = 150
BUY2 = 50
PRICE1 = 300
PRICE2 = 100
UTIL1 = 10
UTIL2 = 30
#===================================чтение файлов

read_txt <- function(way){
  return( read.table(file = way, header = T))
}
#===================================создание таблицы

standart_way = "d:/healthy_food/"
title <- c("Магазин 1","Магазин 2","Магазин 3","Магазин 4","Магазин 5","Магазин 6","Магазин 7",
                   "Магазин 8","Магазин 9","Магазин 10","Итог","Среднее")
rev <- rep(0, 12)
final.res.tab <- data.frame("Название" = title,"Выручка" = rev, "Прибыль" = rev, "Реализация" = rev, "Списания" = rev)

#===================================основной цикл

for(num in 1:10){
  in_ = read_txt(paste0(standart_way,title[num],"/","inall.txt"))
  out_ = read_txt(paste0(standart_way,title[num],"/","outall.txt"))
  titles = colnames(in_) #названия продуктов
  #здесь мы создаем все столбцы для заполнения
  if(num==1){ 
    for(i in 2:length(titles)){
      info = c("Выручка","Прибыль","Реализация","Списания")
      info[1] = paste0(info[1],"_",titles[i])
      info[2] = paste0(info[2],"_",titles[i])
      info[3] = paste0(info[3],"_",titles[i])
      info[4] = paste0(info[4],"_",titles[i])
      tab_names <- names(final.res.tab)
      tab_names <- tab_names[1: (length(final.res.tab)-4)]
      tab_names <- c(tab_names, info)
      names(final.res.tab) <- tab_names
      final.res.tab$New1 <- rev
      final.res.tab$New2 <- rev
      final.res.tab$New3 <- rev
      final.res.tab$New4 <- rev
    }
    final.res.tab <- final.res.tab[ , c(1:(length(final.res.tab)-4))]

  }
  
    #===================================здесь подсчет результатов
  for (i in c(2:length(in_))){
      info <- c("Выручка", "Прибыль", "Реализация", "Списания")
      pr <- sum(out_[, i] * PRICE1) # Выручка
      if(num==1){
        print(pr)
      }
      pc <- pr - (sum(in_[, i]) * BUY1) - ((sum(in_[, i]) - sum(out_[, i])) * UTIL1) # Прибыль
      real <- sum(out_[, i]) # реализованные товары
      spis <- (sum(in_[, i]) - sum(out_[, i])) # списания
      
      # Добавление приписки товара
      for(j in 1:4){
        info[j] = paste0(info[j], "_",  titles[i])
        
      }

      final.res.tab
      final.res.tab[, info[1]][num] <- pr
      final.res.tab[, info[2]][num] <- pc
      final.res.tab[, info[3]][num] <- real
      final.res.tab[, info[4]][num] <- spis
    
  }
  
}

#===================================итог по магазину

colnames = names(final.res.tab)
for (i in 2:ncol(final.res.tab)){
    final.res.tab[, colnames[i]][11] <- sum(final.res.tab[, colnames[i]][1:10])
}

for (i in 2:ncol(final.res.tab)){
    final.res.tab[, colnames[i]][12] <- mean(final.res.tab[, colnames[i]][1:10])
  }

print(final.res.tab)
#===================================сохранение
#write.table(final.res.tab, file = "d:/healthy_food/Итог.csv", sep=";",
           # row.names = FALSE, dec = ',',fileEncoding = "CP1251")
