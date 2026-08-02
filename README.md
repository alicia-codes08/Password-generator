The second branch (add-test) has everything the main-branch has. The only difference from the main-branch is 
that I added a test for generator.py. The first function is a fixture. There I made an instance and let 
the methods of the class from generator.py excecute. So I have results on the instance to test. 
In test_checking_lenght() got the lenght of the two passwords tested. The function 
test_moved_place() tested the most important thing! It tested if you can get the whole using-password
with the keeping-password and the moved place of the elements. There you started with the keeping-passwords and 
the moved place, that shows how many indexes the elements are away from the using-passwords ones. A for-loop 
went trough the keeping-password and build up through moved place the using-password. In the end it compared 
the original using-password with the "traced back" one. 

I already knew that it worked, but I still added a test, to show in another way that my generator works. 
I also wanted to support my learning aswell with writing a test with pytest and I wanted to try adding 
another branch into my project. 
