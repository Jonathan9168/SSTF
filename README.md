# SSTF
Shortest Seek Time First [SSTF] disk scheduling algorithm calculator  
- Either edit predefined list of 'tracks_requested' and run or enter track list manually 
# Sample Output
```
Enter Starting track: 5

Enter Requested Track [Press F To Finish]: 6
Enter Requested Track [Press F To Finish]: 4
Enter Requested Track [Press F To Finish]: 3
Enter Requested Track [Press F To Finish]: 56
Enter Requested Track [Press F To Finish]: 7
Enter Requested Track [Press F To Finish]: 8
Enter Requested Track [Press F To Finish]: 45
Enter Requested Track [Press F To Finish]: 34
Enter Requested Track [Press F To Finish]: f

Starting Track: 5
Requested Tracks: [10, 50, 150, 11, 30, 23, 3, 5, 2, 3, 45, 122, 34, 12, 12, 1, 1, 12, 2, 3, 24, 4, 5, 6, 4, 3, 56, 7, 8, 45, 34] 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                      VISITATION ORDER                                                                                      
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
5 -> 5 -> 5 -> 4 -> 4 -> 3 -> 3 -> 3 -> 3 -> 2 -> 2 -> 1 -> 1 -> 6 -> 7 -> 8 -> 10 -> 11 -> 12 -> 12 -> 12 ---> 23 -> 24 --> 30 -> 34 -> 34 ---> 45 -> 45 -> 50 --> 56 ------> 122 ----> 150

Process finished with exit code 0

```
