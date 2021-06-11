cafe <- list(espresso = c(4, 5, 3, 6, 5, 4, 7),
             americano = c(63, 68, 64, 68, 72, 89, 94),
             latte = c(61, 70, 59, 71, 71, 92, 88),
             price = c(2.0, 2.5, 3.0),
             menu = c('espresso', 'americano', 'latte'))

cafe$menu <- factor(cafe$menu)

names(cafe$price) <- cafe$menu

sale.espresso <- cafe$price['espresso'] * cafe$espresso
sale.americano <- cafe$price['americano'] * cafe$americano
sale.latte <- cafe$price['latte'] * cafe$latte

sale.day <- sale.espresso + sale.americano + sale.latte
names(sale.day) <- c('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
sum(sale.day)
sale.mean <- mean(sale.day)
names(sale.day[sale.day] >= sale.mean)

-------------------------------------------------------
  
accident <- c(31, 26, 42, 47, 50, 54, 70, 66, 43, 32, 32, 22)
names(accident) <- c('M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 
                     'M9', 'M10', 'M11', 'M12')
accident

sum(accident)

max(accident)
min(accident)

accident*0.9

accident[accident>=50]

month.50 <- accident[accident >= 50]
names(month.50)
names(accident[accident >= 50])

length(accident[accident<50])

M6.acc <- accident[6]
accident[accident > M6.acc]
accident[accident > accident[6]]


-------------------------------------------------------
class(trees)
str(trees)

girth.mean <- mean(trees$Girth)

candidate <- subset(tress, Girth >= girth.mean & Height > 80 & Volume > 50)
candidate
nrow(candidate)

