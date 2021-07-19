# K-means clustering (English)

## Description

K-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells. k-means clustering minimizes within-cluster variances (squared Euclidean distances), but not regular Euclidean distances, which would be the more difficult Weber problem: the mean optimizes squared errors, whereas only the geometric median minimizes Euclidean distances. For instance, better Euclidean solutions can be found using k-medians and k-medoids.

Given a set of observations (x1, x2, ..., xn), where each observation is a d-dimensional real vector, k-means clustering aims to partition the n observations into k (≤ n) sets S = {S1, S2, ..., Sk} so as to minimize the within-cluster sum of squares (WCSS) (i.e. variance). Formally, the objective is to find:     

<p align="center">
  <img src="https://user-images.githubusercontent.com/86201781/125795860-980f8c22-4fb9-4724-b292-20dee2ed2200.png">
</p>

where μi is the mean of points in Si. This is equivalent to minimizing the pairwise squared deviations of points in the same cluster:


<img src = "https://user-images.githubusercontent.com/86201781/125796322-5150670a-90f0-41f1-a3a2-b1755b224b96.png">



The equivalence can be deduced from identity     ![image](https://user-images.githubusercontent.com/86201781/125796366-f9a360b8-2e66-466d-bf11-bd9fabd4f71b.png)     Because the total variance is constant, this is equivalent to maximizing the sum of squared deviations between points in different clusters (between-cluster sum of squares, BCSS), which follows from the law of total variance.

## Demonstration of the standard algorithm
1. k initial "means" (in this case k=3) are randomly generated within the data domain (shown in color).

![image](https://user-images.githubusercontent.com/86201781/125801421-a4b2c12e-3928-41d0-ac8e-a1cac84c38f2.png)

2. k clusters are created by associating every observation with the nearest mean. The partitions here represent the Voronoi diagram generated by the means.

![image](https://user-images.githubusercontent.com/86201781/125801624-1ce03d9f-e55e-4396-9568-57f120369fd1.png)

3. The centroid of each of the k clusters becomes the new mean.

![image](https://user-images.githubusercontent.com/86201781/125801948-1ee19df0-b7d0-4571-b005-51dbe88bc9f0.png)

4. Steps 2 and 3 are repeated until convergence has been reached.

![image](https://user-images.githubusercontent.com/86201781/125801974-db15f177-6749-4d34-9e72-aca049fa76d4.png)

## Problem Description

In order to determine the feasibility of growing weeds as a cash crop, samples have been
taken from wild weeds in various locations. In each sample the amount of vitiamin C, and the amount
of gamma-linolenic acid (GLA) has been measured. The samples with low levels of nutrients or samples
containing toxins are discarded, so in the data only samples from edible weeds remain. The next step is to
understand how many species of edible weeds are present at a each location.

The task  is to write a program to display the different species of weed present at a
given location, based only on the given data. It is unknown how many species may be involved at any one
location, but the number is believed to be between two and four. At a particular location, the samples from
one particular species will have similar levels of nutrients and determining the species present is a matter
of grouping the data so samples in a given group belong to the same species. This grouping process is
called clustering. Given a file of pairs of integers, giving the levels of Vitamin C and GLA, the task is to
plot the data with each species given a different color, and to produce a representative for each species at
that location. The representative of a species will have the average amounts of nutrients of the members
of the species.

## Problem Details

A given input file (locationA.txt, locationB.txt, locationC.txt, backyard.txt) is associated with a particular area. Each line of the file contains the infomation for a particular sample and the Vitamin C and GLA measures for a sample is separated by a comma. For example

![image](https://user-images.githubusercontent.com/86201781/125835746-2666ac69-9b30-4650-b2d6-58a5c2a41748.png)

is the contents of the file backyard.txt giving information on seven samples, and the last sample has
vitamin C level 220 and GLA level 190.

## How to use

Here are the steps for how to open, use and utilize the program:
- First, download all of the files listed above;
- Put all the files in one folder;
- Open the file Project_k-means.py;
- The program will open a command console in which it will ask you to name a .txt file located in the same folder;
- Finally, the program will output a graph with results of clusterized data.


*The program can use other .txt file that are in the same format as provided files.



# Метод k-средних (Русский)

## Описание

Кластеризация k-средних - это метод векторного квантования, первоначально из обработки сигналов, который направлен на разделение n наблюдений на k кластеров, в которых каждое наблюдение принадлежит кластеру с ближайшим средним значением (центры кластеров или центроид кластера), служащий прототипным кластером. Это приводит к разделению пространства данных на ячейки диаграммы Вороного. Кластеризация k-средних минимизирует дисперсию внутри кластера (квадраты евклидовых расстояний), но не регулярные евклидовы расстояния, что было бы более сложной проблемой Вебера: среднее оптимизирует квадратичные ошибки, тогда как только геометрическая медиана минимизирует евклидовы расстояния. Например, лучшие евклидовы решения можно найти с помощью k-медиан и k-медоидов.

Учитывая набор наблюдений (x1, x2, ..., xn), где каждое наблюдение является d-мерным вещественным вектором, кластеризация k-средних нацелена на разделение n наблюдений на k (≤ n) наборов S = {S1, S2, ..., Sk}, чтобы минимизировать внутрикластерную сумму квадратов (WCSS) (т. е. Дисперсию). Формально цель - найти:

<p align="center">
  <img src="https://user-images.githubusercontent.com/86201781/125795860-980f8c22-4fb9-4724-b292-20dee2ed2200.png">
</p>

где μi - среднее значение точек в Si. Это эквивалентно минимизации попарных квадратов отклонений точек в одном кластере:

<img src = "https://user-images.githubusercontent.com/86201781/125796322-5150670a-90f0-41f1-a3a2-b1755b224b96.png">

Эквивалентность выводится из тождества  ![image](https://user-images.githubusercontent.com/86201781/125796366-f9a360b8-2e66-466d-bf11-bd9fabd4f71b.png)  Поскольку общая дисперсия постоянна, это эквивалентно максимизации суммы квадратов отклонений между точками в разных кластерах (сумма квадратов между кластерами, BCSS), что следует из закона общей дисперсии.

## Демонстрация стандартного алгоритма
1. Исходные точки и случайно выбранные начальные точки.

![image](https://user-images.githubusercontent.com/86201781/125801421-a4b2c12e-3928-41d0-ac8e-a1cac84c38f2.png)

2. Точки, отнесённые к начальным центрам. Разбиение на плоскости — диаграмма Вороного относительно начальных центров.

![image](https://user-images.githubusercontent.com/86201781/125801624-1ce03d9f-e55e-4396-9568-57f120369fd1.png)

3. Вычисление новых центров кластеров (Ищется центр масс).

![image](https://user-images.githubusercontent.com/86201781/125801948-1ee19df0-b7d0-4571-b005-51dbe88bc9f0.png)

4. Предыдущие шаги, за исключением первого, повторяются, пока алгоритм не сойдётся.

![image](https://user-images.githubusercontent.com/86201781/125801974-db15f177-6749-4d34-9e72-aca049fa76d4.png)

## Описание задачи

Чтобы определить возможность выращивания сорняков в качестве товарной культуры, были взяты образцы диких сорняков в различных местах. В каждом образце измеряли количество витамина С и количество гамма-линоленовой кислоты (GLA). Образцы с низким содержанием питательных веществ или образцы, содержащие токсины, отбрасываются, поэтому в данных остаются только образцы съедобных сорняков. Следующий шаг - понять, сколько видов съедобных сорняков присутствует в каждом месте.

Задача состоит в том, чтобы написать программу для отображения различных видов сорняков, присутствующих в данном месте, только на основе заданных данных. Неизвестно, сколько видов может быть задействовано в каком-либо одном месте, но предполагается, что их количество составляет от двух до четырех. В определенном месте образцы одного конкретного вида будут иметь одинаковые уровни питательных веществ, и определение присутствующих видов является вопросом
группировки данных таким образом, чтобы образцы в данной группе принадлежали к одному виду. Этот процесс группировки называется кластеризацией. Имея файл пар целых чисел, дающий уровни витамина C и GLA, задача состоит в том, чтобы
нанесите на график данные с каждым видом, выделенным разным цветом, и получите представителя для каждого вида в этом месте. Представитель вида будет иметь среднее количество питательных веществ по сравнению с представителями вида.

## Детали задачи

Данный входной файл (locationA.txt, locationB.txt, locationC.txt, backyard.txt) связан с определенной областью. Каждая строка файла содержит информацию для конкретного образца, а показатели витамина C и GLA для образца разделены запятыми. Например

![image](https://user-images.githubusercontent.com/86201781/125835746-2666ac69-9b30-4650-b2d6-58a5c2a41748.png)

это содержимое файла backyard.txt, в котором содержится информация о семи образцах, причем последний образец имеет уровень 220 витамина C и уровень GLA 190.

## Как использовать

Шаги по открытию, использованию программы:
- Сначала загрузите все файлы, перечисленные выше;
- Поместите все файлы в одну папку;
- Откройте файл Project_k-means.py;
- Программа откроет командную консоль, в которой попросит вас назвать файл .txt, расположенный в той же папке;
- Наконец, программа выведет график с результатами кластеризованных данных.

* Программа может использовать другие файлы .txt в том же формате, что и предоставленные файлы.
