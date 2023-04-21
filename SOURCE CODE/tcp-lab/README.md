# Lab 2

[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) 
this repo and clone it to your machine to get started!

## Team Members
- Melissa Shun
- Donya Badamchi

## Lab Question Answers

## Drive PDF
Answer for Question 1: 

   With 50% loss added, some numbers were missing on the server side and some sequences were fully lost.  THis is because UDp does not provide the error correction to recover lost packets. 
   
Answer for Question 2: 
   
   Reliability did not change for TCP; this is because TCP retransmits data back to the sender to recover any lost or corrupted packets.
   
Answer for Question 3: 
  
  TCP response was slower after spamming sequences. TCP essentially does more to send packets (error correction, retransmission, ordering) to ensure reliability nd also modifies transmission rate to match the current bandwitdh.
  

## tcp_server.c

1. What is argc and *argv[]?

    argc and *argv are the arguments taken by the main function, which sepcify the amount of 
    inputs/arguments and an array containing them.
    
2. What is a UNIX file descriptor and file descriptor table?

   the UNIX file descriptor is an integer value used to identify a file. The descriptor table are the array indices that are  pointers to file.
   source: https://www.geeksforgeeks.org/input-output-system-calls-c-create-open-close-read-write/

3. What is a struct? What's the structure of sockaddr_in?

   a structure groups different data values and types together. sockaddr_in is a 4-by

4. What are the input parameters and return value of socket()

    the parameters are3 integers: a communication domain, socket type, and protocol; it returns an integer (file descriptor for the socket).
    
5. What are the input parameters of bind() and listen()?

    Input parameters to bind are the integer sock_fd (file descriptor for socket), const struct sockaddr *addr, socklen_t addrlen.
    Parameters to bind() are int sock_fd, int backlog
    
6. Why use while(1)? Based on the code below, what problems might 
   occur if there are multiple simultaneous connections to handle?
   
   while(1) iterates the set of commands in its loop until the application is exited, making it useful for routines such as listening to and reading from a client; with multiple connections to handle the server might only connect to one client's socket.  
   
7. Research how the command fork() works. How can it be applied here 
   to better handle multiple connections?
   
    fork(): creates a new process concurent with the parent and allows users to run multiple connections simultaneously
    
8. This program makes several system calls such as 'bind', and 'listen.' 
   What exactly is a system call?
        
   A system call is how a program enacts a service from the operating system.
        

   
     
