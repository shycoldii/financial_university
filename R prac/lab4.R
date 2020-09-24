typeof(c(1,2,3))
mode(c(1,2,3))
str(c(1,2,3))

a<- c(7:4, 0)
b<-c(8, 10.5, 0, -2, 9)
res1 <- a+b
res2 <- a*b
res3 <- a/b
res4 <-mean(a)
res5 <- mean(b)
res6 <- sum(a)
res7 <- sum(b)
print("Результат сложения векторов"); paste0(res1)
print("Результат умножения векторов"); paste(res2)
print("Результат среднего арифметического для векторов"); paste(res4);  paste(res5)
print("Результат суммы значений для векторов"); paste(res6);  paste(res7)

w <- c(1,2,3)
typeof(w)
typeof(w[1])
w <- c(1,2,3, "тест")
typeof(w)
w <- c(1,2i,3, "тест")
typeof(w)
w <- c(TRUE,2i,3, "тест")
typeof(w)

a <- c(1,2,3)
b <- c(6,5,10.5)
print(a+b);print(a*b); print(a/b)
a <- c(1,2,3)
b <- c(1,2,3,4)
print(a+b);print(a*b); print(a/b)
a <- c(1,2,3)
b <- c("1","2","3")
print(a+b);print(a*b); print(a/b)
a <- c(1,2,3)
b <- c(1i,2i,3i)
print(a+b);print(a*b); print(a/b)
a <- c(1,2i,3,NULL)
b <- c(1i,2,TRUE)
print(a+b);print(a*b); print(a/b)

a<-c(1,2,3,4,5)
b<-c(FALSE,TRUE)
c <-c(NULL,1,Inf)
print(a&&b)
print(a&b)
#Вектор a короче b, поэтому произошло циклическое повторение
#Оператор && работал по парам 1 и False, поэтому все выражение проверять не стал
#Оператор & работал до конца и вернул итоговое значение
print(a&&c&&b)
#Не стало работать дальше, так как по логике оператора не проверяет другие элементы, если изначально
#вернуло False
print(a&b||c)
#Вернуло True, так как оператор ИЛИ оценивает левую часть и если хоть одно сразу равно
#True, то не проверяет до конца

(runif(10)*28+sample(-7:0,1))%/%1

r <- sample(10000) * -0.001
result=c()
for (number in r)
  if (number >= -7 & number <= -2)
    result <- append(result, number)
result <- sample(result,20)
print(result)

n = 10
w <-unlist(strsplit("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",""))
result<-sample(w,n)
print(result)

result <- c(sample(c("a","b","c","d","e","f","h"),n,replace=TRUE))
#2 способ