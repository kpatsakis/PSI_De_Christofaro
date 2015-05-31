# PSI_De_Christofaro
A trivial implementation of the protocol of De Christofaro et Tsudik [1] for the computation of private set intersection.
The code is written in Python and you will need to install Flask (http://flask.pocoo.org/) and gmpy(https://code.google.com/p/gmpy/) to run the code.
The implementation is quite straightforward, first run *generate_elements.py* to create the client and server data. You can skip this step and write them down on your own by simply writing comma separeted numbers in *client_elements.txt* and *srv_elements.txt* respectively.
Running psi_de_christofaro will start a small web server (flask) in port 5000 which waits for client's elements. The public key of the server n is stored in a text file called *srv.key*. On receiving the comma separeted values, the server performs the calculations and returns a json text to the client.
The client performs the last steps of the protocol and simply returns the common elements.

[1] De Cristofaro, Emiliano, and Gene Tsudik. "Practical private set intersection protocols with linear complexity." Financial Cryptography and Data Security. Springer Berlin Heidelberg, 2010. 143-159.
