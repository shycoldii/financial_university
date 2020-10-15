{n <- readline("Введите число")
nn <- as.numeric(n)
ni <- as.integer(n)

if (nn - ni == 0) {
  print("Введенное число является целым.")
} else {
  print('Введенное число является Дробным.')
}
}
