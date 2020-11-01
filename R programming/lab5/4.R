{n <- readline("Введите число")
n <- as.numeric(n)
res2 <- 0
ch <- n 
for(i in 1:(n)){
  res2 = res2+i;
}
s <- paste('Введенное число:', ch, '; результат: ', res2)
print(s)
}
