install.packages('xlsx') #패키지 설치
library(xlsx)            #패키지 불러오기
air <- read.xlsx('C:/Study/airqaulity.xlsx', header=T,
                 sheetIndex=1)
head(air)

libaray(xlsx)            #패키지 불러오기
my.iris <- subset(iris, Species='setosa') #setosa 품종 데이터만 추출
write.xlsx(my.iris, 'my_iris.xlsx', row.name=F) #파일 저장

#예제
library(xlsx)
setwd('C:/Study/test')
my.mtcars <- subset(mtcars, cyl<=6)
write.xlsx(my.mtcars, 'test.xlsx', row.names = F)
new.mtcars <- read.xlsx('test.xlsx', header=T, sheetIndex=1)

#예제 = 다이아몬드
setwd('C:/Study/Shiny')
library(ggplot2)
str(diamonds)
diamonds.new <- subset(diamonds, cut == 'Premium' & carat >= 2)
write.csv(diamonds.new, 'shiny_diamonds.csv', row.naems=F)

#전달받은 데이터에서 색이 0인 데이터를 제외하여 xlsx 파일 형식으로 제공
diamonds.load <- read.csv('shiny_diamonds.csv', header=T)
diamonds.new <- subset(diamonds.load, color != 'D')
library(xlsx)
write.xlsx(diamonds.new, 'shiny_diamonds.xlsx', row.name=F)

#회원등급 예제
library(svDialogs)
purchase <- dlgInput('Enter the purchase amount')$res
purchase <- as.numeric(purchase)

type <- NULL
ratio <- NULL

if (purchase >= 300000) {
  type <- '플래티넘'
  ratio <- 0.07
} else if (purchase >= 200000) {
  type <- '골드'
  ratio <- o.05
} else if (purchase >= 100000) {
  type <- '실버'
  ratio <- 0.03
} else {
  type <- '프렌즈'
  ratio <- 0.01
}

cat('고객님은', type, '회원으로 구매액의', ratio*100, '%가 적립됩니다.')


#사업부문별 매출액
ha <- c(54659, 61028, 53307, 46161, 54180)
he <- c(31215, 29863, 32098, 39684, 29707)
mc <- c(15104, 16133, 15222, 13208, 9986)
vs <- c(13470, 14231, 13401, 13552, 13193)
bs <- c(16513, 14947, 15112, 14392, 17091)

ds <- rbind(ha, he, ms, vs, bs)
colnames(ds) <- c('19.1Q', '19.2Q', '19.3Q', '19.4Q', '20.1Q')

barplot(ds, main = '사업부문별 매출액')

barplot(ds, main = '사업부문별 매출액',
        col = c('#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'))

barplot(ds, main = '사업부문별 매출액',
        col = c('#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'),
        horiz = T, las = 1)


barplot(ds, main = '사업부문별 매출액',
        col = c('#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'),
        horiz = T, las = 1,
        xlab = '억 원', beside = T)

par(mfrow = c(1, 1), mar = c(5, 5, 5, 10))

barplot(ds, main = '사업부문별 매출액',
        col = c('#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'),
        horiz = T, las = 1,
        xlab = '억 원', beside = T,
        legend.text = c('H&A', 'HE', 'MC', 'VS', 'BS'),
        args.legend = list(x='topright', bty='n', inset=c(-0.25, 0)))

par(mfrow = c(1,1), mar = c(5,4,4,2)+.1)
}