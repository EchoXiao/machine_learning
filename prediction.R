# machine_learning

#Project 1
#5/4/2016


which(is.na(p$Employees))
null <- which(is.na(p$Employees))
p <- p[-null,]


#hierarhical clustering
p_hc <- p[,c(4:9)]
euclid <- dist(p_hc, method="euclidean")
View(as(euclid, "matrix"))
hierarchical <- hclust(euclid, method="ward.D")
plot(hierarchical)

p_hc$cluster <- cutree(hierarchical, k=6)
summary(p_hc[p_hc$cluster == 1,][-ncol(p_hc)])
summary(p_hc[p_hc$cluster == 2,][-ncol(p_hc)])
summary(p_hc[p_hc$cluster == 3,][-ncol(p_hc)])
summary(p_hc[p_hc$cluster == 4,][-ncol(p_hc)])
summary(p_hc[p_hc$cluster == 5,][-ncol(p_hc)])
summary(p_hc[p_hc$cluster == 6,][-ncol(p_hc)])





#correlation

cor(p[,c(1,4,6:9)])


#k-means


View(p)
wss <- c(rep(0,10))
bss <- c(rep(0,10))
p_km <- p[,c(4,6:9)]
for (i in 2:11){
  temp <- kmeans(p[,c(4,6:9)], center=i)
  wss[i-1] <- temp$tot.withinss
  bss[i-1] <- temp$betweenss
}

plot((1:10),wss,type="b",col="blue")
par(new=T)
plot((1:10),bss,type="b",axes=F, xlab="",ylab="",col="dark red")
par(new=F)





#k-nn and decision tree
p_dc <- p[,c(4:9)]
ind <- sample(nrow(p_dc), floor(nrow(p_dc)*0.5)) 
p_train <- p_dc[ind,]
p_test <- p_dc[-ind,]
View(p_dc)

#decision tree
library(rpart)
library(rpart.plot)

p_dc.rpart <- rpart(Price~ Net.income+Total.assets+Employees+Market.value, data=p_test)
rpart.plot(p_dc.rpart)


library(class)
p_knn <- scale(p[,c(4,6:9)], center=FALSE)


library(caret)

p_train <- train(Price~., data=p_train, method="knn")
p_train$bestTune

p_predict <- predict(p_train, newdata=p_test)
View(as.matrix(knn_predict))
RMSE(p_predict,p_test$Price)





