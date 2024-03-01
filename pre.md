
Good morning I m Xiaoyang Lyu. My main role is software structure designed and build the mostly program in the project. The next group menber is Jingyu Huang and welcome

Hi here Xiaoyang again and let me give a specific explanation of function procedure with practical demonstration. Firstly, please refer to the diagram for an overview of how the entire system runs.


The system starts in a closed state after initialization. Upon successful certification, it transitions to the open state. After the vehicle disappears from the webcam, the gate returns to the closed state.



Now i will explain the procedure with the prototype. Jiyuan Guo will assist me. It will divide into three steps. Firstly, as the car approach to the gate, the webcam captures all characters on the license plate. In the second step, the program compares these characters to the data stored in the database. If there is a match, it proceeds to the third step. 
The program will control the motor, and LCD to indicate the driver that he can enter the park.

additionally, there is terminal command line db management application that allow the manager to easily manage the database through actions add, delete, search and modify. Let's demonstration how it work. 


To begin with, Let's replace a plate which doesn't stored in the database. obviously, it cannot pass the certification. Now Please focus on my ipad. It is already connect to the Raspberry pi via ssh.  I will use the UI to add this plate to our db. lets run the ui, and you can see the different options. Input 1 to select the add.  now done. Lets check if the car pass certification. it's successful. thank you very much and lets move to the next parts with dian wang's presentation.