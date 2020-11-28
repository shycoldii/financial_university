#!/bin/bash
cat sorted.ps | while read line
 do 
   name=`echo $line | cut -d" " -f 1`
   name+=".html"
   echo $name >> names
  # echo '<li>'$line'</li>' >> $name
 done
sort names > sortnames
cat sortnames | uniq > namesuniq
echo -e "<html>\n<title>Статистика процессов</title>\n<body><h1>Распределение процессов по пользователям</h1>" > index.html
cat namesuniq | while read line
 do
   name=`echo $line | cut -d "." -f 1`".total"
   proc=$(wc -l $line)
   echo "<p><b>Total Processes:"$proc"</b>" > $name
   echo $proc  >> index.html
   echo "<hr noshade>" >> index.html
 done
echo "</body></html>" >> index.html


