{n <- c()
x <- 0
while(x<8){
  c <- readline("Введите число: ")
  c <- as.numeric(c)
  n <- append(n,c)
  x <- x+1
}
n <- sort(n, decreasing = TRUE)
res <- ''
res <- paste(n[1],'>',n[2],'>',n[3],'>',n[4],'>',n[5],'>',n[6],'>',n[7],'>',n[8])
print(res)
}

