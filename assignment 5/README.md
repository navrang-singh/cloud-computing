This webapp uses php .
steps to run on localhost:-
    1 :- setup php dev enviroment .
    2 :- create a configuration.php .
        <?php
        define("DB_SERVER", "*************");
        define("DB_USER", "********");
        define("DB_PASSWORD", "***********");
        define("DB_NAME", "**********");

        $conn = new mysqli(DB_SERVER, DB_USER, DB_PASSWORD, DB_NAME);

        if($conn->connect_error){
            die("Connection error: ".$conn->connect_error);
        }

        ?>'

    3 :- put server_name,user_name,password,database_name in place of ******** .
    4 :- put configuration.php in folder feedback_app .
    5 :- start server ..

steps to run on aws :-

    1 :- set aws access key and secret access key in place of ******** in boto_rds.py .
    2 :- all set ...  run :- python -u boto_rds.py




