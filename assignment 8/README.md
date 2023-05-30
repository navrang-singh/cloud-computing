+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Run hadoop in docker container ...

download Dockerfile and open the dir. in terminal and run ..

docker build -t hadoop_img .

docker run -dit --name=hadoop_container -v ~/Desktop/'CS351 - IT Workshop'/assignment8/:/code hadoop_img

docker exec -it hadoop_container /bin/bash


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




steps to run :- 

1 :- set up hadoop env in local machine.

2 :- unzip the given folder .

3 :- open terminal and change working directory to unzipped folder .

4 :- then simply run the given commands (remember to delete output directory or simply change -output dir path):--


(After running .. Output that we get is in output directory of each questions directory ..)

                
                
                
                Question 0 :------------------------------------------------------------

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-* -input ./que_0/input  -output ./que_0/output  -mapper ./que_0/mapper.py -reducer ./que_0/reducer.py




                Question 1 :------------------------------------------------------------

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-* -input ./que_1/input  -output ./que_1/output  -mapper ./que_1/mapper.py -reducer ./que_1/reducer.py


                
                Question 2 :--------------------------------------------------------------


hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-* -input ./que_2/input  -output ./que_2/output  -mapper ./que_2/mapper.py -reducer ./que_2/reducer.py -combiner ./que_2/combiner.py


                Question 3 :-------------------------------------------------------------

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-* -output ./que_3/output  -mapper ./que_3/mapper.py -reducer ./que_3/reducer.py -file ./que_3/iris.csv -input ./que_3/input
