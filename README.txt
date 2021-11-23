0.  Please write down the full names and netids of both your team members.
        Toshanraju Vysyaraju - tv135

1.  Briefly discuss how you implemented your recursive client functionality.
        I defined a function in client.txt that is called `lookup`. When the
        reads in a hostname from the input file, it calls `lookup` and passes
        in the hostname of RS, the port of RS, as well as the hostname from the
        input file. If RS responds with NS, the client will recursively call
        `lookup` again but will pass in the hostname of TS, the port of TS,
        as well as the hostname from the input file. In this way, client's
        `lookup` function is recursive.

2.  Are there known issues or functions that aren't working currently in your
    attached code? If so, explain.
        In my code, there are no known issues. The only thing that I am a 
        little confused about is that I am not sure if RS and TS should
        automatically quit after client is finished. Logically, it does not
        make sense for them to quit because servers continue to stay running
        even if the client quits. As a result, I have not coded them to quit
        after the client is done but that functionality can be added very easily.

3.  What problems did you face developing code for this project?
        I did not run into any problems while developing the code for this
        project.

4.  What did you learn by working on this project?
        While the first project gave a good introduction of the power of
        using sockets in python, this project gave me much more of an in
        depth understanding of how sockets work across different hosts.